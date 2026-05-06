# Contributing to BlueFox — v2.5 beta

Thanks for your interest in improving BlueFox.

---

## Ground Rules

- This project is **education and personal research only**.
- Keep all contributions legal, ethical, and focused on defensive / security-learning workflows.
- Avoid adding anything that explicitly facilitates abuse or unauthorized access.

---

## How to Contribute

1. Fork the repository.
2. Create a feature branch:
   - `feature/new-tool-name`
   - `fix/social-lookup-timeout`
   - `docs/update-macos-guide`
3. Make focused changes.
4. Test locally on your platform (Windows / Linux / macOS).
5. Open a pull request with a clear description.

---

## Development Setup

**Windows:**
```bat
pip install -r requirements.txt
python BlueFox.py
```

**Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 BlueFox.py
```

---

## Adding a New Tool

1. Create `Program/tools/<tool_name>.py`
2. Implement `run()` in that file:
   ```python
   from Program import legacy_tools as core

   def run():
       target = core.get_input("Target")
       if not target:
           return
       core.print_header(f"MY TOOL - {target}")
       # ... logic ...
       core.ask_save(f"my_tool_{target}", data)
   ```
3. Register it in the correct category module (`Program/network.py`, `Program/osint.py`, etc.):
   ```python
   from .tools import my_tool
   TOOLS = [
       ...
       ("My Tool", my_tool.run),
   ]
   ```
4. Update `docs/PATCH_NOTES.md` under the next version section.

---

## Coding Style

- Keep code readable and simple.
- Prefer explicit error handling (`try/except`) over silent failures.
- Always set timeouts on external network requests.
- Reuse shared helpers from `legacy_tools.py` (`print_result`, `print_success`, `ask_save`, etc.).
- Use `core.get_input()` for all user prompts — not raw `input()`.

---

## Platform Compatibility

All tools must work on **Windows, Linux, and macOS**.

- Use `platform.system()` to branch on OS-specific behavior.
- Use Python's `socket`, `subprocess`, and `concurrent.futures` — avoid OS-specific shell commands in tool logic.
- If a subprocess command differs by OS, check `platform.system() in ("Windows", "Darwin", ...)`.

---

## Security and Safety

- Do not commit secrets or private API keys.
- Never commit `Program/bluefox_config.json` with real keys (it is already in `.gitignore`).
- Do not commit Python cache folders (`__pycache__`).
- Do not commit the `results/` folder.

---

## Pull Request Checklist

- [ ] Code runs locally (tested on at least one platform)
- [ ] No obvious regressions in main menu / category navigation
- [ ] Tool wired in the correct category module
- [ ] `run()` function present and callable
- [ ] `docs/PATCH_NOTES.md` updated with the change
- [ ] No secrets or local cache files included
- [ ] Timeouts on all network requests
