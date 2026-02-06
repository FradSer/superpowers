#!/usr/bin/env bash
# Test: behavior-driven-development skill
# Verifies conversation-memory BDD-guided TDD workflow requirements
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/test-helpers.sh"

echo "=== Test: behavior-driven-development skill ==="
echo ""

# Test 1: skill loading
echo "Test 1: Skill loading..."
output=$(run_claude "What is the behavior-driven-development skill in superpowers? Summarize its purpose briefly." 30)
if assert_contains "$output" "behavior-driven-development\|Behavior-Driven Development" "Skill is recognized"; then :; else exit 1; fi
echo ""

# Test 2: design entrypoint and scenario source
echo "Test 2: Design source conventions..."
output=$(run_claude "In behavior-driven-development, where should design scenarios be read from?" 30)
if assert_contains "$output" "_index\.md\|docs/plans/.+-design/" "Mentions design folder entrypoint"; then :; else exit 1; fi
if assert_contains "$output" "bdd-scenarios\.md\|SCN-" "Mentions scenario source with IDs"; then :; else exit 1; fi
echo ""

# Test 3: RED/GREEN/REFACTOR ordering
echo "Test 3: RED/GREEN/REFACTOR order..."
output=$(run_claude "In behavior-driven-development, respond with the loop order in one line using arrows, like RED->GREEN->REFACTOR." 30)
if assert_contains "$output" "RED[[:space:]]*->[[:space:]]*GREEN[[:space:]]*->[[:space:]]*REFACTOR\|Red[[:space:]]*->[[:space:]]*Green[[:space:]]*->[[:space:]]*Refactor" "Correct phase order"; then :; else exit 1; fi
echo ""

# Test 4: in-memory control and escalation
echo "Test 4: In-memory loop control..."
output=$(run_claude "What in-memory fields should behavior-driven-development track per scenario, and what happens when no progress repeats?" 30)
if assert_contains "$output" "scenario_id\|phase\|iteration\|stalled" "Mentions in-memory state fields"; then :; else exit 1; fi
if assert_contains "$output" "manual\|escalat" "Mentions manual escalation"; then :; else exit 1; fi
echo ""

# Test 5: no process artifact files in default mode
echo "Test 5: No file artifact outputs..."
output=$(run_claude "In default behavior-driven-development flow, should it generate summary.json or events.jsonl files?" 30)
if assert_contains "$output" "do not\|not generate\|conversation\|in-memory" "Explicitly says in-memory/no files"; then :; else exit 1; fi
echo ""

echo "=== All behavior-driven-development skill tests passed ==="
