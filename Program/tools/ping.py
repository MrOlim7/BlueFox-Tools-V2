import subprocess
import platform
from typing import Any, Dict
from Program.tools.base import BaseTool

class PingTool(BaseTool):
    @property
    def category(self) -> str:
        return "NETWORK"

    @property
    def name(self) -> str:
        return "Ping IP"

    @property
    def description(self) -> str:
        return "Verify if a host is reachable via ICMP ping."

    @property
    def required_inputs(self) -> Dict[str, str]:
        return {"ip": "Adresse IP à ping"}

    def run(self, ip: str) -> Dict[str, Any]:
        if not ip:
            raise ValueError("IP address is required")

        try:
            if platform.system().lower() == "windows":
                result = subprocess.run(['ping', '-n', '4', ip], capture_output=True, text=True, timeout=15)
            else:
                result = subprocess.run(['ping', '-c', '4', ip], capture_output=True, text=True, timeout=15)

            return {
                "ip": ip,
                "output": result.stdout,
                "success": result.returncode == 0,
                "error": None if result.returncode == 0 else "Host unreachable or timeout"
            }
        except subprocess.TimeoutExpired:
            return {"ip": ip, "output": "", "success": False, "error": "Timeout expired"}
        except Exception as e:
            return {"ip": ip, "output": "", "success": False, "error": str(e)}
