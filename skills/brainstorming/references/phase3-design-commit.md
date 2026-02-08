# Phase 3: Design & Commit - Detailed Guidance

## Goal

Create comprehensive design documents (split into multiple files) with BDD specifications, save to folder, and commit to git.

## Actions

### 1. Create Design Document

Draft complete design documents, splitting content into logical files (e.g., `_index.md`, `architecture.md`, `api.md`).

**Required Structure**:

- **MANDATORY**: BDD specifications MUST be in a separate file named `bdd-specs.md`.
- Main content in `_index.md`.
- Other details in supporting files.

#### Overview and Requirements

- Brief summary of what's being built
- Core requirements from Phase 1
- Success criteria and constraints

#### Chosen Approach and Rationale

- Detailed description of chosen approach from Phase 2
- Why this approach fits the requirements
- How it aligns with existing codebase patterns
- Reference specific files and patterns

#### Alternative Approaches Considered

- Brief summary of alternatives from Phase 2
- Key trade-offs that led to rejection
- Don't need full details (already discussed in Phase 2)

#### Detailed Design

- Component breakdown with responsibilities
- Data structures and interfaces
- Integration points with existing code
- Sequence diagrams or flow descriptions (text-based)
- File structure and organization

#### BDD Specifications

**CRITICAL**: Every design MUST include BDD scenarios in a **separate file named `bdd-specs.md`**.

**Why BDD is required**:
- Ensures design is testable before implementation
- Clarifies expected behavior in concrete scenarios
- Provides acceptance criteria for implementation
- Follows BDD principles (behavior-first mindset)

**BDD Format**:

```gherkin
Feature: [Feature name from design]

  Scenario: [Primary happy path]
    Given [initial context/state]
    When [action/event occurs]
    Then [expected outcome]
    And [additional assertions]

  Scenario: [Edge case or error condition]
    Given [context with edge condition]
    When [action triggering edge case]
    Then [expected error handling]
```

**Example**:

```gherkin
Feature: Agent Knowledge Sharing

  Scenario: Agent shares solution after completing task
    Given an agent has completed a task with git commits
    And the agent has analyzed the conversation history
    When the agent calls POST /v1/threads with title, body, and error_log
    Then a new thread is created with status "pending"
    And the thread is visible to other agents immediately
    And the author_id is set to the agent's ID

  Scenario: Agent checks for duplicate before posting
    Given an agent wants to share a solution
    When the agent calls GET /v1/search with error keywords
    And an existing thread matches the error signature
    Then the agent should comment on the existing thread instead
    And mark the comment as is_solution=true if it's a solution

  Scenario: High-reputation agent gets auto-approved content
    Given an agent has reputation >= 100
    When the agent creates a new thread
    Then the review_status is set to "approved" automatically
    And the thread is visible to all agents immediately
```

**BDD Coverage Requirements**:
- At least 3 scenarios per feature
- Cover happy path, edge cases, and error conditions
- Include authentication/authorization scenarios if applicable
- Reference specific API endpoints or methods

#### Error Handling and Edge Cases

- Expected error scenarios and handling strategy
- Edge cases identified and mitigation
- Recovery and rollback strategies

#### Testing Strategy

- Unit test approach and key test cases
- Integration test requirements
- Manual testing checklist if needed
- Reference BDD scenarios from above

#### Open Questions or Risks

- Unresolved technical decisions
- Known risks and mitigation plans
- Dependencies on external systems

### 2. Ground in Reality

Throughout the design:

- Reference specific files: "Similar to the pattern in `src/users/service.ts`"
- Cite existing patterns: "Following the repository pattern used in data access layer"
- Show concrete examples: "The API endpoint will look like: `POST /api/v1/...`"

### 3. Save Design Document

**CRITICAL: You MUST follow this exact folder structure**

**Required Folder Pattern**: `docs/plans/YYYY-MM-DD-<topic>-design/`
- `YYYY-MM-DD` = Current date in ISO format (e.g., `2025-01-15`)
- `<topic>` = Short kebab-case description (e.g., `user-authentication`, `payment-processing`)

**Required Main Document**: `docs/plans/YYYY-MM-DD-<topic>-design/_index.md`
- The main design document MUST be named `_index.md` (with underscore prefix)
- This is NOT optional - always use `_index.md` as the filename
- **MANDATORY**: You MUST split the design into multiple files. Do not dump everything into `_index.md`.

**Complete Examples**:
```
docs/plans/2025-01-15-user-authentication-design/
├── _index.md                                        CORRECT (Main doc)
├── bdd-specs.md                                     CORRECT (MANDATORY BDD doc)
├── architecture.md                                  CORRECT (Supporting doc)
└── api-spec.md                                      CORRECT (Supporting doc)

docs/plans/2025-01-15-payment-processing-design/
└── _index.md                                        CORRECT

docs/plans/2025-01-15-api-rate-limiting-design.md   WRONG (not a folder)
docs/plans/2025-01-15-design/_index.md              WRONG (missing topic)
docs/plans/user-authentication/_index.md            WRONG (missing date)
docs/plans/2025-01-15-design/index.md               WRONG (must be _index.md)
```

**Why This Structure**:
- Folder allows adding supporting files later (diagrams, examples, code samples)
- `_index.md` is the standard main document naming convention
- Date prefix enables chronological sorting
- Topic in folder name provides context

**Step-by-Step Implementation**:

1. **Check if base directory exists**:
   ```bash
   # If docs/plans/ doesn't exist, create it first
   mkdir -p docs/plans
   ```

2. **Create design folder**:
   ```bash
   mkdir -p docs/plans/YYYY-MM-DD-<topic>-design
   ```

3. **Write main design document**:
   - Use the Write tool
   - File path MUST be: `docs/plans/YYYY-MM-DD-<topic>-design/_index.md`
   - Include complete design content with all sections including BDD specs

### 4. Commit Design to Git

**CRITICAL: You MUST commit the entire folder, not just _index.md**

**Required Git Commands**:
```bash
# Add the entire design folder (note the trailing slash)
git add docs/plans/YYYY-MM-DD-<topic>-design/

# Commit with proper message format
git commit -m "docs: add design for <topic>

Includes BDD specifications for test-first development.

Co-Authored-By: <Model Name> <noreply@anthropic.com>"
```

**Complete Example**:
```bash
git add docs/plans/2025-01-15-user-authentication-design/
git commit -m "docs: add design for user authentication

Includes BDD specifications for test-first development.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

**Common Mistakes to Avoid**:
```bash
# WRONG - only adds _index.md file
git add docs/plans/2025-01-15-user-authentication-design/_index.md

# WRONG - missing trailing slash, might not include folder
git add docs/plans/2025-01-15-user-authentication-design

# CORRECT - adds entire folder with trailing slash
git add docs/plans/2025-01-15-user-authentication-design/
```

**Commit Message Requirements** (all mandatory):
- Prefix: `docs:` (lowercase)
- Subject: Short description under 50 characters, lowercase
- Body: Mention "BDD specifications"
- Footer: `Co-Authored-By: <Model Name> <noreply@anthropic.com>`
- Format: Use heredoc for multi-line messages if needed

**Heredoc Example** (recommended for reliability):
```bash
git commit -m "$(cat <<'EOF'
docs: add design for user authentication

Includes BDD specifications for test-first development.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
EOF
)"
```

### 5. Inform User

Tell the user:
- Design folder and main document location
- Git commit completed
- Ready to proceed with implementation following BDD scenarios
- Note that supporting files can be added to the folder later if needed

## Output

- Design folder created at `docs/plans/YYYY-MM-DD-<topic>-design/`
- Main design document `_index.md`
- **MANDATORY**: Separate `bdd-specs.md` file with BDD scenarios
- Other supporting files (`architecture.md`, etc.)
- Design folder committed to git with proper message
- User informed and ready for implementation

## Key Principle

**Complete the brainstorming phase before jumping into implementation.** The design document with BDD specs is a checkpoint - commit it before proceeding to ensure you can refer back to the original plan and have clear acceptance criteria.
