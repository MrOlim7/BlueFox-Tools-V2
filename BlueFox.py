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


def slow_print(lines, delay=0.02):
    for line in lines:
        print(line)
        time.sleep(delay)


def boot_sequence():
    frames = [
        "[*] Initializing BlueFox core...",
        "[/] Loading network modules...",
        "[-] Loading OSINT modules...",
        "[\\] Syncing configuration...",
        "[|] Preparing hacker UI...",
        "[>] Launch complete.",
    ]
    for _ in range(2):
        for frame in frames:
            wipe()
            print(core.color("\n  " + "=" * 66))
            print(core.color("  BlueFox v" + APP_VERSION))
            print(core.color("  " + "-" * 66))
            print(core.color(f"  {frame}"))
            print(core.color("  " + "." * 66))
            time.sleep(0.08)
    wipe()


def animated_banner():
    wipe()
    print(core.color(BANNER))
    print(core.color("  " + "=" * 66))
    print(core.color(f"  BlueFox v{APP_VERSION} | Network / OSINT / Web Recon"))
    print(core.color(f"  {time.strftime('%Y-%m-%d %H:%M:%S')}"))
    print(core.color("  " + "=" * 66))


def transition(label):
    frames = ["[·    ]", "[··   ]", "[···  ]", "[···· ]", "[·····]"]
    for frame in frames:
        wipe()
        print(core.color("\n  " + "=" * 66))
        print(core.color(f"  {label} {frame}"))
        print(core.color("  " + "=" * 66))
        time.sleep(0.05)


def render_category_card(index, key, cat):
    name = cat["name"]
    desc = cat["description"]
    count = len(cat["tools"])
    return core.color(f"  [{index}] {name:<24} {count:>2} tools  |  {desc}")


def main_menu():
    wipe()
    animated_banner()
    print(core.color("\n  Select a module:\n"))
    keys = list(registry.CATEGORIES.keys())
    for idx, key in enumerate(keys, 1):
        print(render_category_card(idx, key, registry.CATEGORIES[key]))

    print(core.color("\n  [S] Settings / API Keys"))
    print(core.color("  [Q] Quit"))
    return keys


def category_menu(cat_key):
    wipe()
    cat = registry.CATEGORIES[cat_key]
    title = cat["name"]
    tools = cat["tools"]

    print(core.color("\n  " + "=" * 66))
    print(core.color(f"  {title}"))
    print(core.color(f"  {cat['description']}"))
    print(core.color("  " + "=" * 66))
    print()

    for i, (name, _) in enumerate(tools, 1):
        prefix = f"  [{i:02d}]"
        print(core.color(f"{prefix} {name}"))

    print(core.color("\n  [B] Back"))
    return tools


def hacker_settings():
    while True:
        wipe()
        print(core.color("\n  " + "=" * 66))
        print(core.color("  BLUEFOX SETTINGS"))
        print(core.color("  API keys are stored locally in bluefox_config.json"))
        print(core.color("  " + "=" * 66))
        print()

        for key, meta in settings.API_KEY_FIELDS.items():
            value = settings.CONFIG.get(key, "")
            status = "OK" if value else "EMPTY"
            print(core.color(f"  {meta['label']:<16} [{status:<5}] {core.mask_secret(value)}"))

        print(core.color("\n  [1] Edit API keys"))
        print(core.color("  [2] Results folder"))
        print(core.color("  [3] Max workers"))
        print(core.color("  [4] Reset API keys"))
        print(core.color("  [5] Open API links"))
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
            sys.exit(0)


if __name__ == "__main__":
    main()
