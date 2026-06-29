---
name: nexus-workbench-designer
description: Use when a user wants to add, design, or implement a local ML experiment workbench, experiment tracker, training-result dashboard, EDA/report system, or Nexus-like workflow inside their own repository.
---

# Nexus Workbench Designer

## Principle

Design a project-specific experiment workbench. Do not copy or install the original Nexus app as the default solution.

The output should belong to the target repository: its stack, paths, commands, storage, and UI conventions.

## Workflow

1. Inspect the repository before proposing architecture.
2. Identify project type: Python ML, Node/TS, notebook-heavy, existing frontend, minimal scripts, or existing tracker.
3. Ask at most one clarification if the primary experiment artifacts are unclear.
4. Design a file-first workbench around existing local artifacts: metrics CSV, JSON logs, TensorBoard/WandB/MLflow exports, datasets, notebook outputs.
5. Choose a storage pattern proportional to the repo: JSON/YAML for small projects, SQLite for durable local tracking, existing DB only when already present.
6. Design commands for `record --file`, `eda --file`, `compare`, `render/dashboard`, and `list/inspect`.
7. Apply `nexus-agent-protocol` when commands will be called by coding agents.
8. Apply `nexus-experiment-ux` when designing dashboards, charts, reports, or EDA pages.
9. Write a concise spec and implementation plan before coding.

## Defaults

- Python ML repo: Python CLI plus static HTML reports unless an app already exists.
- Node/TS repo: TypeScript command layer plus app-native or static dashboard.
- Notebook-heavy repo: scripts plus `reports/` or `experiments/`; avoid forcing package structure.
- Minimal repo: JSON/YAML storage plus static HTML before SQLite.
- Existing frontend repo: integrate the dashboard into the existing app when cheaper than standalone pages.
- Existing tracker: import/export or report around existing artifacts rather than replacing it.

## Hard Rules

- Do not vendor this Nexus repo or require its Python package.
- Do not require users to modify training code or adopt an SDK in MVP.
- Never modify raw input files in place.
- Put generated artifacts in explicit generated directories.
- Treat deletion as out of scope unless soft-delete and confirmation are designed.
- Fail or ask one clarification when inference is low-confidence.

## References

- Read `references/architecture-patterns.md` when choosing layout and storage.
- Read `references/data-model-patterns.md` when designing entities and artifact paths.
- Read `references/generation-decision-tree.md` when repo type is ambiguous.
- Read `references/implementation-checklist.md` before implementation.
