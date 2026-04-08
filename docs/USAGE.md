# BlueFox Usage Guide — v2.5 beta

---

## Platform-Specific Launch

### Windows

```bat
start.bat
```
Or directly:
```bat
python BlueFox.py
```

### Linux

```bash
chmod +x start.sh
./start.sh
```
Or directly:
```bash
python3 BlueFox.py
```

### macOS (Intel & Apple Silicon)

```bash
chmod +x start.sh
./start.sh
```

The launcher auto-detects your Python version (3.10+ required) and activates any existing virtual environment.

> **Tip for macOS:** If `python3` is not found, install it via [Homebrew](https://brew.sh):
> ```bash
> brew install python@3.12
> ```
> Then retry `./start.sh`.

> **Apple Silicon (M1/M2/M3):** All tools work natively on ARM. No Rosetta or compatibility shim needed.

---

## First Run

At startup:

1. A **4-phase boot animation** plays automatically (matrix rain → boot log → module loading → logo).
2. Press **Enter** when the prompt appears to open the main menu.

The boot sequence is informational — it shows your platform, Python version, API key status, and loaded modules.

---

## Main Categories

| Key | Category | Description |
|---|---|---|
| 1 | NETWORK | Host and infrastructure reconnaissance |
| 2 | OSINT | Identity / email / domain intelligence |
| 3 | WEB | Web surface analysis and protocol checks |
| 4 | REPORTS | Saved results and report generation |
| 5 | DISCOVERY | Targeted recon helper tools |
| 6 | INTEL | IOC / forensics helper tools |

---

## Settings

Open `Settings / API Keys` (`S` from main menu) to:

- Set or update API keys
- Change the result output folder
- Tune worker / thread count
- Pick an interface color theme

API keys are stored locally in `Program/bluefox_config.json`.
They are excluded from version control via `.gitignore`.

---

## Saving Results

Most tools prompt for an export format at the end of a run:

| Format | Use case |
|---|---|
| `json` | Structured data, further processing |
| `csv` | Spreadsheet import |
| `txt` | Human-readable plaintext |
| `non` | Skip saving |

Exports land in the configured results folder (default: `results/`).

---

## macOS-Specific Notes

| Feature | macOS behavior |
|---|---|
| Network info | Uses `ifconfig` (native) |
| Ping | `ping -c 4` (POSIX, same as Linux) |
| Traceroute | `traceroute -m 30 -w 3` (native) |
| Port scan | Pure Python sockets — fully compatible |
| Discord RPC | Works if Discord desktop app is running |
| pystyle colors | Works in Terminal.app and iTerm2 |

> **Terminal recommendations for macOS:** [iTerm2](https://iterm2.com) gives the best color rendering. Set font to a Nerd Font or monospace for correct box-drawing character alignment.

---

## Themes

Change the color theme via Settings → `[6] Interface color theme`:

| Theme | Description |
|---|---|
| `blue` | Blue → Cyan (default) |
| `cyan` | Cyan → Blue |
| `green` | Green → Cyan |
| `red` | Red → Yellow |
| `purple` | Purple → Blue |

---

## Tips

- Start with **low thread counts** (e.g. 50) on unstable or throttled networks.
- For API-based tools (Shodan, VirusTotal, etc.) configure keys in Settings first — they fall back to free methods without keys but give richer results with them.
- Use the **Report Generator** (`REPORTS` category) to combine multiple saved JSON results into a single investigation report.
- Press `Ctrl+C` at any time to interrupt a running tool without crashing the shell.
