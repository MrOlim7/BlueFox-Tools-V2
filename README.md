# BlueFox Tools v2.5 beta

BlueFox is a modular terminal toolkit for network reconnaissance and OSINT workflows.
It is built for learning, security awareness, and authorized assessments.

## Education Purpose Only

BlueFox is provided strictly for educational and personal research purposes.
Do not use it for illegal, malicious, or unauthorized activity.

By using this project you are responsible for complying with all applicable laws.
See [DISCLAIMER-en.md](DISCLAIMER-en.md).

---

## What BlueFox Can Do

- **Network recon** — ping, traceroute, reverse DNS, port scanning, TCP checks, CIDR analysis, host sweeps, banner grabbing.
- **Domain / IP intelligence** — WHOIS, ASN, DNS records, blacklist checks, reputation links, resolver comparisons.
- **Web recon** — headers analysis, SSL / TLS checks, redirect analysis, host header probe, robots / sitemap / security.txt checks.
- **OSINT workflows** — social lookup, username checks, email and phone OSINT, breach checks, dork generation.
- **Intel / forensics helpers** — IOC analyzer, file hash audit, password strength estimator, username / email permutations.
- **Reporting** — save outputs in `json / csv / txt` and generate investigation reports.

---

## Highlights in v2.5 beta

- **Redesigned boot animation** — 4-phase startup: matrix rain → detailed boot log stream → module loading panel → logo reveal with blinking prompt.
- **macOS full support** — tested on macOS (Intel + Apple Silicon); native `ifconfig` path for network info; `start.sh` auto-detects platform and Python version.
- **Linux launch script** — `start.sh` works on Linux and macOS, detects venv automatically.
- **Improved transition animations** — smoother arrow-flow transitions between menus.
- **Enhanced category cards** — tool count and description displayed inline.
- **Cleaner settings panel** — API key status with ✓/✗ indicators.
- **System info in banner** — OS, architecture, and Python version shown on every main screen.

---

## Platform Support

| Platform | Status | Notes |
|---|---|---|
| Windows 10 / 11 | ✓ Supported | Use `start.bat` |
| Linux (Debian / Ubuntu / Arch) | ✓ Supported | Use `start.sh` |
| macOS (Intel) | ✓ Supported | Use `start.sh` |
| macOS (Apple Silicon M1/M2/M3/M4) | ✓ Supported | Use `start.sh` |

See [docs/USAGE.md](docs/USAGE.md) for platform-specific instructions.

---

## Project Structure

```
BlueFox.py                 ← Main UI and runtime loop
start.bat                  ← Windows launcher
start.sh                   ← Linux / macOS launcher
Program/
  core.py          ← Shared core utilities
  registry.py              ← Category registry used by UI
  network.py               ← Network category bindings
  osint.py                 ← OSINT category bindings
  web.py                   ← Web category bindings
  discovery.py             ← Discovery category bindings
  intel.py                 ← Intel & Forensics bindings
  reports.py               ← Reporting bindings
  tools/                   ← One file per tool entrypoint (run())
docs/
  USAGE.md
  ARCHITECTURE.md
  CONTRIBUTING.md
  PATCH_NOTES.md
```

---

## Installation

**Requirements:**
- Python 3.10 or higher
- Terminal / shell environment

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**Windows:**
```bat
start.bat
```

**Linux / macOS:**
```bash
chmod +x start.sh
./start.sh
```

**Or run directly:**
```bash
python BlueFox.py
# or
python3 BlueFox.py
```

---

## Configuration

BlueFox stores local runtime settings in `Program/bluefox_config.json`.

API providers currently supported:

| Provider | Free Tier | Used by |
|---|---|---|
| IPGeolocation | Yes (1 000/day) | IP Lookup enrichment |
| AbuseIPDB | Yes (1 000/day) | Blacklist Check |
| Shodan | Yes (query limited) | Shodan Search |
| VirusTotal | Yes (4 req/min) | VirusTotal Check |
| Hunter.io | Yes (25/month) | Email OSINT |
| NumVerify | Yes (100/month) | Phone OSINT |

All API keys are optional. Tools degrade gracefully to free fallbacks when keys are absent.

---

## Documentation

- [Usage Guide](docs/USAGE.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Contributing](docs/CONTRIBUTING.md)
- [Patch Notes](docs/PATCH_NOTES.md)

---

## License

See [LICENSE](LICENSE) — MIT

---

## Donation

Bitcoin:
```
bc1q8urqhsnlt0h43ufs5et5ajxjaekngs6dt3udd7
```
Ethereum:
```
0x9CC941d1A9173867cd50248f2d886C55E265aD98
```
Solana:
```
DAonu76tu3XfyTnGX5MDD1gfLJj9QHYeeNaavu7TB9NQ
```
