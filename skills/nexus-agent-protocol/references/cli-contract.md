# CLI Contract

Design commands only when the workbench needs automation beyond the human-facing dashboard/report.

## When To Add Commands

Add a command layer when at least one is true:

- CI or scheduled jobs need to regenerate reports.
- Coding agents need to record, compare, or inspect runs without opening the UI.
- Remote machines need to push metrics or trigger rendering.
- The repository already has command-based experiment workflows.

For local human inspection of existing files, prefer a simple refresh script, app route, or static renderer.

## Common Optional Commands

- `init`: create required generated directories and config
- `record --file <path>`: ingest a metric or run artifact
- `eda --file <path>`: analyze a dataset artifact
- `compare`: compare runs
- `render` or `dashboard`: regenerate visual pages
- `list` or `inspect`: show known tasks/runs

Names may vary, but the behavior should be discoverable and tested.

## Output

Commands may print human text. If an agent will call the command, also print a sentinel JSON line as the final machine-readable result.

## Errors

Do not rely on tracebacks. Convert expected problems into structured failures:

- missing file
- unsupported file type
- missing task/run context
- no metrics found
- ambiguous inference
