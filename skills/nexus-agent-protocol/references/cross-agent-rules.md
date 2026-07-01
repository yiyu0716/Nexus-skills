# Cross-Agent Rules

Write project-level instructions that any coding agent can follow when optional automation exists.

## Minimum Rule Content

- Where generated workbench files live.
- Which dashboard/report files humans should open.
- Which raw/log/metric paths must not be modified.
- Which command records metrics, runs EDA, compares runs, or regenerates pages if such commands exist.
- How to parse the sentinel JSON line if such a line exists.
- What paths must not be modified.
- What to do when context is missing.

## Portable Instruction Example

```markdown
When asked to record an experiment, run the project experiment CLI with `--json`.
Parse the final line starting with `NEXUS_JSON `.
If `ok` is false, ask one concise clarification or report the structured error.
Never modify files under raw data directories.
```

If the project is visual-only, rules may instead say:

```markdown
When asked to inspect experiments, read the existing metrics/log files and regenerate the local dashboard/report.
Open or return the generated human-facing report path.
Do not introduce a CLI or JSON protocol unless automation is requested.
Never modify raw metric, log, or dataset files.
```

## Platform Notes

- Codex: use `SKILL.md` or `AGENTS.md`.
- ClaudeCode: use `CLAUDE.md`.
- Cursor/Zed/Trae/Qoder/Cline/Continue: use the project's supported rules file.

Keep the core instructions platform-neutral.
