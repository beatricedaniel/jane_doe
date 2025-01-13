import json
import csv
import re
from pathlib import Path
from presidio_analyzer import AnalyzerEngine
from docx import Document

from modules.anonymizer.anonymizer_V2 import WordDocumentAnonymizer

def main():
    # Define the path to the configuration file
    config_file = "jane_doe/config/config.json"

    # Initialize the anonymizer
    anonymizer = WordDocumentAnonymizer(config_file)

    # Ensure output directory exists
    Path(anonymizer.output_dir).mkdir(parents=True, exist_ok=True)

    # Process all Word documents in the input directory
    for input_file in Path(anonymizer.input_dir).glob("*.docx"):
        output_file = Path(anonymizer.output_dir) / input_file.name
        output_csv = anonymizer.resolve_csv_path(input_file)
        anonymizer.process_document(str(input_file), str(output_file), str(output_csv))


if __name__ == "__main__":
    main()
