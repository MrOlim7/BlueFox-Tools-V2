# BlueFox Usage Guide

## Start BlueFox

```bash
python BlueFox.py
```

At startup:
- Wait for animation to complete
- Press Enter when prompted to open the main menu

## Main Categories

- `NETWORK`: host and infrastructure reconnaissance
- `OSINT`: identity/email/domain intelligence workflows
- `WEB`: web surface analysis and protocol checks
- `DISCOVERY`: targeted recon helper tools
- `INTEL`: IOC/forensics helper tools
- `REPORTS`: saved results and report generation

## Settings

Open `Settings / API Keys` from the main menu to:
- Set API keys
- Change result output folder
- Tune worker/thread count
- Pick an interface theme

## Saving Results

Most tools prompt for export format:
- `json`
- `csv`
- `txt`
- or skip export

Exports are written to the configured results folder.

## Tips

- Start with low thread counts on unstable networks.
- Use category-specific tools instead of running everything blindly.
- For API-based tools, configure keys first for best output quality.

