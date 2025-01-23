import os
import json
import csv
import logging
from pathlib import Path
from modules.file_handler import load_word_documents, save_anonymized_documents
from modules.regex_extractor import extract_text_with_regex
from modules.pii_detector import detect_pii
from modules.false_positive_filter import filter_false_positives
from modules.report_generator import generate_report
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig


# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """Point d'entrée principal du script."""
    # Charger la configuration
    config_path = Path("jane_doe/settings/config.json")
    if not config_path.exists():
        logging.error("Le fichier de configuration est introuvable.")
        return
    
    with open(config_path, "r", encoding="utf-8") as config_file:
        config = json.load(config_file)
    
    word_documents_dir = Path(config["word_documents_dir"])
    acronyms_file = Path(config["acronyms_file"])
    output_report = Path(config["output_report"])
    regex_patterns = config["regex_patterns"]
    pii_regex_exclusions = config["pii_regex_exclusions"]
    placeholder = config["placeholder"]

    # Vérifier l'existence des répertoires
    if not word_documents_dir.exists():
        logging.error(f"Le répertoire contenant les documents Word n'existe pas: {word_documents_dir}")
        return
    
    if not acronyms_file.exists():
        logging.error(f"Le fichier des acronymes est introuvable: {acronyms_file}")
        return
    
    # Charger les documents Word
    documents = load_word_documents(word_documents_dir)
    if not documents:
        logging.warning("Aucun document Word trouvé.")
        return
    
    extracted_data = []
    anonymized_documents = {}
    anonymizer = AnonymizerEngine()
    
    for doc_name, doc_content in documents.items():
        matches = extract_text_with_regex(doc_content, regex_patterns)
        pii_results = detect_pii(matches)
        filtered_results = filter_false_positives(pii_results, acronyms_file, pii_regex_exclusions)
        extracted_data.extend([(doc_name, *res) for res in filtered_results])
        
        # Créer une copie anonymisée du document
        anonymized_content = []
        for line in doc_content:
            updated_line = line
            # Gérer les duplications en traquant les portions déjà anonymisées
            already_replaced = set()
            for original_text, _, is_pii in filtered_results:
                if not is_pii and original_text not in already_replaced:
                    # Trouver toutes les occurrences de la chaîne et les remplacer
                    start_index = 0
                    while start_index != -1:
                        start_index = updated_line.find(original_text, start_index)
                        if start_index != -1:
                            end_index = start_index + len(original_text)
                            analyzer_results = [
                                RecognizerResult(
                                    entity_type="PII",
                                    start=start_index,
                                    end=end_index,
                                    score=1.0  # Confiance élevée
                                )
                            ]
                            anonymization_result = anonymizer.anonymize(
                                text=updated_line,
                                analyzer_results=analyzer_results,
                                operators={"PII": OperatorConfig("replace", {"new_value": placeholder})}
                            )
                            updated_line = anonymization_result.text
                            already_replaced.add(original_text)
                            start_index = end_index  # Avancer pour trouver la prochaine occurrence
            anonymized_content.append(updated_line)
        
        anonymized_documents[doc_name] = anonymized_content
    
    # Générer le rapport CSV
    generate_report(extracted_data, output_report)
    
    # Sauvegarder les documents anonymisés
    save_anonymized_documents(word_documents_dir, anonymized_documents)
    
    logging.info("Processus terminé avec succès.")

if __name__ == "__main__":
    main()
