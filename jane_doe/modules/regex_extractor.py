# --- modules/regex_extractor.py ---
import re

def extract_text_with_regex(text_data: list[str], patterns: list[str]) -> list[str]:
    """Extrait les chaînes correspondant aux expressions régulières."""
    matches = []
    for pattern in patterns:
        regex = re.compile(pattern)
        for line in text_data:
            found = regex.findall(line)
            if found:
                # Aplatir les tuples en chaînes de caractères
                for item in found:
                    if isinstance(item, tuple):  # Si la regex capture plusieurs groupes
                        matches.append(" ".join(item))  # Concatène les groupes
                    else:
                        matches.append(item)
    return matches
