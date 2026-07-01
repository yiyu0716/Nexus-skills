# Nexus Skills

Nexus Skills is a collection of agent skills for designing **project-specific local ML experiment workbenches**.

It does not install a fixed Nexus app. Instead, it teaches a coding agent how to build a lightweight, human-facing experiment analysis, comparison, and visualization system inside the user's own repository.

[中文介绍](README.zh-CN.md)

## What This Is

These skills help coding agents design and implement local-first ML experiment systems that can:

- read or ingest existing metric files, logs, and dataset artifacts,
- generate EDA reports and experiment dashboards,
- compare runs and baselines,
- design clear charts with hoverable values,
- optionally expose stable machine-readable command output when automation is explicitly needed.

The generated workbench should belong to the target project. It should match that project's stack, file layout, and UI conventions.

## What This Is Not

Nexus Skills does not:

- copy or install the original Nexus implementation,
- require a fixed Python package or SQLite schema,
- require users to modify training code or adopt an SDK,
- require a CLI or JSON protocol for visual-only local workflows,
- ship private experiment data,
- depend on Codex, Claude Code, Trae, Qoder, Cursor, Zed, or any single agent platform.

## Skills

### `nexus-workbench-designer`

Use when designing or adding a human-facing local ML experiment visualization workbench, EDA/report system, training-result dashboard, or Nexus-like visual workflow inside a repository.

### `nexus-experiment-ux`

Use when designing experiment dashboards, comparison charts, EDA reports, metric cards, hover tooltips, and visual QA for ML experiment analysis interfaces.

### `nexus-agent-protocol`

Optional. Use only when explicitly designing command-line automation, JSON output contracts, structured errors, CI hooks, remote ingestion, or project rules for coding agents.

## Repository Layout

```text
skills/
  nexus-workbench-designer/
  nexus-experiment-ux/
  nexus-agent-protocol/

fixtures/
  python-classification/
```

The fixture is for forward-testing whether an agent can use the skills to generate a small project-specific workbench.

## Installation

### Codex

Copy the skill folders into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -r skills/nexus-workbench-designer ~/.codex/skills/
cp -r skills/nexus-experiment-ux ~/.codex/skills/
```

Optional automation add-on:

```bash
cp -r skills/nexus-agent-protocol ~/.codex/skills/
```

Restart Codex after copying.

### Other Coding Agents

The core instructions are plain Markdown. For Claude Code, Trae, Qoder, Cursor, Zed, Cline, Continue, or other agents, adapt the same skill content into the platform's supported rule or skill format, such as:

- `CLAUDE.md`
- `AGENTS.md`
- `.cursorrules`
- project rule files
- custom skill folders

See [INSTALL.md](INSTALL.md) for more detail.

## Example Prompts

```text
Use Nexus Skills to design a local experiment workbench for this ML repository.
```

```text
Add an experiment dashboard that can ingest metrics CSV files and compare runs.
```

Use this prompt only when automation is needed:

```text
Add an optional agent-friendly CLI/JSON protocol for this experiment dashboard.
```

```text
Improve this experiment dashboard so chart points show exact values on hover.
```

## Design Philosophy

Nexus Skills distributes design capability, not a fixed app.

The default approach is file-first and artifact-first: use existing local CSV, JSON, logs, dataset samples, TensorBoard exports, WandB/MLflow exports, and notebook outputs before asking users to change training code.

Generated systems should be safe by default:

- do not mutate raw data,
- do not delete experiments without confirmation,
- do not write secrets into reports,
- keep CLI and machine-readable protocol optional unless agents, CI, or remote tools need to call commands.

## Status

Initial public skill set. The two visual-first core skills and one optional automation skill are valid Codex-compatible skill folders and include a small forward-test fixture.
