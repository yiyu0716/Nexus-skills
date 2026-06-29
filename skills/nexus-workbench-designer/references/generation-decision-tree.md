# Generation Decision Tree

Use this when choosing what to build.

## Repository Type

If Python ML repo:

- create Python scripts or package modules
- prefer static HTML reports
- use JSON/YAML first, SQLite when runs will grow

If Node/TypeScript repo:

- create TypeScript command scripts
- integrate with existing frontend if present
- otherwise static HTML export is acceptable

If notebook-heavy repo:

- avoid forcing package structure
- create scripts plus reports
- read notebook outputs only when necessary

If existing frontend:

- reuse components, routing, and styling
- avoid standalone dashboard unless cheaper

If existing tracker:

- import, summarize, or visualize existing tracker exports
- do not replace it by default

## Clarification Threshold

Ask one concise question when:

- the primary metric source is unknown
- task/run naming cannot be inferred
- the user asks for "dashboard" but there is no clear data source

Proceed without asking when:

- explicit metric/data files are provided
- repo conventions clearly identify logs or results
- the requested change is visual-only
