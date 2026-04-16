from Program import core
import subprocess
import platform

def run():
    ip = core.get_input("Adresse IP à ping")
    if not ip:
        return
    core.update_rpc("Ping IP", f"Ping de {ip}")
    core.print_header(f"PING - {ip}")
    try:
        if platform.system().lower() == "windows":
            result = subprocess.run(['ping', '-n', '4', ip], capture_output=True, text=True, timeout=15)
        else:
            result = subprocess.run(['ping', '-c', '4', ip], capture_output=True, text=True, timeout=15)
        print(core.color(result.stdout))
        if result.returncode != 0:
            core.print_error("Hôte injoignable ou timeout.")
    except subprocess.TimeoutExpired:
        core.print_error("Timeout expiré.")
    except Exception as e:
        core.print_error(f"Erreur: {e}")
