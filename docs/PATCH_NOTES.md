# BlueFox Patch Notes

---

## v2.5 beta

### Boot Animation — Complete Rewrite

The startup sequence is now a **4-phase cinematic boot**:

1. **Matrix Rain** — screen fills with random ASCII characters scrolling at speed, setting the hacker atmosphere.
2. **Boot Log Stream** — a bordered box scrolls through detailed system initialization messages: platform detection, Python version, thread pool capacity, API key status, and module imports. A progress bar tracks overall boot progress.
3. **Module Loading Panel** — each internal module (core, network, OSINT, web, intel, discovery, reports, RPC) is displayed with an animated fill bar transitioning from PENDING → LOADING → LOADED.
4. **Logo Reveal + Press Enter** — the BlueFox ASCII banner appears with system info (OS, architecture, Python version), followed by a blinking prompt border.

### macOS Support

- All tools are now fully tested on macOS (Intel and Apple Silicon).
- `my_ip_info()` uses the native `ifconfig` path on Darwin instead of the Linux fallback chain.
- `start.sh` auto-detects the platform and selects the correct Python interpreter (3.10+).
- Documentation updated with macOS-specific installation and troubleshooting steps.
- `traceroute` and `ping` already used POSIX flags compatible with macOS — no changes required.

### Linux / macOS Launcher — `start.sh`

New `start.sh` script:
- Scans for Python 3.10, 3.11, 3.12 in PATH.
- Activates `.venv` or `venv` if found.
- Auto-installs dependencies if `requests` is missing.
- Cross-platform: works on Debian, Ubuntu, Arch, Fedora, macOS.

### UI Improvements

- Improved category cards now show tool count and description inline.
- Settings panel shows API key status with `✓ SET` / `✗ EMPTY` indicators.
- Transition animation replaced with a smoother arrow-flow style.
- System info (OS, arch, Python version) displayed in the main banner on every screen.
- `animated_banner()` refreshes timestamp on each menu visit.

### Minor Fixes

- Boot sequence timing tuned for smoother feel across fast and slow terminals.
- Box drawing characters consistent across all panels (80-char terminal width assumed).
- `center_line()` now accepts explicit width argument for flexible box layouts.
- Various string padding fixes to prevent text overflow in bordered panels.

---

## v2.4 beta

### UI and UX
- Reworked terminal interface with a stronger hacker-style visual identity.
- New startup animation with scrolling code and `Press Enter to Start`.
- Improved menu and submenu presentation.
- Theme selection from settings.

### Architecture
- Refactored category structure and runtime wiring.
- Tool entrypoints split into `Program/tools/` (one file per option).
- Added dedicated category modules (`network`, `osint`, `web`, `discovery`, `intel`, `reports`).

### New Categories
- `Discovery`
- `Intel & Forensics`

### New Tools Added
- IOC Analyzer
- File Hash Audit
- Password Strength Estimator
- Username Variations
- Email Permutations
- IP/Domain Reputation Links
- Netblock Host Counter
- TLS Version Probe
- Host Header Probe
- Security.txt Audit
- Redirect Chain Analyzer
- DNS Resolver Compare
- Plus additional recon helpers in Discovery category

### Fixes and Hardening
- Improved social lookup robustness for special-character usernames.
- Better handling of blocked/limited HTTP statuses in lookup workflows.
- Safer result filename sanitization during export.
- Cleaner RPC shutdown to reduce Windows transport warnings.

---

## v2.3 beta (summary)

- Added persistent local API-key configuration.
- Added web recon capabilities and additional network utilities.
- Began modularization and category cleanup.
