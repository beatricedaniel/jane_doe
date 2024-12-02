import os
import sys
from modules.anonymizer.anonymizer import Anonymizer
from utils.load_docx_files import load_docx_files

def main():
    file_path = "jane_doe/config/config.json"
    printer = Anonymizer()
    printer.read_settings(file_path)
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
