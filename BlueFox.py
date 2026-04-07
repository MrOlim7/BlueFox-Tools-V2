import os
import sys
import time

from Program import legacy_tools as core
from Program import registry, settings


APP_VERSION = core.CONFIG.get("version", "2.4 beta")

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


def wipe():
    core.clear()


def center_line(text, width=76):
    return text.center(width)


def boot_sequence():
    code_stream = [
        "import core.runtime",
        "load module network.scan",
        "load module osint.lookup",
        "load module web.recon",
        "establish rpc tunnel",
        "hydrate local settings",
        "verify api keys state",
        "prepare ui renderer",
        "compile menu registry",
        "arming bluefox shell",
    ]

    for idx in range(24):
        wipe()
        print(core.color("┌" + "─" * 78 + "┐"))
        print(core.color("│ " + center_line("TERMINAL BOOTSTREAM", 76) + " │"))
        print(core.color("├" + "─" * 78 + "┤"))
        for i in range(12):
            stream_index = (idx + i) % len(code_stream)
            left = f"[{(idx+i):02d}]"
            line = f"{left} {code_stream[stream_index]} ; status=ok"
            print(core.color("│ " + line.ljust(76) + " │"))
        print(core.color("├" + "─" * 78 + "┤"))
        bar_len = (idx % 11) + 1
        bar = ("#" * bar_len).ljust(11)
        print(core.color(f"│ loading [{bar}]  bluefox-core v{APP_VERSION:<45} │"))
        print(core.color("└" + "─" * 78 + "┘"))
        time.sleep(0.05)

    for blink in range(6):
        wipe()
        print()
        print(core.color(center_line("██████  ██      ██    ██  ████████  ███████  ██████  ██   ██")))
        print(core.color(center_line("██   ██ ██      ██    ██  ██        ██      ██    ██  ██ ██ ")))
        print(core.color(center_line("██████  ██      ██    ██  ██████    █████   ██    ██   ███  ")))
        print(core.color(center_line("██   ██ ██      ██    ██  ██        ██      ██    ██  ██ ██ ")))
        print(core.color(center_line("██████  ███████  ██████   ████████  ██       ██████  ██   ██")))
        print()
        if blink % 2 == 0:   
            print(core.color(center_line(f"BlueFox {APP_VERSION}")))
            print(core.color(center_line("PRESS ENTER TO START")))
        time.sleep(0.18)

    input(core.color("\n" + center_line(">> Press Enter to Start BlueFox <<") + "\n"))
    wipe()


def animated_banner():
    wipe()
    print(core.color(BANNER))
    print(core.color("┏" + "━" * 78 + "┓"))
    print(core.color("┃ " + center_line(f"BlueFox v{APP_VERSION} | Network | OSINT | Recon", 76) + " ┃"))
    print(core.color("┃ " + center_line(time.strftime('%Y-%m-%d %H:%M:%S'), 76) + " ┃"))
    print(core.color("┗" + "━" * 78 + "┛"))


def transition(label):
    frames = ["[>      ]", "[>>     ]", "[>>>    ]", "[ >>>>  ]", "[  >>>>>]", "[   >>>>]"]
    for frame in frames * 2:
        wipe()
        print(core.color("\n  " + "╔" + "═" * 78 + "╗"))
        print(core.color(f"  ║ {label:<58} {frame:<16} ║"))
        print(core.color("  " + "╚" + "═" * 78 + "╝"))
        time.sleep(0.035)


def render_category_card(index, key, cat):
    name = cat["name"]
    desc = cat["description"]
    count = len(cat["tools"])
    return core.color(f"  [{index:02d}] {name:<26} {count:>2} tools | {desc}")


def main_menu():
    wipe()
    animated_banner()
    print(core.color("\n  Select a module:\n"))
    keys = list(registry.CATEGORIES.keys())
    for idx, key in enumerate(keys, 1):
        print(render_category_card(idx, key, registry.CATEGORIES[key]))

    print(core.color("\n  [S] Settings / API Keys"))
    print(core.color("  [Q] Quit"))
    print(core.color("  " + "-" * 80))
    return keys


def category_menu(cat_key):
    wipe()
    cat = registry.CATEGORIES[cat_key]
    title = cat["name"]
    tools = cat["tools"]

    print(core.color("\n  " + "╔" + "═" * 78 + "╗"))
    print(core.color(f"  ║ {title:<76} ║"))
    print(core.color(f"  ║ {cat['description']:<76} ║"))
    print(core.color("  " + "╚" + "═" * 78 + "╝"))
    print()

    for i, (name, _) in enumerate(tools, 1):
        prefix = f"[{i:02d}]"
        print(core.color(f"  {prefix} {name}"))

    print(core.color("\n  [B] Back"))
    print(core.color("  " + "-" * 80))
    return tools


def hacker_settings():
    while True:
        wipe()
        print(core.color("\n  " + "=" * 66))
        print(core.color("  BLUEFOX SETTINGS"))
        print(core.color("  API keys are stored locally in bluefox_config.json"))
        print(core.color("  " + "=" * 66))
        print()

        current_theme = core.CONFIG.get("ui_theme", "blue")
        print(core.color(f"  Interface theme: {current_theme}"))
        for key, meta in settings.API_KEY_FIELDS.items():
            value = settings.CONFIG.get(key, "")
            status = "OK" if value else "EMPTY"
            print(core.color(f"  {meta['label']:<16} [{status:<5}] {core.mask_secret(value)}"))

        print(core.color("\n  [1] Edit API keys"))
        print(core.color("  [2] Results folder"))
        print(core.color("  [3] Max workers"))
        print(core.color("  [4] Reset API keys"))
        print(core.color("  [5] Open API links"))
        print(core.color("  [6] Interface color theme"))
        print(core.color("  [B] Back"))

        choice = core.get_input("Choice").lower()

        if choice == "b":
            return

        if choice == "1":
            for key, meta in settings.API_KEY_FIELDS.items():
                current = settings.CONFIG.get(key, "")
                print(core.color(f"\n  {meta['label']} current: {core.mask_secret(current)}"))
                new_value = core.get_input(f"New {meta['label']} key (leave empty to keep)")
                if new_value:
                    settings.CONFIG[key] = new_value.strip()
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
            print(core.color("\n  " + "-" * 66))
            print(core.color("  Shodan       https://account.shodan.io/register"))
            print(core.color("  VirusTotal   https://www.virustotal.com/gui/join-us"))
            print(core.color("  AbuseIPDB    https://www.abuseipdb.com/register"))
            print(core.color("  Hunter.io    https://hunter.io/users/sign_up"))
            print(core.color("  IPGeo        https://ipgeolocation.io/signup"))
            core.pause()
            continue

        if choice == "6":
            print(core.color("\n  Themes disponibles:"))
            for idx, theme_key in enumerate(core.THEME_PRESETS.keys(), 1):
                marker = "*" if core.CONFIG.get("ui_theme", "blue") == theme_key else " "
                print(core.color(f"  [{idx}] {marker} {theme_key}"))
            selected = core.get_input("Theme (numéro ou nom)")
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
                core.print_error("Theme invalide")
            core.pause()
            continue

        core.print_error("Invalid choice")
        time.sleep(0.8)


def run_tool(tool_func, tool_name, cat_name):
    core.update_rpc(cat_name, tool_name)
    try:
        tool_func()
    except KeyboardInterrupt:
        core.print_warning("Interrupted by user")
    except Exception as e:
        core.print_error(f"Tool error: {e}")


def main():
    boot_sequence()
    core.init_rpc()
    core.update_rpc("Menu Principal", f"BlueFox v{APP_VERSION}")

    while True:
        try:
            keys = main_menu()
            choice = core.get_input("Choice").lower()

            if choice == "q":
                wipe()
                print(core.color("\n  Thanks for using BlueFox.\n"))
                core.close_rpc()
                sys.exit(0)

            if choice == "s":
                transition("Opening settings")
                hacker_settings()
                continue

            if choice.isdigit() and 1 <= int(choice) <= len(keys):
                cat_key = keys[int(choice) - 1]
                cat = registry.CATEGORIES[cat_key]
                transition(f"Loading {cat['name']}")

                while True:
                    tools = category_menu(cat_key)
                    sub_choice = core.get_input("Choice").lower()

                    if sub_choice == "b":
                        break

                    if sub_choice.isdigit() and 1 <= int(sub_choice) <= len(tools):
                        tool_name, tool_func = tools[int(sub_choice) - 1]
                        run_tool(tool_func, tool_name, cat["name"])
                        core.pause()
                    else:
                        core.print_error("Invalid choice")
                        time.sleep(0.8)
            else:
                core.print_error("Invalid choice")
                time.sleep(0.8)

        except KeyboardInterrupt:
            wipe()
            print(core.color("\n  Bye.\n"))
            core.close_rpc()
            sys.exit(0)


if __name__ == "__main__":
    main()
