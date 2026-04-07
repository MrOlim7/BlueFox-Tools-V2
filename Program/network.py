from .legacy_tools import (
    asn_info,
    blacklist_check,
    dns_records,
    ip_lookup,
    my_ip_info,
    ping_ip,
    port_scanner,
    reverse_dns,
    subnet_calculator,
    tcp_connect_test,
    traceroute,
    whois_lookup,
)

TOOLS = [
    ("Ping", ping_ip),
    ("IP Lookup / Geolocation", ip_lookup),
    ("Traceroute", traceroute),
    ("Reverse DNS", reverse_dns),
    ("Port Scanner", port_scanner),
    ("TCP Connect Test", tcp_connect_test),
    ("DNS Records", dns_records),
    ("WHOIS Lookup", whois_lookup),
    ("ASN Information", asn_info),
    ("Blacklist Check", blacklist_check),
    ("My IP / Network Info", my_ip_info),
    ("Subnet Calculator", subnet_calculator),
]
