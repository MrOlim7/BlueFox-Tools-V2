import socket

from Program import legacy_tools as core


def run():
    domain = core.get_input("Domaine a verifier")
    if not domain:
        return
    if not core.HAS_DNS:
        core.print_error("dnspython requis: pip install dnspython")
        return

    core.print_header(f"DNS RESOLVER COMPARE - {domain}")
    resolvers = [
        ("Cloudflare", "1.1.1.1"),
        ("Google", "8.8.8.8"),
        ("Quad9", "9.9.9.9"),
        ("OpenDNS", "208.67.222.222"),
    ]
    data = {"domain": domain, "resolvers": {}}

    for name, ip in resolvers:
        resolver = core.dns.resolver.Resolver(configure=False)
        resolver.nameservers = [ip]
        resolver.lifetime = 5
        resolver.timeout = 5
        try:
            answers = resolver.resolve(domain, "A")
            values = sorted({str(a) for a in answers})
            data["resolvers"][name] = values
            core.print_result(name, ", ".join(values))
        except Exception as e:
            data["resolvers"][name] = f"ERROR: {e}"
            core.print_warning(f"{name}: erreur")

    try:
        local_ip = socket.gethostbyname(domain)
        data["local_resolver"] = local_ip
        core.print_result("Local resolver", local_ip)
    except Exception:
        pass

    core.ask_save(f"dns_compare_{domain}", data)

