from . import discovery, intel, network, osint, reports, web

CATEGORIES = {
    "NETWORK": {
        "name": "🌐 Network Tools",
        "description": "Outils réseau et analyse IP",
        "tools": network.TOOLS,
    },
    "OSINT": {
        "name": "🔍 OSINT Tools",
        "description": "Open Source Intelligence",
        "tools": osint.TOOLS,
    },
    "WEB": {
        "name": "🕸 Web Recon",
        "description": "Audit rapide de surface web et exposition",
        "tools": web.TOOLS,
    },
    "REPORTS": {
        "name": "📊 Rapports & Export",
        "description": "Génération de rapports et export",
        "tools": reports.TOOLS,
    },
    "DISCOVERY": {
        "name": "🧭 Discovery Lab",
        "description": "Découverte réseau, DNS et service fingerprinting",
        "tools": discovery.TOOLS,
    },
    "INTEL": {
        "name": "🧪 Intel & Forensics",
        "description": "Analyse IOC, hash, permutations et audits ciblés",
        "tools": intel.TOOLS,
    },
}
