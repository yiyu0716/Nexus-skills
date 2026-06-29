# Cross-Agent Rules

Write project-level instructions that any coding agent can follow.

## Minimum Rule Content

- Where generated workbench files live.
- Which command records metrics.
- Which command runs EDA.
- Which command compares runs.
- How to parse the sentinel JSON line.
- What paths must not be modified.
- What to do when context is missing.

## Portable Instruction Example

```markdown
When asked to record an experiment, run the project experiment CLI with `--json`.
Parse the final line starting with `NEXUS_JSON `.
If `ok` is false, ask one concise clarification or report the structured error.
Never modify files under raw data directories.
```

## Platform Notes

- Codex: use `SKILL.md` or `AGENTS.md`.
- ClaudeCode: use `CLAUDE.md`.
- Cursor/Zed/Trae/Qoder/Cline/Continue: use the project's supported rules file.

Keep the core instructions platform-neutral.
