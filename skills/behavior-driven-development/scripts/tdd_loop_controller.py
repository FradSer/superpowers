#!/usr/bin/env python3
"""Legacy file-artifact loop controller for behavior-driven-development skill.

Default skill execution is conversation-memory flow; this script remains for
external harness compatibility.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


FAILURE_COUNT_PATTERNS = [
    re.compile(r"(\d+)\s+failed", re.IGNORECASE),
    re.compile(r"failures?:\s*(\d+)", re.IGNORECASE),
]


@dataclass
class CommandResult:
    command: str
    exit_code: int
    stdout: str
    stderr: str

    @property
    def combined_output(self) -> str:
        return "\n".join(part for part in [self.stdout, self.stderr] if part)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run RED->GREEN->REFACTOR loops per scenario")
    parser.add_argument("--workspace", required=True, help="Absolute path to workspace")
    parser.add_argument("--scenarios-json", required=True, help="Path to scenarios json")
    parser.add_argument("--verify-cmd-template", required=True, help="Template command; may include {scenario_id}")
    parser.add_argument("--patch-cmd", required=True, help="Patch command executed each iteration")
    parser.add_argument("--max-iterations", type=int, default=6)
    parser.add_argument("--max-stalled", type=int, default=2)
    parser.add_argument("--report-dir", required=True)
    return parser.parse_args()


def run_command(command: str, cwd: Path, extra_env: dict[str, str] | None = None) -> CommandResult:
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)

    completed = subprocess.run(
        command,
        cwd=str(cwd),
        env=env,
        shell=True,
        text=True,
        capture_output=True,
    )
    return CommandResult(
        command=command,
        exit_code=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )


def write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8")


def append_jsonl(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")


def load_scenarios(path: Path) -> list[dict[str, Any]]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(raw, dict) and isinstance(raw.get("scenarios"), list):
        return raw["scenarios"]
    if isinstance(raw, list):
        return raw
    raise ValueError(f"Unsupported scenarios format in {path}")


def normalize_id(value: str, index: int) -> str:
    raw = value.strip() if value else f"SCN_{index:03d}"
    cleaned = re.sub(r"[^A-Za-z0-9_.-]", "_", raw)
    return cleaned or f"SCN_{index:03d}"


def scenario_text(scenario: dict[str, Any]) -> str:
    lines: list[str] = []
    title = scenario.get("title") or scenario.get("name") or "untitled"
    lines.append(f"Scenario: {title}")

    for key, prefix in (("given", "Given"), ("when", "When"), ("then", "Then")):
        value = scenario.get(key, [])
        if isinstance(value, list):
            for item in value:
                lines.append(f"{prefix} {item}")
        elif isinstance(value, str) and value.strip():
            lines.append(f"{prefix} {value.strip()}")

    if len(lines) == 1:
        lines.append("Given scenario definition from source json")
    return "\n".join(lines)


def extract_failure_count(output: str) -> int | None:
    for pattern in FAILURE_COUNT_PATTERNS:
        match = pattern.search(output)
        if match:
            try:
                return int(match.group(1))
            except ValueError:
                return None
    return None


def failure_fingerprint(exit_code: int, output: str) -> str:
    trimmed = "\n".join(output.strip().splitlines()[:80])
    digest = hashlib.sha256(trimmed.encode("utf-8")).hexdigest()[:16]
    return f"{exit_code}:{digest}"


def failure_reason(exit_code: int, output: str) -> str:
    for line in output.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped[:400]
    return f"verify command exited with code {exit_code}"


def extract_patch_summary(patch_result: CommandResult) -> str | None:
    for line in (patch_result.stdout + "\n" + patch_result.stderr).splitlines():
        if line.startswith("PATCH_SUMMARY:"):
            return line.split("PATCH_SUMMARY:", 1)[1].strip() or "patch summary provided"
    return None


def is_git_workspace(workspace: Path) -> bool:
    check = subprocess.run(
        ["git", "-C", str(workspace), "rev-parse", "--is-inside-work-tree"],
        text=True,
        capture_output=True,
    )
    return check.returncode == 0


def git_snapshot(workspace: Path) -> str:
    status = subprocess.run(
        ["git", "-C", str(workspace), "status", "--porcelain"],
        text=True,
        capture_output=True,
    )
    diff = subprocess.run(
        ["git", "-C", str(workspace), "diff", "--name-status"],
        text=True,
        capture_output=True,
    )
    return "\n".join([status.stdout.strip(), diff.stdout.strip()])


def git_patch_summary(workspace: Path) -> str | None:
    summary = subprocess.run(
        ["git", "-C", str(workspace), "diff", "--shortstat"],
        text=True,
        capture_output=True,
    )
    text = summary.stdout.strip()
    return text or None


def create_manual_decision(
    decision_path: Path,
    scenario_id: str,
    scenario_definition: dict[str, Any],
    reason: str,
    verify_cmd: str,
    max_iterations: int,
    max_stalled: int,
    latest_log: Path | None,
) -> None:
    excerpt = ""
    if latest_log and latest_log.exists():
        lines = latest_log.read_text(encoding="utf-8").splitlines()
        excerpt = "\n".join(lines[:120])

    content = [
        f"# Manual Decision Required: {scenario_id}",
        "",
        f"- **Reason:** {reason}",
        f"- **Verify Command:** `{verify_cmd}`",
        f"- **Max Iterations:** {max_iterations}",
        f"- **Max Stalled:** {max_stalled}",
        "",
        "## Scenario",
        "",
        "```json",
        json.dumps(scenario_definition, ensure_ascii=False, indent=2),
        "```",
        "",
    ]

    if excerpt:
        content.extend(
            [
                "## Latest Failure Output (excerpt)",
                "",
                "```text",
                excerpt,
                "```",
                "",
            ]
        )

    content.extend(
        [
            "## Recommended Next Actions",
            "",
            "1. Inspect failure output and identify root cause.",
            "2. Decide whether to adjust tests, implementation, or scenario assumptions.",
            "3. Re-run orchestrator with updated context once decision is made.",
        ]
    )
    write_text(decision_path, "\n".join(content))


def record_event(
    events_file: Path,
    scenario_id: str,
    iteration: int,
    phase: str,
    verify_cmd: str,
    verify_result: CommandResult,
    verify_log: Path,
    failure_count: int | None,
    fingerprint: str,
    progress: bool,
    patch_exit_code: int | None = None,
    patch_summary: str | None = None,
    patch_log: Path | None = None,
) -> None:
    reason = failure_reason(verify_result.exit_code, verify_result.combined_output)
    payload: dict[str, Any] = {
        "timestamp": utc_now(),
        "scenario_id": scenario_id,
        "iteration": iteration,
        "phase": phase,
        "verify_cmd": verify_cmd,
        "exit_code": verify_result.exit_code,
        "failure_count": failure_count,
        "failure_fingerprint": fingerprint,
        "failure_reason": reason,
        "progress": progress,
        "verify_log": str(verify_log),
    }
    if patch_exit_code is not None:
        payload["patch_exit_code"] = patch_exit_code
    if patch_summary is not None:
        payload["patch_summary"] = patch_summary
    if patch_log is not None:
        payload["patch_log"] = str(patch_log)
    append_jsonl(events_file, payload)


def scenario_state(status: str, reason: str, scenario_id: str, iterations: int) -> dict[str, Any]:
    return {
        "id": scenario_id,
        "status": status,
        "reason": reason,
        "iterations": iterations,
    }


def run_single_scenario(
    workspace: Path,
    scenario: dict[str, Any],
    index: int,
    verify_cmd_template: str,
    patch_cmd: str,
    max_iterations: int,
    max_stalled: int,
    report_dir: Path,
    events_file: Path,
) -> dict[str, Any]:
    scenario_id = normalize_id(str(scenario.get("id", "")), index)
    verify_cmd = verify_cmd_template.replace("{scenario_id}", scenario_id)
    text = scenario_text(scenario)

    artifacts_dir = report_dir / "artifacts" / scenario_id
    artifacts_dir.mkdir(parents=True, exist_ok=True)

    red_result = run_command(verify_cmd, workspace)
    red_log = artifacts_dir / "verify_red.log"
    write_text(red_log, red_result.combined_output)

    red_failure_count = extract_failure_count(red_result.combined_output)
    red_fingerprint = failure_fingerprint(red_result.exit_code, red_result.combined_output)

    red_progress = red_result.exit_code != 0
    record_event(
        events_file=events_file,
        scenario_id=scenario_id,
        iteration=0,
        phase="RED",
        verify_cmd=verify_cmd,
        verify_result=red_result,
        verify_log=red_log,
        failure_count=red_failure_count,
        fingerprint=red_fingerprint,
        progress=red_progress,
    )

    if red_result.exit_code == 0:
        decision = report_dir / "manual_decision" / f"{scenario_id}.md"
        create_manual_decision(
            decision_path=decision,
            scenario_id=scenario_id,
            scenario_definition=scenario,
            reason="blocked_red_missing",
            verify_cmd=verify_cmd,
            max_iterations=max_iterations,
            max_stalled=max_stalled,
            latest_log=red_log,
        )
        return scenario_state("blocked", "blocked_red_missing", scenario_id, 0)

    git_enabled = is_git_workspace(workspace)
    previous_failure_count = red_failure_count
    previous_fingerprint = red_fingerprint
    stalled = 0
    latest_failure_log: Path = red_log

    for iteration in range(1, max_iterations + 1):
        patch_log = artifacts_dir / f"patch_{iteration}.log"
        verify_log = artifacts_dir / f"verify_{iteration}.log"

        env = {
            "SCENARIO_ID": scenario_id,
            "SCENARIO_TEXT": text,
            "ITERATION_INDEX": str(iteration),
            "LAST_FAILURE_FILE": str(latest_failure_log),
            "VERIFY_CMD": verify_cmd,
        }

        before_snapshot = git_snapshot(workspace) if git_enabled else ""
        patch_result = run_command(patch_cmd, workspace, env)
        write_text(patch_log, patch_result.combined_output)
        after_snapshot = git_snapshot(workspace) if git_enabled else ""

        code_changed = before_snapshot != after_snapshot if git_enabled else patch_result.exit_code == 0

        patch_summary = extract_patch_summary(patch_result)
        if patch_summary is None:
            patch_summary = git_patch_summary(workspace) if git_enabled and code_changed else "no patch summary reported"

        verify_result = run_command(verify_cmd, workspace)
        write_text(verify_log, verify_result.combined_output)

        failure_count = extract_failure_count(verify_result.combined_output)
        fingerprint = failure_fingerprint(verify_result.exit_code, verify_result.combined_output)

        if verify_result.exit_code == 0:
            record_event(
                events_file=events_file,
                scenario_id=scenario_id,
                iteration=iteration,
                phase="GREEN",
                verify_cmd=verify_cmd,
                verify_result=verify_result,
                verify_log=verify_log,
                failure_count=failure_count,
                fingerprint=fingerprint,
                progress=True,
                patch_exit_code=patch_result.exit_code,
                patch_summary=patch_summary,
                patch_log=patch_log,
            )

            refactor_result = run_command(verify_cmd, workspace)
            refactor_log = artifacts_dir / "verify_refactor.log"
            write_text(refactor_log, refactor_result.combined_output)
            refactor_count = extract_failure_count(refactor_result.combined_output)
            refactor_fingerprint = failure_fingerprint(refactor_result.exit_code, refactor_result.combined_output)
            record_event(
                events_file=events_file,
                scenario_id=scenario_id,
                iteration=iteration,
                phase="REFACTOR",
                verify_cmd=verify_cmd,
                verify_result=refactor_result,
                verify_log=refactor_log,
                failure_count=refactor_count,
                fingerprint=refactor_fingerprint,
                progress=refactor_result.exit_code == 0,
            )

            if refactor_result.exit_code == 0:
                return scenario_state("passed", "passed", scenario_id, iteration)

            decision = report_dir / "manual_decision" / f"{scenario_id}.md"
            create_manual_decision(
                decision_path=decision,
                scenario_id=scenario_id,
                scenario_definition=scenario,
                reason="refactor_regression",
                verify_cmd=verify_cmd,
                max_iterations=max_iterations,
                max_stalled=max_stalled,
                latest_log=refactor_log,
            )
            return scenario_state("escalated", "refactor_regression", scenario_id, iteration)

        failure_count_decreased = (
            previous_failure_count is not None
            and failure_count is not None
            and failure_count < previous_failure_count
        )
        fingerprint_changed = fingerprint != previous_fingerprint
        progress = bool(failure_count_decreased or (fingerprint_changed and code_changed))

        if progress:
            stalled = 0
        else:
            stalled += 1

        record_event(
            events_file=events_file,
            scenario_id=scenario_id,
            iteration=iteration,
            phase="GREEN",
            verify_cmd=verify_cmd,
            verify_result=verify_result,
            verify_log=verify_log,
            failure_count=failure_count,
            fingerprint=fingerprint,
            progress=progress,
            patch_exit_code=patch_result.exit_code,
            patch_summary=patch_summary,
            patch_log=patch_log,
        )

        previous_failure_count = failure_count
        previous_fingerprint = fingerprint
        latest_failure_log = verify_log

        if stalled >= max_stalled:
            decision = report_dir / "manual_decision" / f"{scenario_id}.md"
            create_manual_decision(
                decision_path=decision,
                scenario_id=scenario_id,
                scenario_definition=scenario,
                reason="stalled_no_progress",
                verify_cmd=verify_cmd,
                max_iterations=max_iterations,
                max_stalled=max_stalled,
                latest_log=latest_failure_log,
            )
            return scenario_state("escalated", "stalled_no_progress", scenario_id, iteration)

    decision = report_dir / "manual_decision" / f"{scenario_id}.md"
    create_manual_decision(
        decision_path=decision,
        scenario_id=scenario_id,
        scenario_definition=scenario,
        reason="max_iterations_exceeded",
        verify_cmd=verify_cmd,
        max_iterations=max_iterations,
        max_stalled=max_stalled,
        latest_log=latest_failure_log,
    )
    return scenario_state("escalated", "max_iterations_exceeded", scenario_id, max_iterations)


def main() -> int:
    args = parse_args()

    workspace = Path(args.workspace).expanduser().resolve()
    scenarios_json = Path(args.scenarios_json).expanduser().resolve()
    report_dir = Path(args.report_dir).expanduser().resolve()

    if not workspace.exists():
        print(f"workspace does not exist: {workspace}", file=sys.stderr)
        return 2
    if not scenarios_json.exists():
        print(f"scenarios json does not exist: {scenarios_json}", file=sys.stderr)
        return 2

    scenarios = load_scenarios(scenarios_json)

    report_dir.mkdir(parents=True, exist_ok=True)
    events_file = report_dir / "events.jsonl"
    if events_file.exists():
        events_file.unlink()

    started_at = utc_now()
    results: list[dict[str, Any]] = []

    for idx, scenario in enumerate(scenarios, start=1):
        result = run_single_scenario(
            workspace=workspace,
            scenario=scenario,
            index=idx,
            verify_cmd_template=args.verify_cmd_template,
            patch_cmd=args.patch_cmd,
            max_iterations=args.max_iterations,
            max_stalled=args.max_stalled,
            report_dir=report_dir,
            events_file=events_file,
        )
        results.append(result)

    summary = {
        "started_at": started_at,
        "finished_at": utc_now(),
        "workspace": str(workspace),
        "scenarios_file": str(scenarios_json),
        "max_iterations": args.max_iterations,
        "max_stalled": args.max_stalled,
        "scenario_count": len(results),
        "scenarios": results,
    }

    write_text(report_dir / "summary.json", json.dumps(summary, ensure_ascii=False, indent=2))

    has_failed = any(item["status"] in {"blocked", "escalated"} for item in results)
    return 1 if has_failed else 0


if __name__ == "__main__":
    sys.exit(main())
