from .tools import (
    host_header_probe,
    http_headers,
    redirect_chain_analyzer,
    robots_sitemap_audit,
    security_txt_audit,
    ssl_cert_info,
    tech_stack_detector,
    url_recon,
)

TOOLS = [
    ("URL Recon", url_recon.run),
    ("Robots / Sitemap Audit", robots_sitemap_audit.run),
    ("HTTP Headers Analysis", http_headers.run),
    ("SSL Certificate Info", ssl_cert_info.run),
    ("Tech Stack Detector", tech_stack_detector.run),
    ("Host Header Probe", host_header_probe.run),
    ("Security.txt Audit", security_txt_audit.run),
    ("Redirect Chain Analyzer", redirect_chain_analyzer.run),
]
