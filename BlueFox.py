import os
import sys
import time
import random
import platform

from Program import legacy_tools as core
from Program import registry, settings

APP_VERSION = core.CONFIG.get("version", "2.5 beta")

BANNER = r"""
 ▄▄▄▄    ██▓     █    ██ ▓█████   █████▒▒█████  ▒██   ██▒
▓█████▄ ▓██▒     ██  ▓██▒▓█   ▀ ▓██   ▒▒██▒  ██▒▒▒ █ █ ▒░
▒██▒ ▄██▒██░    ▓██  ▒██░▒███   ▒████ ░▒██░  ██▒░░  █   ░
▒██░█▀  ▒██░    ▓▓█  ░██░▒▓█  ▄ ░▓█▒  ░▒██   ██░ ░ █ █ ▒ 
░▓█  ▀█▓░██████▒▒▒█████▓ ░▒████▒░▒█░   ░ ████▓▒░▒██▒ ▒██▒
░▒▓███▀▒░ ▒░▓  ░░▒▓▒ ▒ ▒ ░░ ▒░ ░ ▒ ░   ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░
▒░▒   ░ ░ ░ ▒  ░░░▒░ ░ ░  ░ ░  ░ ░       ░ ▒ ▒░ ░░   ░▒ ░
 ░    ░   ░ ░    ░░░ ░ ░    ░    ░ ░   ░ ░ ░ ▒   ░    ░  
 ░          ░  ░   ░        ░  ░           ░ ░   ░    ░  
      ░                                                   
"""

MATRIX_CHARS = (
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789!@#$%^&*<>[]{}|/\\"
)

# ─── box sizing ──────────────────────────────────────────────────────────────
BOX_W = 78   # chars between ╔ and ╗  (total line = 80)


def wipe():
    core.clear()


def center_line(text, width=76):
    return text.center(width)


# ─── BOOT SEQUENCE ───────────────────────────────────────────────────────────
def boot_sequence():
    _sys    = platform.system()
    _mach   = platform.machine()
    _py     = platform.python_version()
    _theme  = core.CONFIG.get("ui_theme", "blue")
    _work   = core.CONFIG.get("max_workers", 200)
    _res    = core.CONFIG.get("results_folder", "results")

    def _api(key):
        return "configured ✓" if core.CONFIG.get(key) else "not set   ✗"

    # ── PHASE 1 : MATRIX RAIN ─────────────────────────────────────────────────
    for _frame in range(18):
        wipe()
        for _row in range(23):
            sys.stdout.write(
                core.color("".join(random.choice(MATRIX_CHARS) for _ in range(80))) + "\n"
            )
        sys.stdout.flush()
        time.sleep(0.04)

    # ── PHASE 2 : BOOT LOG STREAM ─────────────────────────────────────────────
    boot_lines = [
        f"[SYS]    BlueFox Kernel v{APP_VERSION} — bootloader active",
        f"[SYS]    Platform  : {_sys} / {_mach}",
        f"[SYS]    Python    : v{_py}",
        f"[MEM]    Memory allocator : initialized",
        f"[CPU]    Thread pool capacity : {_work} workers",
        f"[NET]    Raw socket layer  : ACTIVE",
        f"[NET]    IPv4 stack        : READY",
        f"[NET]    IPv6 stack        : READY",
        f"[DNS]    Resolver pool     : Cloudflare / Google / Quad9",
        f"[FS]     Results folder    : ./{_res}/",
        f"[CFG]    bluefox_config.json : loaded",
        f"[CFG]    UI theme          : {_theme}",
        f"[API]    IPGeolocation     — {_api('ipgeo_api_key')}",
        f"[API]    AbuseIPDB         — {_api('abuseipdb_api_key')}",
        f"[API]    Shodan            — {_api('shodan_api_key')}",
        f"[API]    VirusTotal        — {_api('virustotal_api_key')}",
        f"[API]    Hunter.io         — {_api('hunter_api_key')}",
        f"[API]    NumVerify         — {_api('numverify_api_key')}",
        f"[MOD]    Importing core.runtime ...",
        f"[MOD]    Importing network.scanner ...",
        f"[MOD]    Importing osint.engine ...",
        f"[MOD]    Importing web.recon ...",
        f"[MOD]    Importing intel.forensics ...",
        f"[MOD]    Importing discovery.lab ...",
        f"[MOD]    Importing reports.generator ...",
        f"[RPC]    Discord RPC : {'available' if core.HAS_RPC else 'module not installed'}",
        f"[SYS]    All systems operational — BlueFox shell ready",
    ]

    VISIBLE = 10   # log lines shown at once
    BAR_LEN = 38

    for idx in range(len(boot_lines) + VISIBLE):
        wipe()

        start   = max(0, idx - VISIBLE + 1)
        end     = min(idx + 1, len(boot_lines))
        visible = boot_lines[start:end]

        progress = min((idx + 1) / len(boot_lines), 1.0)
        filled   = int(BAR_LEN * progress)
        bar      = "█" * filled + "░" * (BAR_LEN - filled)
        pct      = int(progress * 100)

        ms  = idx * 68
        ts  = f"{ms // 60000:02d}:{(ms % 60000) // 1000:02d}:{ms % 1000:03d}"

        hdr_left  = f"  BLUEFOX BOOT SEQUENCE v{APP_VERSION}"
        hdr_right = f"[{ts}]"
        hdr_mid   = " " * max(BOX_W - len(hdr_left) - len(hdr_right) - 2, 1)
        hdr_line  = (hdr_left + hdr_mid + hdr_right + " ")[:BOX_W]

        print(core.color("╔" + "═" * BOX_W + "╗"))
        print(core.color(f"║{hdr_line}║"))
        print(core.color("╠" + "═" * BOX_W + "╣"))

        for i in range(VISIBLE):
            if i < len(visible):
                row = f"  {visible[i]}"
            else:
                row = ""
            print(core.color(f"║{row:<{BOX_W}}║"))

        print(core.color("╠" + "═" * BOX_W + "╣"))
        bar_row = f"  [{bar}] {pct:>3}%   bluefox-core v{APP_VERSION}"
        print(core.color(f"║{bar_row:<{BOX_W}}║"))
        print(core.color("╚" + "═" * BOX_W + "╝"))

        time.sleep(0.068)

    time.sleep(0.25)

    # ── PHASE 3 : MODULE STATUS PANEL ─────────────────────────────────────────
    MODULES = [
        ("core.runtime",       "Core utilities & configuration"),
        ("network.scanner",    "IP / port / host reconnaissance"),
        ("osint.engine",       "Username / email / domain intel"),
        ("web.recon",          "HTTP / SSL / redirect analysis"),
        ("intel.forensics",    "IOC / hash / audit helpers"),
        ("discovery.lab",      "DNS / banner / sweep"),
        ("reports.generator",  "Save & export results"),
        ("discord.rpc",        "Rich Presence integration"),
    ]
    MOD_BAR = 16

    for step in range(len(MODULES) + 2):
        wipe()
        print(core.color("╔" + "═" * BOX_W + "╗"))
        title_row = "  MODULE INITIALIZATION STATUS"
        print(core.color(f"║{title_row:<{BOX_W}}║"))
        print(core.color("╠" + "═" * BOX_W + "╣"))

        for i, (mod, desc) in enumerate(MODULES):
            if i < step:
                bar_s  = "█" * MOD_BAR
                status = "LOADED  "
                icon   = "✓"
            elif i == step:
                half   = MOD_BAR // 2
                bar_s  = "█" * half + "▒" * (MOD_BAR - half)
                status = "LOADING "
                icon   = "›"
            else:
                bar_s  = "░" * MOD_BAR
                status = "PENDING "
                icon   = " "

            row = f"  [{icon}] {mod:<22}  [{bar_s}]  {status}  {desc}"
            print(core.color(f"║{row:<{BOX_W}}║"))

        print(core.color("╠" + "═" * BOX_W + "╣"))
        if step >= len(MODULES):
            msg = "  ✓  All modules loaded — BlueFox is ready to launch"
        else:
            msg = f"  ›  Initializing {MODULES[step][0]} ..."
        print(core.color(f"║{msg:<{BOX_W}}║"))
        print(core.color("╚" + "═" * BOX_W + "╝"))

        time.sleep(0.14)

    time.sleep(0.4)

    # ── PHASE 4 : LOGO + PRESS ENTER ─────────────────────────────────────────
    sys_str = f"BlueFox v{APP_VERSION}  |  {_sys} {_mach}  |  Python {_py}"
    sub_str = "Network  |  OSINT  |  Recon  |  Intel  |  Forensics"

    for blink in range(9):
        wipe()
        print(core.color(BANNER))
        print(core.color("┏" + "━" * BOX_W + "┓"))
        print(core.color("┃ " + center_line(sub_str,  BOX_W - 2) + " ┃"))
        print(core.color("┃ " + center_line(sys_str,  BOX_W - 2) + " ┃"))
        print(core.color("┗" + "━" * BOX_W + "┛"))
        print()

        blink_line = "◄◄   PRESS  ENTER  TO  START   ►►"
        border_ln  = "─" * (len(blink_line) + 6)

        if blink % 2 == 0:
            print(core.color2("    " + border_ln))
            print(core.color2("    ║  " + blink_line + "  ║"))
            print(core.color2("    " + border_ln))
        else:
            print(core.color("    " + border_ln))
            print(core.color("    ║  " + blink_line + "  ║"))
            print(core.color("    " + border_ln))

        time.sleep(0.22)

    input(core.color("\n" + center_line(">> Press Enter to launch BlueFox <<") + "\n"))
    wipe()


# ─── BANNER (in-session) ─────────────────────────────────────────────────────
def animated_banner():
    wipe()
    _sys = platform.system()
    _py  = platform.python_version()
    sys_info = f"v{APP_VERSION}  |  {_sys}  |  Python {_py}"
    print(core.color(BANNER))
    print(core.color("┏" + "━" * BOX_W + "┓"))
    print(core.color("┃ " + center_line("Network  |  OSINT  |  Recon  |  Intel  |  Forensics", BOX_W - 2) + " ┃"))
    print(core.color("┃ " + center_line(sys_info, BOX_W - 2) + " ┃"))
    print(core.color("┃ " + center_line(time.strftime('%Y-%m-%d  %H:%M:%S'), BOX_W - 2) + " ┃"))
    print(core.color("┗" + "━" * BOX_W + "┛"))


# ─── TRANSITION ──────────────────────────────────────────────────────────────
def transition(label):
    frames = [
        "[ ▹          ]",
        "[ ▸▹         ]",
        "[ ▸▸▹        ]",
        "[  ▸▸▹       ]",
        "[   ▸▸▹      ]",
        "[    ▸▸▹     ]",
        "[     ▸▸▹    ]",
        "[      ▸▸▹   ]",
        "[       ▸▸▹  ]",
        "[        ▸▸▸ ]",
        "[         ▸▸▹]",
        "[          ▸▸]",
    ]
    for frame in frames * 2:
        wipe()
        print(core.color("\n\n"))
        print(core.color("  ╔" + "═" * (BOX_W - 2) + "╗"))
        inner = f"  {frame}  {label}"
        print(core.color(f"  ║ {inner:<{BOX_W - 4}} ║"))
        print(core.color("  ╚" + "═" * (BOX_W - 2) + "╝"))
        time.sleep(0.032)


# ─── CATEGORY CARD ───────────────────────────────────────────────────────────
def render_category_card(index, key, cat):
    name  = cat["name"]
    desc  = cat["description"]
    count = len(cat["tools"])
    return core.color(
        f"  [{index:02d}]  {name:<30}  {count:>2} tools  │  {desc}"
    )


# ─── MAIN MENU ───────────────────────────────────────────────────────────────
def main_menu():
    wipe()
    animated_banner()
    print(core.color("\n  Select a module:\n"))
    keys = list(registry.CATEGORIES.keys())
    for idx, key in enumerate(keys, 1):
        print(render_category_card(idx, key, registry.CATEGORIES[key]))

    print(core.color("\n  " + "─" * 79))
    print(core.color("  [S]  Settings / API Keys"))
    print(core.color("  [Q]  Quit"))
    print(core.color("  " + "─" * 79))
    return keys


# ─── CATEGORY MENU ───────────────────────────────────────────────────────────
def category_menu(cat_key):
    wipe()
    cat   = registry.CATEGORIES[cat_key]
    title = cat["name"]
    tools = cat["tools"]

    print(core.color("\n  ╔" + "═" * (BOX_W - 2) + "╗"))
    print(core.color(f"  ║  {title:<{BOX_W - 5}}║"))
    print(core.color(f"  ║  {cat['description']:<{BOX_W - 5}}║"))
    print(core.color("  ╚" + "═" * (BOX_W - 2) + "╝"))
    print()

    for i, (name, _) in enumerate(tools, 1):
        print(core.color(f"  [{i:02d}]  {name}"))

    print(core.color("\n  [B]  Back"))
    print(core.color("  " + "─" * 79))
    return tools


# ─── SETTINGS ────────────────────────────────────────────────────────────────
def hacker_settings():
    while True:
        wipe()
        print(core.color("\n  ╔" + "═" * (BOX_W - 2) + "╗"))
        print(core.color(f"  ║{'  BLUEFOX SETTINGS':<{BOX_W - 2}}║"))
        print(core.color(f"  ║{'  API keys are stored in Program/bluefox_config.json':<{BOX_W - 2}}║"))
        print(core.color("  ╚" + "═" * (BOX_W - 2) + "╝\n"))

        current_theme = core.CONFIG.get("ui_theme", "blue")
        print(core.color(f"  Theme: {current_theme}"))
        print()

        for key, meta in settings.API_KEY_FIELDS.items():
            value  = settings.CONFIG.get(key, "")
            status = "✓ SET  " if value else "✗ EMPTY"
            print(core.color(f"  {meta['label']:<16}  [{status}]  {core.mask_secret(value)}"))

        print(core.color("\n  [1]  Edit API keys"))
        print(core.color("  [2]  Results folder"))
        print(core.color("  [3]  Max workers"))
        print(core.color("  [4]  Reset API keys"))
        print(core.color("  [5]  Open API registration links"))
        print(core.color("  [6]  Interface color theme"))
        print(core.color("  [B]  Back"))
        print(core.color("  " + "─" * 79))

        choice = core.get_input("Choice").lower()

        if choice == "b":
            return

        if choice == "1":
            for key, meta in settings.API_KEY_FIELDS.items():
                current = settings.CONFIG.get(key, "")
                print(core.color(f"\n  {meta['label']}  current: {core.mask_secret(current)}"))
                new_val = core.get_input(f"New {meta['label']} key (leave empty to keep)")
                if new_val:
                    settings.CONFIG[key] = new_val.strip()
            settings.save_local_config()
            core.print_success("API keys saved.")
            core.pause()
            continue

        if choice == "2":
            folder = core.get_input(f"Results folder [{settings.CONFIG.get('results_folder', 'results')}]")
            if folder:
                settings.CONFIG["results_folder"] = folder
                os.makedirs(folder, exist_ok=True)
                settings.save_local_config()
                core.print_success("Results folder updated.")
            core.pause()
            continue

        if choice == "3":
            workers = core.get_input(f"Max workers [{settings.CONFIG.get('max_workers', 200)}]")
            try:
                if workers:
                    settings.CONFIG["max_workers"] = max(1, int(workers))
                    settings.save_local_config()
                    core.print_success("Max workers updated.")
            except ValueError:
                core.print_error("Invalid number.")
            core.pause()
            continue

        if choice == "4":
            for key in settings.API_KEY_FIELDS:
                settings.CONFIG[key] = ""
            settings.save_local_config()
            core.print_success("API keys cleared.")
            core.pause()
            continue

        if choice == "5":
            print(core.color("\n  " + "─" * 66))
            print(core.color("  Shodan       →  https://account.shodan.io/register"))
            print(core.color("  VirusTotal   →  https://www.virustotal.com/gui/join-us"))
            print(core.color("  AbuseIPDB    →  https://www.abuseipdb.com/register"))
            print(core.color("  Hunter.io    →  https://hunter.io/users/sign_up"))
            print(core.color("  IPGeo        →  https://ipgeolocation.io/signup"))
            print(core.color("  NumVerify    →  https://numverify.com/product"))
            print(core.color("  " + "─" * 66))
            core.pause()
            continue

        if choice == "6":
            print(core.color("\n  Available themes:"))
            for idx, theme_key in enumerate(core.THEME_PRESETS.keys(), 1):
                marker = "●" if core.CONFIG.get("ui_theme", "blue") == theme_key else "○"
                print(core.color(f"  [{idx}]  {marker}  {theme_key}"))
            selected = core.get_input("Theme (number or name)")
            theme_key = None
            if selected.isdigit():
                items = list(core.THEME_PRESETS.keys())
                if 1 <= int(selected) <= len(items):
                    theme_key = items[int(selected) - 1]
            elif selected.strip().lower() in core.THEME_PRESETS:
                theme_key = selected.strip().lower()

            if theme_key and core.set_ui_theme(theme_key):
                settings.save_local_config()
                core.print_success(f"Theme set to {theme_key}")
            else:
                core.print_error("Invalid theme.")
            core.pause()
            continue

        core.print_error("Invalid choice.")
        time.sleep(0.8)


# ─── TOOL RUNNER ─────────────────────────────────────────────────────────────
def run_tool(tool_func, tool_name, cat_name):
    core.update_rpc(cat_name, tool_name)
    try:
        tool_func()
    except KeyboardInterrupt:
        core.print_warning("Interrupted by user.")
    except Exception as e:
        core.print_error(f"Tool error: {e}")


# ─── MAIN LOOP ────────────────────────────────────────────────────────────────
def main():
    boot_sequence()
    core.init_rpc()
    core.update_rpc("Main Menu", f"BlueFox v{APP_VERSION}")

    while True:
        try:
            keys   = main_menu()
            choice = core.get_input("Choice").lower()

            if choice == "q":
                wipe()
                print(core.color(f"\n  Thanks for using BlueFox v{APP_VERSION}.\n"))
                core.close_rpc()
                sys.exit(0)

            if choice == "s":
                transition("Opening settings")
                hacker_settings()
                continue

            if choice.isdigit() and 1 <= int(choice) <= len(keys):
                cat_key = keys[int(choice) - 1]
                cat     = registry.CATEGORIES[cat_key]
                transition(f"Loading {cat['name']}")

                while True:
                    tools      = category_menu(cat_key)
                    sub_choice = core.get_input("Choice").lower()

                    if sub_choice == "b":
                        break

                    if sub_choice.isdigit() and 1 <= int(sub_choice) <= len(tools):
                        tool_name, tool_func = tools[int(sub_choice) - 1]
                        run_tool(tool_func, tool_name, cat["name"])
                        core.pause()
                    else:
                        core.print_error("Invalid choice.")
                        time.sleep(0.8)
            else:
                core.print_error("Invalid choice.")
                time.sleep(0.8)

        except KeyboardInterrupt:
            wipe()
            print(core.color("\n  Bye.\n"))
            core.close_rpc()
            sys.exit(0)


if __name__ == "__main__":
    main()
