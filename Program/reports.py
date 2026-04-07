from .tools import list_saved_results, report_generator

TOOLS = [
    ("Generer un rapport", report_generator.run),
    ("Voir les resultats sauvegardes", list_saved_results.run),
]
