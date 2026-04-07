import hashlib
import os

from Program import legacy_tools as core


def run():
    path = core.get_input("Chemin du fichier")
    if not path or not os.path.exists(path):
        core.print_error("Fichier introuvable")
        return

    core.print_header(f"FILE HASH AUDIT - {os.path.basename(path)}")
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()
    size = 0

    with open(path, "rb") as f:
        while True:
            chunk = f.read(65536)
            if not chunk:
                break
            size += len(chunk)
            md5.update(chunk)
            sha1.update(chunk)
            sha256.update(chunk)

    data = {
        "file": path,
        "size": size,
        "md5": md5.hexdigest(),
        "sha1": sha1.hexdigest(),
        "sha256": sha256.hexdigest(),
    }

    core.print_result("Size", str(size))
    core.print_result("MD5", data["md5"])
    core.print_result("SHA1", data["sha1"])
    core.print_result("SHA256", data["sha256"])
    core.print_result("VirusTotal", f"https://www.virustotal.com/gui/file/{data['sha256']}")
    core.ask_save(f"hash_{os.path.basename(path)}", data)

