# BlueFox Architecture — v2.5 beta

---

## Overview

BlueFox uses a menu-driven terminal UI and a fully modular backend.
The startup sequence, UI loop, and tool dispatch are separated from tool logic.

---

## Runtime Layers

```
┌─────────────────────────────────────────────────────────┐
│  BlueFox.py                                             │
│  ─ Boot animation (4 phases)                            │
│  ─ Main menu / category menu loop                       │
│  ─ Tool dispatch + error handling                       │
│  ─ Settings panel                                       │
└──────────────────────┬──────────────────────────────────┘
                       │ imports
┌──────────────────────▼──────────────────────────────────┐
│  Program/registry.py                                    │
│  ─ Central category map (name, description, tool list)  │
└──────────────────────┬──────────────────────────────────┘
                       │ imports
┌──────────────────────▼──────────────────────────────────┐
│  Program/<category>.py                                  │
│  (network / osint / web / discovery / intel / reports)  │
│  ─ Imports tool entrypoints from Program/tools/         │
│  ─ Builds TOOLS list for the registry                   │
└──────────────────────┬──────────────────────────────────┘
                       │ imports
┌──────────────────────▼──────────────────────────────────┐
│  Program/tools/*.py                                     │
│  ─ One file per tool                                    │
│  ─ Each exposes run()                                   │
└──────────────────────┬──────────────────────────────────┘
                       │ calls
┌──────────────────────▼──────────────────────────────────┐
│  Program/core.py                                │
│  ─ Shared helpers (color, input, print, save, config)   │
│  ─ Legacy full-function implementations                 │
│  ─ Discord RPC wrapper                                  │
└─────────────────────────────────────────────────────────┘
```

---

## Boot Sequence (v2.5)

```
Phase 1  Matrix Rain       16 frames × 0.04s   ≈ 0.6 s
Phase 2  Boot Log Stream   27 entries × 0.068s ≈ 1.9 s
Phase 3  Module Panel      10 steps × 0.14s    ≈ 1.4 s
Phase 4  Logo + Enter      9 blinks × 0.22s    ≈ 2.0 s
─────────────────────────────────────────────────────────
Total before Enter prompt                       ≈ 6 s
```

---

## Configuration

Local config file: `Program/bluefox_config.json`

Contains:
- `version` — current app version string
- `ui_theme` — color theme name
- `results_folder` — export output path
- `max_workers` — thread pool ceiling
- `*_api_key` — optional API credentials (6 providers)

Environment variables override the JSON file at startup (see `load_local_config()`).

---

## Platform Compatibility

| Layer | Windows | Linux | macOS |
|---|---|---|---|
| Terminal colors (pystyle) | ✓ | ✓ | ✓ |
| Box-drawing characters | ✓ | ✓ | ✓ |
| Ping / traceroute subprocess | ✓ (ipconfig / tracert) | ✓ | ✓ |
| Network info (ifconfig / ipconfig) | ipconfig | ifconfig / ip addr | ifconfig |
| Port scanning (sockets) | ✓ | ✓ | ✓ |
| Discord RPC (pypresence) | ✓ | ✓ | ✓ |

---

## Design Goals

- Keep tool logic isolated — one file per tool, one `run()` per file.
- Minimize regressions when adding tools.
- Support fast iteration toward future major versions.
- Zero platform-specific code in individual tools — delegate to helpers.
