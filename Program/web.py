from .legacy_tools import http_headers, robots_sitemap_audit, ssl_cert_info, tech_stack_detector, url_recon

TOOLS = [
    ("URL Recon", url_recon),
    ("Robots / Sitemap Audit", robots_sitemap_audit),
    ("HTTP Headers Analysis", http_headers),
    ("SSL Certificate Info", ssl_cert_info),
    ("Tech Stack Detector", tech_stack_detector),
]

