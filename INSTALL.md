# Installation

## Codex

Clone this repository and copy the skills:

```bash
git clone https://github.com/yiyu0716/Nexus-skills.git
cd Nexus-skills
mkdir -p ~/.codex/skills
cp -r skills/nexus-workbench-designer ~/.codex/skills/
cp -r skills/nexus-experiment-ux ~/.codex/skills/
cp -r skills/nexus-agent-protocol ~/.codex/skills/
```

Restart Codex.

## Claude Code

These skills are plain Markdown. You can either:

1. keep the skill folders and tell Claude Code to read the relevant `SKILL.md`, or
2. adapt the key instructions into your repository's `CLAUDE.md`.

Recommended minimal `CLAUDE.md` pointer:

```markdown
When asked to design a local ML experiment workbench, read the Nexus Skills:
- skills/nexus-workbench-designer/SKILL.md
- skills/nexus-experiment-ux/SKILL.md
- skills/nexus-agent-protocol/SKILL.md
Do not copy a fixed Nexus app. Design a project-specific file-first workbench.
```

## Cursor, Trae, Qoder, Zed, Cline, Continue

Use the same Markdown content through the agent's rule system. Common targets:

- `AGENTS.md`
- `.cursorrules`
- project rules
- custom skill/rule folders

The important point is to preserve the three roles:

- `nexus-workbench-designer`: architecture and generation strategy
- `nexus-experiment-ux`: dashboards, charts, reports, visual QA
- `nexus-agent-protocol`: CLI, JSON sentinel, agent-readable errors

## Forward Test

Use `fixtures/python-classification` to test whether an agent can generate a project-specific workbench without copying the original Nexus implementation.
