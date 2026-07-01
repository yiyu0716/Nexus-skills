# JSON Sentinel Pattern

Use this pattern only when a command will be consumed by an agent, CI job, remote tool, or other automation. It is not required for a purely human-facing dashboard that reads local files.

Use one parseable line in stdout:

```text
NEXUS_JSON {"ok": true, "action": "record", "artifacts": {"report": "reports/run.html"}, "message": "Recorded run."}
```

## Required Fields

- `ok`: boolean
- `action`: command name
- `message`: short result
- `artifacts`: object
- `errors`: list

## Failure Example

```text
NEXUS_JSON {"ok": false, "action": "record", "message": "missing task", "artifacts": {}, "errors": [{"type": "ValueError", "message": "missing task"}]}
```

## Parsing Rule

Agents should parse the last stdout line starting with the sentinel prefix. Treat `ok: false` as failure even if the command printed friendly text.

## Naming

Projects can rename the prefix, but the rule must be explicit in project agent instructions.
