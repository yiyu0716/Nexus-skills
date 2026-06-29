# Implementation Checklist

Use before writing code.

## Design

- Repository inspected.
- Existing training outputs identified.
- Storage choice justified.
- Generated artifact paths chosen.
- Raw files protected.
- Agent protocol decided if agents will call commands.

## Commands

- `record --file` or equivalent.
- `eda --file` or equivalent.
- `compare`.
- `render` or `dashboard`.
- `list` or `inspect`.

## Tests

- Ingest one metric fixture.
- Analyze latest/best metric values.
- Generate at least one report/dashboard.
- Verify machine-readable output if included.
- Verify ambiguous filenames fail or ask instead of guessing.

## Completion

- Generated pages open successfully.
- Visual QA checklist passed.
- No secrets written.
- No raw files modified.
