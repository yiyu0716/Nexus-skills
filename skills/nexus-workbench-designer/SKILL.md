---
name: nexus-workbench-designer
description: Use when a user wants to add, design, or implement a human-facing local ML experiment dashboard, experiment visualization workbench, EDA/report system, training-result comparison UI, or Nexus-like visual workflow inside their own repository.
---

# Nexus Workbench Designer

## Principle

Design a project-specific experiment visualization workbench for humans first. Do not copy or install the original Nexus app as the default solution.

The output should belong to the target repository: its stack, paths, storage, and UI conventions. Command-line interfaces are optional integration surfaces, not the default product.

## Workflow

1. Inspect the repository before proposing architecture.
2. Identify project type: Python ML, Node/TS, notebook-heavy, existing frontend, minimal scripts, or existing tracker.
3. Ask at most one clarification if the primary experiment artifacts are unclear.
4. Design a file-first visual workbench around existing local artifacts: metrics CSV, JSON logs, TensorBoard/WandB/MLflow exports, datasets, notebook outputs.
5. Choose a storage pattern proportional to the repo: JSON/YAML for small projects, SQLite for durable local tracking, existing DB only when already present.
6. Design the human-facing dashboard/report flow first: what files are read, what views are generated, and how users inspect experiments.
7. Add scripts, commands, or a CLI only when useful for the repository's existing workflow or explicitly requested.
8. Apply `nexus-agent-protocol` only when commands will be called by coding agents, CI, remote automation, or other tools.
9. Apply `nexus-experiment-ux` when designing dashboards, charts, reports, or EDA pages.
10. Write a concise spec and implementation plan before coding.

## Defaults

- Python ML repo: static HTML reports or a lightweight local dashboard around existing files unless an app already exists.
- Node/TS repo: app-native or static dashboard; add TypeScript command scripts only when automation is needed.
- Notebook-heavy repo: `reports/`, `experiments/`, or notebook-adjacent generated pages; avoid forcing package structure.
- Minimal repo: JSON/YAML storage plus static HTML before SQLite.
- Existing frontend repo: integrate the dashboard into the existing app when cheaper than standalone pages.
- Existing tracker: import/export or report around existing artifacts rather than replacing it.

## Hard Rules

- Do not vendor this Nexus repo or require its Python package.
- Do not require users to modify training code or adopt an SDK in MVP.
- Do not make CLI or JSON protocol mandatory when local logs/files are enough.
- Never modify raw input files in place.
- Put generated artifacts in explicit generated directories.
- Treat deletion as out of scope unless soft-delete and confirmation are designed.
- Fail or ask one clarification when inference is low-confidence.

## References

- Read `references/architecture-patterns.md` when choosing layout and storage.
- Read `references/data-model-patterns.md` when designing entities and artifact paths.
- Read `references/generation-decision-tree.md` when repo type is ambiguous.
- Read `references/implementation-checklist.md` before implementation.
