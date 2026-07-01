# Implementation Checklist

Use before writing code.

## Design

- Repository inspected.
- Existing training outputs identified.
- Storage choice justified.
- Generated artifact paths chosen.
- Raw files protected.
- Human-facing views chosen before automation surfaces.
- Agent protocol explicitly marked optional unless agents, CI, or remote tools will call commands.

## Visual Workflow

- Identify metric/log/dataset inputs.
- Normalize enough data for charts and tables.
- Generate dashboard, report, or app route.
- Include comparison and EDA views when matching data exists.
- Add a refresh script or command only if the repo needs repeatable regeneration.

## Tests

- Ingest one metric fixture.
- Analyze latest/best metric values.
- Generate at least one report/dashboard.
- Verify hover values and multi-run line clarity.
- Verify machine-readable output only if optional automation is included.
- Verify ambiguous filenames fail or ask instead of guessing.

## Completion

- Generated pages open successfully.
- Visual QA checklist passed.
- No secrets written.
- No raw files modified.
