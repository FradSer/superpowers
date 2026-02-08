# Workflow: Initiate Team

## Prerequisites
- `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` is set in your environment.

## Steps

1. **Identify the Need**:
   - Complex Plan? -> Need an **Architect**.
   - Parallelizable Tasks? -> Need multiple **Implementers**.
   - Strict Quality Control? -> Need a **Reviewer**.

2. **Spawn the Team**:
   - Use natural language to describe the team you want.
   
   *Example Command*:
   ```
   Create an agent team with:
   - 1 Architect to design the solution
   - 2 Implementers to build the components
   - 1 Reviewer to check the code
   ```

3. **Confirm Composition**:
   - Claude will propose a team structure. Review it and confirm.

4. **Set Context**:
   - Once the team is active, share the relevant files or context with them.
   - *Tip*: "Architect, please read `implementation_plan.md` and `SKILL.md`."
