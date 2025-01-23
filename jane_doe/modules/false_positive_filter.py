from pathlib import Path
import csv
import re

def filter_false_positives(detected_pii: list[tuple[str, bool]], acronyms_file: Path, exclusions: list[str]) -> list[tuple[str, str, bool]]:
    """Filtre les faux positifs en utilisant une liste d'acronymes et d'expressions régulières d'exclusion."""
    with open(acronyms_file, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        acronyms = {row[0] for row in reader}
    
    filtered_results = []
    for text, is_pii in detected_pii:
        if text in acronyms:
            is_pii = False
        if any(re.match(pattern, text) for pattern in exclusions):
            is_pii = False
        filtered_results.append((text, "non" if is_pii else "oui", is_pii))
    
    return filtered_results
