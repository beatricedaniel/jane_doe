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


if __name__ == "__main__":
    main()
    