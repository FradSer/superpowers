#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SKILL_FILE="$REPO_ROOT/skills/behavior-driven-development/SKILL.md"
CONTRACT_FILE="$REPO_ROOT/skills/behavior-driven-development/references/loop-contract.md"

grep -q "_index.md" "$SKILL_FILE"
grep -q "bdd-scenarios.md" "$SKILL_FILE"
grep -q "Do not generate .*summary.json.*events.jsonl" "$SKILL_FILE"

grep -Eq "conversation-memory|conversation flow" "$CONTRACT_FILE"
grep -q "Do not generate .*summary.json.*events.jsonl" "$CONTRACT_FILE"

echo "[PASS] behavior-driven-development memory contract checks"
