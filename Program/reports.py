from .legacy_tools import list_saved_results, report_generator

TOOLS = [
    ("Générer un rapport", report_generator),
    ("Voir les résultats sauvegardés", list_saved_results),
]

