import sys
import time
import platform


from Program import registry, ui, config

# --- CONSTANTS ---
APP_VERSION = config.config.get("version", "2.5 beta")
BANNER = r"""
 ▄▄▄▄    ██▓     █    ██ ▓█████   █████▒▒█████  ▒██   ██▒
▓█████▄ ▓██▒     ██  ▓██▒▓█   ▀ ▓██   ▒▒██▒  ██▒▒▒ █ █ ▒░
▒██▒ ▄██▒██░    ▓██  ▒██░▒███   ▒████ ░▒██░  ██▒░░  █   ░
▒██░█▀  ▒██░    ▓▓█  ░██░▒▓█  ▄ ░▓█▒  ░▒██   ██░ ░ █ █ ▒
░▓█  ▀█▓░██████▒▒▒█████▓ ░▒████▒░▒█░   ░ ████▓▒░▒██▒ ▒██▒
░▒▓███▀▒░ ▒░▓  ░░▒▓▒ ▒ ▒ ░░ ▒░ ░ ▒ ░   ░ ▒ ▒░ ░░   ░▒ ░
▒░▒   ░ ░ ░ ▒  ░░░▒░ ░ ░  ░ ░  ░ ░       ░ ▒ ▒░ ░░   ░▒ ░
 ░    ░   ░ ░    ░░░ ░ ░    ░    ░ ░   ░ ░ ░ ▒   ░    ░
 ░          ░  ░   ░        ░  ░           ░ ░   ░    ░
      ░
"""

def wipe():
    ui.clear()

def center_line(text, width=76):
    return ui.center(text)

def boot_sequence():
    _sys = platform.system()
    _mach = platform.machine()
    _py = platform.python_version()
    _theme = config.config.get("ui_theme", "blue")
    _work = config.config.get("max_workers", 200)
    _res = config.config.get("results_folder", "results")

    # API status helper
    def _api(key):
        return "configured ✓" if config.config.get(key) else "not set   ✗"

    # Phase 1: Matrix Rain (Simplified for brevity)
    ui.clear()
    print(ui.color("\n  [!] Initializing BlueFox Kernel..."))
    time.sleep(0.5)

    # Phase 2: Boot Log
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
        f"[MOD]    Importing osint.engine ...",
        f"[MOD]    Importing web.recon ...",
        f"[MOD]    Importing intel.forensics ...",
        f"[MOD]    Importing discovery.lab ...",
        f"[MOD]    Importing reports.generator ...",
        f"[RPC]    Discord RPC : module active",
        f"[SYS]    All systems operational — BlueFox shell ready",
    ]

    for line in boot_lines:
        print(ui.color(f"  {line}"))
        time.sleep(0.05)

    time.sleep(0.5)
    ui.clear()
    print(ui.color(BANNER))
    print(ui.color("┏" + "━" * 78 + "┓"))
    print(ui.color("┃ " + center_line("Network  |  OSINT  |  Recon  |  Intel  |  Forensics") + " ┃"))
    print(ui.color("┃ " + center_line(f"v{APP_VERSION}  |  {_sys} {_mach}  |  Python {_py}") + " ┃"))
    print(ui.color("┗" + "━" * 78 + "┛"))
    print()
    input(ui.color("\n" + center_line(">> Press Enter to launch BlueFox <<") + "\n"))
    ui.clear()

def animated_banner():
    ui.clear()
    _sys = platform.system()
    _py = platform.python_version()
    sys_info = f"v{APP_VERSION}  |  {_sys}  |  Python {_py}"
    print(ui.color(BANNER))
    print(ui.color("┏" + "━" * 78 + "┓"))
    print(ui.color("┃ " + center_line("Network  |  OSINT  |  Recon  |  Intel  |  Forensics") + " ┃"))
    print(ui.color("┃ " + center_line(sys_info, 76) + " ┃"))
    print(ui.color("┃ " + center_line(time.strftime('%Y-%m-%d  %H:%M:%S'), 76) + " ┃"))
    print(ui.color("┗" + "━" * 78 + "┛"))

def transition(label):
    print(ui.color(f"\n  [>] Loading {label}..."))
    time.sleep(0.3)

def render_category_card(index, key, cat):
    name = cat["name"]
    desc = cat["description"]
    count = len(cat["tools"])
    return ui.color(f"  [{index:02d}]  {name:<30}  {count:>2} tools  │  {desc}")

def main_menu():
    ui.clear()
    animated_banner()
    print(ui.color("\n  Select a module:\n"))
    keys = list(registry.CATEGORIES.keys())
    for idx, key in enumerate(keys, 1):
        print(render_category_card(idx, key, registry.CATEGORIES[key]))

    print(ui.color("\n  " + "─" * 79))
    print(ui.color("  [S]  Settings / API Keys"))
    print(ui.color("  [Q]  Quit"))
    print(ui.color("  " + "─" * 79))
    return keys

def category_menu(cat_key):
    ui.clear()
    cat = registry.CATEGORIES[cat_key]
    print(ui.color("\n  ╔" + "═" * 76 + "╗"))
    print(ui.color(f"  ║  {cat['name']:<{76-4}}║"))
    print(ui.color(f"  ║  {cat['description']:<{76-4}}║"))
    print(ui.color("  ╚" + "═" * 76 + "╝"))
    print()

    tools = cat["tools"]
    for i, (name, tool_instance) in enumerate(tools, 1):
        print(ui.color(f"  [{i:02d}]  {name}"))

    print(ui.color("\n  [B]  Back"))
    print(ui.color("  " + "─" * 79))
    return tools

def run_tool(tool_instance):
    ui.print_header(tool_instance.name)

    # Dynamic Input Collection
    inputs = {}
    for param, prompt in tool_instance.required_inputs.items():
        inputs[param] = ui.get_input(prompt)

    try:
        # Pure logic call
        result = tool_instance.run(**inputs)

        if result.get("success") is False:
            ui.print_error(result.get("error", "Unknown error occurred"))
        elif "error" in result and result["error"]:
            ui.print_error(result["error"])
        else:
            # Generic Result Presenter
            data = result.get("data", result)
            for k, v in data.items():
                ui.print_result(k, v)
            ui.print_success("Tool execution completed.")

    except Exception as e:
        ui.print_error(f"Critical Tool Error: {e}")

    ui.pause()

def hacker_settings():
    # This remains largely the same but uses the new config manager
    while True:
        ui.clear()
        print(ui.color("\n  ╔" + "═" * 76 + "╗"))
        print(ui.color(f"  ║{'  BLUEFOX SETTINGS':<{76-2}}║"))
        print(ui.color(f"  ║{'  API keys are stored in Program/bluefox_config.json':<{76-2}}║"))
        print(ui.color("  ╚" + "═" * 76 + "╝\n"))

        current_theme = config.config.get("ui_theme", "blue")
        print(ui.color(f"  Theme: {current_theme}"))
        print()

        for key, meta in config.API_KEY_FIELDS.items():
            value = config.config.get(key, "")
            status = "✓ SET  " if value else "✗ EMPTY"
            print(ui.color(f"  {meta['label']:<16}  [{status}]  {config.mask_secret(value)}"))

        # Note: For brevity, I've simplified the settings menu options.
        # In a real refactor, we'd build a more robust settings system.
        print(ui.color("\n  [1] Edit API keys"))
        print(ui.color("  [B] Back"))
        print(ui.color("  " + "─" * 79))

        choice = ui.get_input("Choice").lower()
        if choice == "b": return
        if choice == "1":
            for key, meta in config.API_KEY_FIELDS.items():
                val = ui.get_input(f"New {meta['label']} key (leave empty to keep)")
                if val: config.config.set(key, val)
            config.config.save()
            ui.print_success("API keys saved.")
            ui.pause()

def main():
    boot_sequence()

    while True:
        try:
            keys = main_menu()
            choice = ui.get_input("Choice").lower()

            if choice == "q":
                ui.clear()
                print(ui.color(f"\n  Thanks for using BlueFox v{APP_VERSION}.\n"))
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
                    sub_choice = ui.get_input("Choice").lower()

                    if sub_choice == "b":
                        break

                    if sub_choice.isdigit() and 1 <= int(sub_choice) <= len(tools):
                        _, tool_instance = tools[int(sub_choice) - 1]
                        run_tool(tool_instance)
                    else:
                        ui.print_error("Invalid choice.")
                        time.sleep(0.8)
            else:
                ui.print_error("Invalid choice.")
                time.sleep(0.8)

        except KeyboardInterrupt:
            ui.clear()
            print(ui.color("\n  Bye.\n"))
            sys.exit(0)

if __name__ == "__main__":
    main()
