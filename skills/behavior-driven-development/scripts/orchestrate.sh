#!/usr/bin/env bash
set -euo pipefail

# Legacy compatibility wrapper.
# Default behavior-driven-development flow is conversation-memory execution.

usage() {
  cat <<'EOF'
Usage:
  orchestrate.sh \
    --workspace <abs_path> \
    --scenarios-json <abs_path> \
    --verify-cmd-template "<cmd with {scenario_id}>" \
    --patch-cmd "<agent patch command>" \
    [--max-iterations <n>] \
    [--max-stalled <n>] \
    --report-dir <abs_path>
EOF
}

WORKSPACE=""
SCENARIOS_JSON=""
VERIFY_CMD_TEMPLATE=""
PATCH_CMD=""
MAX_ITERATIONS="6"
MAX_STALLED="2"
REPORT_DIR=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --workspace)
      WORKSPACE="$2"
      shift 2
      ;;
    --scenarios-json)
      SCENARIOS_JSON="$2"
      shift 2
      ;;
    --verify-cmd-template)
      VERIFY_CMD_TEMPLATE="$2"
      shift 2
      ;;
    --patch-cmd)
      PATCH_CMD="$2"
      shift 2
      ;;
    --max-iterations)
      MAX_ITERATIONS="$2"
      shift 2
      ;;
    --max-stalled)
      MAX_STALLED="$2"
      shift 2
      ;;
    --report-dir)
      REPORT_DIR="$2"
      shift 2
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage
      exit 2
      ;;
  esac
done

if [[ -z "$WORKSPACE" || -z "$SCENARIOS_JSON" || -z "$VERIFY_CMD_TEMPLATE" || -z "$PATCH_CMD" || -z "$REPORT_DIR" ]]; then
  echo "Missing required arguments" >&2
  usage
  exit 2
fi

for path_value in "$WORKSPACE" "$SCENARIOS_JSON" "$REPORT_DIR"; do
  if [[ "$path_value" != /* ]]; then
    echo "Expected absolute path, got: $path_value" >&2
    exit 2
  fi
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONTROLLER="$SCRIPT_DIR/tdd_loop_controller.py"

if [[ ! -f "$CONTROLLER" ]]; then
  echo "Controller not found: $CONTROLLER" >&2
  exit 2
fi

python3 "$CONTROLLER" \
  --workspace "$WORKSPACE" \
  --scenarios-json "$SCENARIOS_JSON" \
  --verify-cmd-template "$VERIFY_CMD_TEMPLATE" \
  --patch-cmd "$PATCH_CMD" \
  --max-iterations "$MAX_ITERATIONS" \
  --max-stalled "$MAX_STALLED" \
  --report-dir "$REPORT_DIR"
