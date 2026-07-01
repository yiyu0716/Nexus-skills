# Architecture Patterns

Use these patterns to design a custom local ML experiment workbench in the target repository.

## Standard Flow

```text
local artifacts -> read/ingest -> normalize -> analyze -> visualize -> human-readable dashboard/report
```

## Recommended Modules

- storage layer: JSON/YAML, SQLite, or existing DB
- ingest layer: CSV/JSON/log parsers
- analysis layer: summaries, best/latest values, metric direction
- rendering layer: static HTML/SVG or existing frontend for human inspection
- optional refresh layer: small scripts or commands to regenerate reports
- optional agent protocol layer: stable machine-readable output only when automation is required

## Layout Options

Small Python project:

```text
experiment_workbench/
experiments/
reports/
scripts/render_experiments.py   # optional refresh script
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
data/experiments/
scripts/render-experiments.*    # optional automation hook
```

## Storage Choices

- JSON/YAML: choose for small projects, simplest setup, fewer than dozens of runs.
- SQLite: choose for durable local indexing, comparisons, many runs, or multi-task projects.
- Existing DB: choose only when the project already depends on one.

Do not introduce a service or server unless the user asks for one.

Do not introduce a CLI contract unless the user wants automation, CI, cross-agent workflows, or remote ingestion. For local visual inspection, a refresh script or app route is usually enough.

## File-First Default

Prefer ingesting existing files over requiring training-code changes:

- metrics CSV
- JSON training logs
- TensorBoard scalar exports
- WandB/MLflow exports
- notebook result files
- dataset samples or summaries
