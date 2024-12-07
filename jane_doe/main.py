import os
import sys
from modules.anonymizer.anonymizer import Anonymizer
from utils.load_settings import load_settings

dev_config_file_path = "jane_doe/config/config.json"

def main():
    extract_sensitive_infos()

#def extract_sensitive_infos(patterns: list, input_dir_path: str, output_csv: str):
def extract_sensitive_infos(config_file_path = dev_config_file_path):
    """Extract all the sensitives informations from the documents and sotre them in a specific .csv file.
    All arguments values correspond to variables of the config/config.json file. 
    Args:
        config_file_path: path of the config file.
    """
    settings = load_settings(config_file_path)
    patterns = Anonymizer.get_patterns(settings)
    input_dir_path = settings.get("input_dir_path")
    output_csv_path = settings.get("output_csv_path")
    Anonymizer.get_sensitive_infos(patterns, input_dir_path, output_csv_path)


    #file_path = "jane_doe/config/config.json"
    #input_path = "jane_doe/data/input/R_EHPAD.docx"
    #printer = Anonymizer()
    #printer.get_patterns(file_path)
    #printer.extract_text_from_docx(input_path)

    # if len(sys.argv) < 2:
    #     print("Usage: python main.py <directory_path>")
    #     sys.exit(1)
    
    # directory_path = sys.argv[1]
    # if not os.path.isdir(directory_path):
    #     print(f"Error: {directory_path} is not a valid directory.")
    #     sys.exit(1)

    # docx_files = load_docx_files(directory_path)
    # anonymizer = Anonymizer()

    # for file_path in docx_files:
    #     print(f"Anonymizing {file_path}...")
    #     anonymizer.anonymize_file(file_path)
    #     print(f"Successfully anonymized {file_path}")

if __name__ == "__main__":
    main()
