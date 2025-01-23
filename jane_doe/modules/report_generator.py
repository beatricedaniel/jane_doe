# --- modules/report_generator.py ---
from pathlib import Path
import csv

def generate_report(data: list[tuple[str, str, bool]], output_file: Path) -> None:
    """Génère un fichier CSV avec les résultats du traitement."""
    with open(output_file, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Nom du document", "Chaine identifiée", "Est faux positif", "Page"])
        for row in data:
            writer.writerow(row)
