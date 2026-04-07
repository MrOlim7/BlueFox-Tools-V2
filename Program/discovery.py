from .tools import (
    banner_grabber,
    dns_lookup_suite,
    dns_resolver_compare,
    dns_zone_transfer_test,
    favicon_hash,
    http_title_probe,
    ping_sweep_cidr,
    subdomain_resolver,
)

TOOLS = [
    ("HTTP Title Probe", http_title_probe.run),
    ("Favicon Hash", favicon_hash.run),
    ("DNS Lookup Suite", dns_lookup_suite.run),
    ("DNS Resolver Compare", dns_resolver_compare.run),
    ("Zone Transfer Test", dns_zone_transfer_test.run),
    ("Subdomain Resolver", subdomain_resolver.run),
    ("Ping Sweep CIDR", ping_sweep_cidr.run),
    ("Banner Grabber", banner_grabber.run),
]

