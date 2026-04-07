from .tools import (
    email_permutations,
    file_hash_audit,
    ioc_analyzer,
    ip_reputation_links,
    netblock_host_counter,
    password_strength_estimator,
    tls_version_probe,
    username_variations,
)

TOOLS = [
    ("IOC Analyzer", ioc_analyzer.run),
    ("File Hash Audit", file_hash_audit.run),
    ("Password Strength Estimator", password_strength_estimator.run),
    ("Username Variations", username_variations.run),
    ("Email Permutations", email_permutations.run),
    ("IP/Domain Reputation Links", ip_reputation_links.run),
    ("Netblock Host Counter", netblock_host_counter.run),
    ("TLS Version Probe", tls_version_probe.run),
]

