---
name: nexus-agent-protocol
description: Use when a user explicitly needs optional command-line automation, JSON output contracts, agent-readable errors, CI hooks, project rules, remote ingestion, or cross-agent workflows for an ML experiment visualization workbench.
---

# Nexus Agent Protocol

## Principle

Give coding agents and automation tools a boring, stable command contract when a human-facing visual workbench also needs automation.

This skill is optional. Do not add a CLI or JSON sentinel merely because a dashboard reads local logs, metrics, or datasets. Use it only when commands will be called by agents, CI, remote tools, scheduled jobs, or other integrations.

## Contract Pattern

When a command contract is needed, commands may print human-readable output, but they should also print one final machine-readable sentinel line:

```text
NEXUS_JSON {"ok": true, "action": "record", "artifacts": {}, "message": "..."}
```

Projects may rename the sentinel, but the pattern should remain: one stable line prefix followed by JSON.

## Required Payload Fields

- `ok`: boolean
- `action`: command or workflow name
- `message`: short human-readable result
- `artifacts`: object of named paths
- `errors`: list, empty on success
- context fields when available: `task`, `project`, `experiment`, `dataset`, `run`

Failure payloads must be structured and parseable. Do not rely on traceback text.

## Optional Agent Behavior

1. Run the command with `--json` or equivalent.
2. Find the last line starting with the sentinel prefix.
3. Parse the JSON after the prefix.
4. Treat `ok: false` as failure even when other text exists.
5. Ask one concise clarification when required context is missing.
6. Return report/dashboard paths and the most important takeaway.

## Inference Rules

- Prefer explicit user-provided task/run names.
- Infer from filenames only when confidence is high, such as `task_experiment.csv`.
- Do not invent task names from vague filenames like `run.csv`.
- Do not overwrite existing runs unless the generated system has a clear update policy.

## References

- Read `references/cli-contract.md` when designing commands.
- Read `references/json-sentinel.md` when implementing sentinel output.
- Read `references/cross-agent-rules.md` when writing `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, or similar project rules.
- Use `assets/snippets/json-result-helper.py` as a small Python reference pattern, not as a required runtime.
