from Program import legacy_tools as core


def run():
    target = core.get_input("IP ou domaine")
    if not target:
        return

    core.print_header("IP/DOMAIN REPUTATION LINKS")
    links = {
        "VirusTotal Domain": f"https://www.virustotal.com/gui/domain/{target}",
        "VirusTotal IP": f"https://www.virustotal.com/gui/ip-address/{target}",
        "AbuseIPDB": f"https://www.abuseipdb.com/check/{target}",
        "Shodan": f"https://www.shodan.io/search?query={target}",
        "AlienVault OTX": f"https://otx.alienvault.com/indicator/hostname/{target}",
        "GreyNoise": f"https://viz.greynoise.io/query/?gnql={target}",
        "URLScan": f"https://urlscan.io/search/#domain:{target}",
    }
    for key, value in links.items():
        core.print_result(key, value)
    core.ask_save("reputation_links", {"target": target, "links": links})

