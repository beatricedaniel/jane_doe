# --- modules/pii_detector.py ---
from presidio_analyzer import AnalyzerEngine

def detect_pii(matches: list[str]) -> list[tuple[str, bool]]:
    """Détecte les PII avec Presidio Analyzer."""
    analyzer = AnalyzerEngine()
    results = []
    for match in matches:
        if isinstance(match, tuple):  # Sécurisation supplémentaire
            match = " ".join(match)  
        analysis = analyzer.analyze(text=match, entities=[], language='en')
        is_pii = bool(analysis)
        results.append((match, is_pii))
    return results
