from Program import legacy_tools as core


def run():
    first = core.get_input("Prenom")
    last = core.get_input("Nom")
    nick = core.get_input("Pseudo de base (optionnel)")
    if not first and not last and not nick:
        return

    core.print_header("USERNAME VARIATIONS")
    first = first.lower().strip()
    last = last.lower().strip()
    nick = nick.lower().strip()

    variants = set()
    if nick:
        variants.add(nick)
        variants.add(f"{nick}01")
        variants.add(f"{nick}123")
    if first and last:
        variants.update({
            f"{first}{last}",
            f"{first}.{last}",
            f"{first}_{last}",
            f"{first[0]}{last}",
            f"{first}{last[0]}",
            f"{last}{first}",
            f"{last}.{first}",
        })
    if first:
        variants.update({first, f"{first}01", f"{first}x"})
    if last:
        variants.update({last, f"{last}01"})

    data = {"count": len(variants), "variants": sorted(variants)}
    for v in data["variants"]:
        core.print_result("username", v)
    core.ask_save("username_variations", data)

