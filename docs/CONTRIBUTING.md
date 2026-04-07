# Contributing to BlueFox

Thanks for your interest in improving BlueFox.

## Ground Rules

- This project is **education purpose only**.
- Keep all contributions legal, ethical, and focused on defensive/security-learning workflows.
- Avoid adding anything that explicitly facilitates abuse.

## How to Contribute

1. Fork the repository.
2. Create a feature branch:
   - `feature/new-tool-name`
   - `fix/social-lookup-timeout`
3. Make focused changes.
4. Run local checks before opening a PR.
5. Open a pull request with a clear description.

## Development Notes

- Main UI entrypoint: `BlueFox.py`
- Category bindings: `Program/*.py`
- Tool entrypoints: `Program/tools/*.py`
- Shared core helpers: `Program/legacy_tools.py`

When adding a new tool:

1. Add a file in `Program/tools/<tool_name>.py`
2. Implement `run()` in that file
3. Register it in the correct category module (`Program/network.py`, `Program/osint.py`, etc.)
4. Update docs if behavior is user-facing

## Coding Style

- Keep code readable and simple.
- Prefer explicit error handling over silent failures.
- Keep timeouts on all external network requests.
- Reuse shared helper functions from `legacy_tools.py` when possible.

## Security and Safety

- Do not commit secrets or private API keys.
- Never commit `Program/bluefox_config.json` with real keys.
- Do not commit Python cache folders (`__pycache__`).

Recommended `.gitignore` entries:

```gitignore
__pycache__/
*.py[cod]
Program/bluefox_config.json
```

## Pull Request Checklist

- [ ] Code runs locally
- [ ] No obvious regressions in main menu / category navigation
- [ ] Tool is wired in the correct category
- [ ] Documentation updated if needed
- [ ] No secrets or local cache files included

