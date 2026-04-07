import socket
import ssl

from Program import legacy_tools as core


def run():
    host = core.get_input("Domaine")
    if not host:
        return
    port_raw = core.get_input("Port [443]")
    port = int(port_raw) if port_raw else 443

    core.print_header(f"TLS VERSION PROBE - {host}:{port}")
    versions = []

    if hasattr(ssl, "TLSVersion"):
        versions = [
            ("TLSv1.0", ssl.TLSVersion.TLSv1),
            ("TLSv1.1", ssl.TLSVersion.TLSv1_1),
            ("TLSv1.2", ssl.TLSVersion.TLSv1_2),
            ("TLSv1.3", ssl.TLSVersion.TLSv1_3),
        ]
    else:
        core.print_warning("TLSVersion indisponible sur cette version Python")
        return

    data = {"host": host, "port": port, "versions": {}}
    for label, version in versions:
        try:
            ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            ctx.minimum_version = version
            ctx.maximum_version = version
            with socket.create_connection((host, port), timeout=5) as sock:
                with ctx.wrap_socket(sock, server_hostname=host):
                    data["versions"][label] = "supported"
                    core.print_success(f"{label}: supported")
        except Exception:
            data["versions"][label] = "not_supported"
            core.print_info(f"{label}: not supported")

    core.ask_save(f"tls_probe_{host}", data)

