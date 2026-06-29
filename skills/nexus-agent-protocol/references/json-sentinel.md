# JSON Sentinel Pattern

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
