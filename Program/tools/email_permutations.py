from Program import legacy_tools as core


def run():
    first = core.get_input("Prenom")
    last = core.get_input("Nom")
    domain = core.get_input("Domaine email (ex: company.com)")
    if not first or not last or not domain:
        core.print_error("Prenom, nom et domaine requis")
        return

    core.print_header("EMAIL PERMUTATIONS")
    first = first.lower().strip()
    last = last.lower().strip()
    domain = domain.lower().strip()

    local_parts = sorted({
        f"{first}.{last}",
        f"{first}_{last}",
        f"{first}{last}",
        f"{first[0]}{last}",
        f"{first}{last[0]}",
        f"{last}.{first}",
        f"{last}{first[0]}",
    })

    emails = [f"{lp}@{domain}" for lp in local_parts]
    for email in emails:
        core.print_result("candidate", email)

    core.ask_save("email_permutations", {"domain": domain, "emails": emails})

