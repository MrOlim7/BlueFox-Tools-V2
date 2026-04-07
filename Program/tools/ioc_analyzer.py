import re

from Program import legacy_tools as core


IPV4_RE = re.compile(r"^(?:\d{1,3}\.){3}\d{1,3}$")
DOMAIN_RE = re.compile(r"^(?=.{1,253}$)(?:[a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,63}$")
HASH_RE = re.compile(r"^[a-fA-F0-9]{32}$|^[a-fA-F0-9]{40}$|^[a-fA-F0-9]{64}$")
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def run():
    indicator = core.get_input("IOC (ip/domain/url/hash/email)")
    if not indicator:
        return
    value = indicator.strip()

    core.print_header("IOC ANALYZER")
    result = {"input": value, "type": "unknown"}

    if value.startswith(("http://", "https://")):
        result["type"] = "url"
    elif EMAIL_RE.match(value):
        result["type"] = "email"
    elif IPV4_RE.match(value):
        result["type"] = "ipv4"
    elif HASH_RE.match(value):
        if len(value) == 32:
            result["type"] = "hash_md5"
        elif len(value) == 40:
            result["type"] = "hash_sha1"
        else:
            result["type"] = "hash_sha256"
    elif DOMAIN_RE.match(value.lower()):
        result["type"] = "domain"

    core.print_result("Type", result["type"])

    if result["type"] in ["domain", "url"]:
        domain = value
        if result["type"] == "url":
            domain = core.urlparse(value).netloc
        core.print_result("VirusTotal", f"https://www.virustotal.com/gui/domain/{domain}")
        core.print_result("URLScan", f"https://urlscan.io/search/#domain:{domain}")
        core.print_result("Shodan", f"https://www.shodan.io/search?query={domain}")
        result["links"] = {
            "virustotal": f"https://www.virustotal.com/gui/domain/{domain}",
            "urlscan": f"https://urlscan.io/search/#domain:{domain}",
            "shodan": f"https://www.shodan.io/search?query={domain}",
        }
    elif result["type"] == "ipv4":
        ip = value
        core.print_result("AbuseIPDB", f"https://www.abuseipdb.com/check/{ip}")
        core.print_result("Shodan", f"https://www.shodan.io/host/{ip}")
        core.print_result("VirusTotal", f"https://www.virustotal.com/gui/ip-address/{ip}")
    elif result["type"].startswith("hash_"):
        h = value.lower()
        core.print_result("VirusTotal", f"https://www.virustotal.com/gui/file/{h}")
        core.print_result("MalwareBazaar", f"https://bazaar.abuse.ch/browse.php?search={h}")
    elif result["type"] == "email":
        e = value
        core.print_result("HIBP", f"https://haveibeenpwned.com/account/{e}")
        core.print_result("IntelX", f"https://intelx.io/?s={e}")
    else:
        core.print_warning("IOC non reconnu")

    core.ask_save("ioc_analyzer", result)

