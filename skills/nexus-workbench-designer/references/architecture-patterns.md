# Architecture Patterns

Use these patterns to design a custom local ML experiment workbench in the target repository.

## Standard Flow

```text
local artifacts -> ingest -> normalize -> analyze -> visualize -> report -> agent-readable result
```

## Recommended Modules

- command layer: CLI or scripts the user and agents can call
- storage layer: JSON/YAML, SQLite, or existing DB
- ingest layer: CSV/JSON/log parsers
- analysis layer: summaries, best/latest values, metric direction
- rendering layer: static HTML/SVG or existing frontend
- agent protocol layer: stable machine-readable output

## Layout Options

Small Python project:

```text
tools/experiment_cli.py
experiment_workbench/
experiments/
reports/
```

Notebook-heavy project:

```text
scripts/record_experiment.py
experiments/
reports/
notebooks/
```

Existing web app:

```text
src/experiment-workbench/
scripts/experiment-cli.*
data/experiments/
```

## Storage Choices

- JSON/YAML: choose for small projects, simplest setup, fewer than dozens of runs.
- SQLite: choose for durable local indexing, comparisons, many runs, or multi-task projects.
- Existing DB: choose only when the project already depends on one.

Do not introduce a service or server unless the user asks for one.

## File-First Default

Prefer ingesting existing files over requiring training-code changes:

- metrics CSV
- JSON training logs
- TensorBoard scalar exports
- WandB/MLflow exports
- notebook result files
- dataset samples or summaries
