# BlueFox Tools v2.4 beta

BlueFox is a modular terminal toolkit for network reconnaissance and OSINT workflows.
It is built for learning, security awareness, and authorized assessments.

## Education Purpose Only

BlueFox is provided strictly for educational and personal research purposes.
Do not use it for illegal, malicious, or unauthorized activity.

By using this project, you are responsible for complying with all applicable laws.
See [DISCLAIMER-en.md](DISCLAIMER-en.md).

## What BlueFox Can Do

- Network recon: ping, traceroute, reverse DNS, port scanning, TCP checks, CIDR analysis, host sweeps, banner grabbing.
- Domain/IP intelligence: WHOIS, ASN, DNS records, blacklist checks, reputation links, resolver comparisons.
- Web recon: headers analysis, SSL/TLS checks, redirect analysis, host header probe, robots/sitemap/security.txt checks.
- OSINT workflows: social lookup, username checks, email and phone OSINT, breach checks, dork generation.
- Intel/forensics helpers: IOC analyzer, file hash audit, password strength estimator, username/email permutations.
- Reporting: save outputs in `json/csv/txt` and generate investigation reports.

## Highlights in v2.4 beta

- New hacker-style interface with stronger visual menu design.
- Animated startup with scrolling code + `Press Enter to Start`.
- Persistent local settings and API key management.
- Configurable interface theme.
- Expanded tool coverage in `Discovery` and `Intel & Forensics`.
- Category and tool architecture refactor for easier maintenance.

## Project Structure

```text
BlueFox.py                 # Main UI and runtime loop
Program/
  legacy_tools.py          # Shared core utilities + legacy implementations
  registry.py              # Category registry used by UI
  network.py               # Network category bindings
  osint.py                 # OSINT category bindings
  web.py                   # Web category bindings
  discovery.py             # Discovery category bindings
  intel.py                 # Intel & Forensics bindings
  reports.py               # Reporting bindings
  tools/                   # One file per tool entrypoint (run())
```

## Installation

Requirements:
- Python 3.10+ recommended
- Terminal environment (Windows/Linux)

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python BlueFox.py
```

## Configuration

BlueFox stores local runtime settings in:
- `Program/bluefox_config.json`

API providers currently supported:
- IPGeolocation
- AbuseIPDB
- Shodan
- VirusTotal
- Hunter.io
- NumVerify

## Documentation

- Usage Guide: [docs/USAGE.md](docs/USAGE.md)
- Architecture: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- Contributing: [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)
- Patch Notes: [docs/PATCH_NOTES.md](docs/PATCH_NOTES.md)

## Contributing

Contributions are welcome.
Please read [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) before opening a PR.

## License

See [LICENSE](LICENSE).

## Donation

Bitcoin adress :
```
bc1q8urqhsnlt0h43ufs5et5ajxjaekngs6dt3udd7
```
Ethereum adress :
```
0x9CC941d1A9173867cd50248f2d886C55E265aD98
```
Solana adress :
```
DAonu76tu3XfyTnGX5MDD1gfLJj9QHYeeNaavu7TB9NQ
```
