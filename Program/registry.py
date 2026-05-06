import os
import importlib
import inspect
from typing import Dict, Any, List, Type
from Program.tools.base import BaseTool

# Define the metadata for categories
CATEGORY_METADATA = {
    "NETWORK": {
        "name": "🌐 Network Tools",
        "description": "Outils réseau et analyse IP",
    },
    "OSINT": {
        "name": "🔍 OSINT Tools",
        "description": "Open Source Intelligence",
    },
    "WEB": {
        "name": "🕸 Web Recon",
        "description": "Audit rapide de surface web et exposition",
    },
    "REPORTS": {
        "name": "📊 Rapports & Export",
        "description": "Génération de rapports et export",
    },
    "DISCOVERY": {
        "name": "🧭 Discovery Lab",
        "description": "Découverte réseau, DNS et service fingerprinting",
    },
    "INTEL": {
        "name": "🧪 Intel & Forensics",
        "description": "Analyse IOC, hash, permutations et audits ciblés",
    },
}

class ToolRegistry:
    def __init__(self):
        self.categories: Dict[str, Any] = {}
        self._load_tools()

    def _load_tools(self):
        """Automatically discover and load tools from Program/tools/*.py"""
        tools_dir = os.path.join(os.path.dirname(__file__), "tools")
        if not os.path.exists(tools_dir):
            return

        # Initialize categories from metadata
        for cat_key, meta in CATEGORY_METADATA.items():
            self.categories[cat_key] = {
                "name": meta["name"],
                "description": meta["description"],
                "tools": [],
            }

        # Scan for .py files in Program/tools/
        for filename in os.listdir(tools_dir):
            if filename.endswith(".py") and filename != "base.py":
                module_name = f"Program.tools.{filename[:-3]}"
                try:
                    module = importlib.import_module(module_name)
                    # Find classes that inherit from BaseTool and are not BaseTool itself
                    for name, obj in inspect.getmembers(module, inspect.isclass):
                        if issubclass(obj, BaseTool) and obj is not BaseTool:
                            tool_instance = obj()
                            cat_key = tool_instance.category

                            if cat_key not in self.categories:
                                # Handle categories not defined in METADATA
                                self.categories[cat_key] = {
                                    "name": cat_key.capitalize(),
                                    "description": "Automatic category",
                                    "tools": [],
                                }

                            # Store as (Name, Instance)
                            self.categories[cat_key]["tools"].append((tool_instance.name, tool_instance))
                except Exception as e:
                    print(f"Error loading tool {module_name}: {e}")

    def get_categories(self) -> Dict[str, Any]:
        return self.categories

# Singleton instance
registry = ToolRegistry()
CATEGORIES = registry.get_categories()
