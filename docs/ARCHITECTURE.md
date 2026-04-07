# BlueFox Architecture

## Overview

BlueFox uses a menu-driven terminal UI and a modular backend.

## Runtime Layers

1. `BlueFox.py`
   - UI loop
   - startup animation
   - category and tool execution flow

2. `Program/registry.py`
   - central category map
   - binds category names/descriptions to tool lists

3. `Program/<category>.py`
   - category-level tool registration
   - imports tool entrypoints from `Program/tools/`

4. `Program/tools/*.py`
   - one file per tool entrypoint
   - each tool exposes `run()`

5. `Program/legacy_tools.py`
   - shared utility functions
   - common printing/config helpers
   - backward compatibility for legacy implementations

## Configuration

Local config file:
- `Program/bluefox_config.json`

Contains:
- UI theme
- API keys
- output folder
- worker/thread limits

## Design Goals

- Keep tool logic isolated and easy to extend
- Minimize regressions when adding new tools
- Make debugging straightforward through clear module boundaries
- Support fast iteration toward future major versions

