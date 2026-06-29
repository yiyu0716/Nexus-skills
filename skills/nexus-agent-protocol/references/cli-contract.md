# CLI Contract

Design commands so both humans and coding agents can call them.

## Common Commands

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
