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

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def anonymize_content(doc_content, filtered_results, placeholder):
    """
    Anonymise le contenu d'un document tout en conservant la mise en page.
    
    :param doc_content: Liste des paragraphes ou tables (chaînes de caractères ou structure de table).
    :param filtered_results: Résultats filtrés contenant les occurrences à anonymiser.
    :param placeholder: Texte à utiliser pour remplacer les données sensibles.
    :return: Contenu anonymisé.
    """
    anonymized_content = []

    for element in doc_content:
        if isinstance(element, str):
            # Traiter les paragraphes en tant que chaînes de caractères
            updated_element = element
            already_replaced = set()

            for original_text, _, is_pii in filtered_results:
                if is_pii and original_text not in already_replaced:
                    updated_element = updated_element.replace(original_text, placeholder)
                    already_replaced.add(original_text)

            anonymized_content.append(updated_element)
        elif isinstance(element, list):
            # Traiter les tables représentées comme des listes de listes
            updated_table = []

            for row in element:
                updated_row = []
                for cell in row:
                    updated_cell = cell
                    already_replaced = set()

                    for original_text, _, is_pii in filtered_results:
                        if is_pii and original_text not in already_replaced:
                            updated_cell = updated_cell.replace(original_text, placeholder)
                            already_replaced.add(original_text)

                    updated_row.append(updated_cell)
                updated_table.append(updated_row)

            anonymized_content.append(updated_table)
        else:
            logging.warning("Élément non reconnu dans le contenu du document. Ignoré.")

    return anonymized_content

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

    for doc_name, doc_content in documents.items():
        matches = extract_text_with_regex(doc_content, regex_patterns)
        pii_results = detect_pii(matches)
        filtered_results = filter_false_positives(pii_results, acronyms_file, pii_regex_exclusions)
        extracted_data.extend([(doc_name, *res) for res in filtered_results])

        # Anonymiser le contenu tout en conservant la mise en page
        anonymized_content = anonymize_content(doc_content, filtered_results, placeholder)
        anonymized_documents[doc_name] = anonymized_content

    # Générer le rapport CSV
    generate_report(extracted_data, output_report)

    # Sauvegarder les documents anonymisés
    save_anonymized_documents(word_documents_dir, anonymized_documents)

    logging.info("Processus terminé avec succès.")

if __name__ == "__main__":
    main()
