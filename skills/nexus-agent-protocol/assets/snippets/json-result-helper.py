import json


def nexus_json(payload: dict) -> None:
    """Print one machine-readable result line for coding agents."""
    print("NEXUS_JSON " + json.dumps(payload, ensure_ascii=False, sort_keys=True))


def ok(action: str, message: str, **fields) -> dict:
    return {
        "ok": True,
        "action": action,
        "message": message,
        "artifacts": fields.pop("artifacts", {}),
        "errors": [],
        **fields,
    }


def fail(action: str, message: str, error_type: str = "ValueError", **fields) -> dict:
    return {
        "ok": False,
        "action": action,
        "message": message,
        "artifacts": fields.pop("artifacts", {}),
        "errors": [{"type": error_type, "message": message}],
        **fields,
    }
