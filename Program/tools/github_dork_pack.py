from Program import legacy_tools as core


def run():
    target = core.get_input("Mot-cle ou domaine")
    if not target:
        return

    core.print_header("GITHUB DORK PACK")
    dorks = [
        f'"{target}" "api_key" site:github.com',
        f'"{target}" "secret" site:github.com',
        f'"{target}" "password" site:github.com',
        f'"{target}" "token" site:github.com',
        f'"{target}" "aws_access_key_id" site:github.com',
        f'"{target}" "BEGIN PRIVATE KEY" site:github.com',
        f'"{target}" ".env" site:github.com',
        f'"{target}" "firebase" "apikey" site:github.com',
    ]

    payload = []
    for dork in dorks:
        url = f"https://www.google.com/search?q={core.quote_plus(dork)}"
        payload.append({"dork": dork, "url": url})
        core.print_result("Dork", dork)
        core.print_result("URL", url)
        print()

    core.ask_save("github_dorks", {"target": target, "dorks": payload})

