# BDD Scenarios

### SCN-001 Discover available skills
Given Superpowers is installed in OpenCode
When the agent asks to list available skills
Then the system returns namespaced skills with descriptions
Tags: smoke, cli

### SCN-002 Load a specific skill
Given a valid skill exists
When the agent requests that skill by name
Then the skill content is returned and used for subsequent behavior
Tags: smoke, cli

### SCN-003 Respect priority order
Given the same skill exists in project, personal, and superpowers scopes
When the agent resolves an unqualified skill name
Then project scope wins over personal, and personal wins over superpowers
Tags: full, cli
