# BlueFox Patch Notes

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

## v2.3 beta (summary)

- Added persistent local API-key configuration.
- Added web recon capabilities and additional network utilities.
- Began modularization and category cleanup.

