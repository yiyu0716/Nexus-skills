# Verification

To validate the Codex-compatible skill structure, run `quick_validate.py` from the Codex `skill-creator` system skill against each skill folder.

Example on Windows:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" ".\skills\nexus-workbench-designer"
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" ".\skills\nexus-experiment-ux"
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" ".\skills\nexus-agent-protocol"
```

Expected result:

```text
Skill is valid!
Skill is valid!
Skill is valid!
```
