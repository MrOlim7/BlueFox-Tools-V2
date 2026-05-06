import os
import json
import re
from datetime import datetime
from typing import Any, Dict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(BASE_DIR, "bluefox_config.json")

API_KEY_FIELDS = {
    "ipgeo_api_key": {"label": "IPGeolocation", "env": "IPGEO_API_KEY"},
    "abuseipdb_api_key": {"label": "AbuseIPDB", "env": "ABUSEIPDB_API_KEY"},
    "shodan_api_key": {"label": "Shodan", "env": "SHODAN_API_KEY"},
    "virustotal_api_key": {"label": "VirusTotal", "env": "VIRUSTOTAL_API_KEY"},
    "hunter_api_key": {"label": "Hunter.io", "env": "HUNTER_API_KEY"},
    "numverify_api_key": {"label": "NumVerify", "env": "NUMVERIFY_API_KEY"},
}

DEFAULT_CONFIG = {
    "version": "2.5 beta",
    "client_id": "1305534641200959600",
    "ui_theme": os.getenv("BLUEFOX_THEME", "blue"),
    "ipgeo_api_key": os.getenv("IPGEO_API_KEY", ""),
    "abuseipdb_api_key": os.getenv("ABUSEIPDB_API_KEY", ""),
    "shodan_api_key": os.getenv("SHODAN_API_KEY", ""),
    "virustotal_api_key": os.getenv("VIRUSTOTAL_API_KEY", ""),
    "hunter_api_key": os.getenv("HUNTER_API_KEY", ""),
    "numverify_api_key": os.getenv("NUMVERIFY_API_KEY", ""),
    "results_folder": "results",
    "max_workers": 200,
}

class ConfigManager:
    def __init__(self):
        self.config = DEFAULT_CONFIG.copy()
        self.load()

    def load(self):
        if not os.path.exists(CONFIG_FILE):
            return

        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                saved = json.load(f)

            for key, value in saved.items():
                if key in self.config and value not in [None, ""]:
                    self.config[key] = value

            try:
                self.config["max_workers"] = int(self.config["max_workers"])
            except (ValueError, TypeError):
                self.config["max_workers"] = 200
        except Exception as e:
            print(f"Config error: {e}")

    def save(self):
        data = {
            "version": self.config["version"],
            "ui_theme": self.config.get("ui_theme", "blue"),
            "results_folder": self.config["results_folder"],
            "max_workers": self.config["max_workers"],
        }
        for key in API_KEY_FIELDS:
            data[key] = self.config.get(key, "")

        try:
            with open(CONFIG_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Save error: {e}")
            return False

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

    def set(self, key: str, value: Any):
        self.config[key] = value

config = ConfigManager()
