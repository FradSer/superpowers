# Workflow: Manage Team

## Assigning Tasks
- **Direct Assignment**: "Implementer 1, please take Task 1 from the plan."
- **Task List**: Use the shared task list feature if available/enabled.
- **Delegate Mode**: For complex tasks, use "Delegate Mode" to let the teammate work autonomously for a while.

## Monitoring
- **Teammate Mode**:
  - `in-process`: Use Shift+Up/Down to switch views in your terminal.
  - `tmux`: See all teammates in split panes.
- **Interrupting**: If a teammate is going off-track, you can interrupt them (Ctrl+C or dedicated command depending on mode).

## Reviewing Work
1. **Teammate Reports Completion**.
2. **Lead Verification**:
   - "Reviewer, please check the changes made by Implementer 1."
   - Or check it yourself: `git diff`, run tests.
3. **Feedback Loop**:
   - If issues found: "Implementer 1, please fix [issues]."
   - If execution fails: Debug with them or reassign.

## Closing the Team
- When the objective is met: "Great work team. Please shut down."
