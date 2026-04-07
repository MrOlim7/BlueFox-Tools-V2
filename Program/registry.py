from . import network, osint, reports, web

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
}

