import os
import re
import csv 
import json
from utils.load_docx_files import load_docx_files
from docx import Document

class Anonymizer():

    def get_patterns(settings: dict) -> list:
        """Get list of patterns from the config dictionary.
        Args:
            settings: dictionary.
        Returns:
            list of patterns.
        """
        patterns = settings.get("anonymization_patterns", [])
        try:
            return patterns
        except ValueError:
            raise ValueError("Patterns must be a list")
        
    def get_sensitive_infos(patterns: list, input_dir_path: str, output_csv_path: str) -> list:
        """Get list of words corresponding to the patterns.
        Args:
            patterns: list of regex patterns.
            input_dir_path: directory where are the input documents.
            output_csv_path: path of the csv file where are stored results.
        Returns:
            csv file with 
                a acolumn for the sensitive infos extracted
                a column for the location of each word.
        """
        docx_directory = load_docx_files(input_dir_path)
        for docx_path in docx_directory:
            document = Document(docx_path)
            results = []
            # Extract from paragraphs
            for i, paragraph in enumerate(document.paragraphs):
                for pattern in patterns:
                    matches = pattern.findall(paragraph.text)
                    for match in matches:
                        results.append({
                            "word": match,
                            "location": f"Paragraph {i + 1}"
                        })
            # Extract from tables
            for table_idx, table in enumerate(document.tables):
                for row_idx, row in enumerate(table.rows):
                    for col_idx, cell in enumerate(row.cells):
                        for pattern in patterns:
                            matches = pattern.findall(cell.text)
                            for match in matches:
                                results.append({
                                    "word": match,
                                    "location": f"Table {table_idx + 1}, Row {row_idx + 1}, Column {col_idx + 1}"
                                })
        return

    # def get_patterns(self, file_path: str) -> list:
    #     """Get the pztterns of the regex corresponding to sensitive informations.
    #     Args:
    #         file_path: path of the file containing the patterns.
    #     Return:
    #         list: the list of all the regex patterns
    #     """
    #     settings = load_settings(file_path)
    #     patterns = settings.get("anonymization_patterns", [])
    #     print(patterns)
    #     return patterns

    def extract_text_from_docx(self, filepath):
        """Extracts text from a .docx file, including both paragraphs and tables."""
        document = Document(filepath)
        text_parts = []

        # Extract text from paragraphs
        text_parts.extend(paragraph.text for paragraph in document.paragraphs)
        
        # Extract text from tables
        for table in document.tables:
            for row in table.rows:
                for cell in row.cells:
                    text_parts.append(cell.text)
                    
        print("\n".join(text_parts))       
        # return "\n".join(text_parts)
    

# import os
# import re
# import csv
# import json
# from docx import Document

# # Paths
# DIRECTORY_PATH = './docx_files'
# OUTPUT_CSV = 'extracted_names.csv'
# PATTERNS_JSON_FILE = 'name_patterns.json'

# def load_name_patterns(json_path):
#     """Loads name patterns from a JSON file."""
#     with open(json_path, 'r', encoding='utf-8') as file:
#         data = json.load(file)
#     return data.get('patterns', [])

# def extract_text_from_docx(filepath):
#     """Extracts text from a .docx file, including both paragraphs and tables."""
#     document = Document(filepath)
#     text_parts = []
    
#     # Extract text from paragraphs
#     text_parts.extend(paragraph.text for paragraph in document.paragraphs)
    
#     # Extract text from tables
#     for table in document.tables:
#         for row in table.rows:
#             for cell in row.cells:
#                 text_parts.append(cell.text)
                
#     return "\n".join(text_parts)

# def find_names(text, patterns):
#     """Finds names using patterns loaded from the JSON file."""
#     names = set()
#     for pattern in patterns:
#         matches = re.findall(pattern, text)
#         for match in matches:
#             names.add(" ".join(match).strip())
#     return names

# def main():
#     # Load name patterns from JSON file
#     name_patterns = load_name_patterns(PATTERNS_JSON_FILE)
#     if not name_patterns:
#         print("No patterns found in the JSON file.")
#         return

#     all_names = set()

#     # Traverse through all .docx files in the directory
#     for filename in os.listdir(DIRECTORY_PATH):
#         if filename.endswith('.docx'):
#             filepath = os.path.join(DIRECTORY_PATH, filename)
#             print(f"Processing: {filename}")
            
#             # Extract text and find names
#             text = extract_text_from_docx(filepath)
#             found_names = find_names(text, name_patterns)
#             all_names.update(found_names)

#     # Write names to a CSV file
#     with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(['First Name', 'Last Name'])
#         for name in sorted(all_names):
#             if len(name.split()) == 2:  # Ensure we have a valid Firstname Lastname pair
#                 writer.writerow(name.split())
#             else:
#                 writer.writerow([name])  # For Title Lastname

#     print(f"Extraction complete. Names saved to '{OUTPUT_CSV}'.")

# if __name__ == '__main__':
#     main()



    # def __init__(self):
    #     self.config = self.load_config()
    #     self.placeholder = self.config.get("placeholder", "[REDACTED]")
    
    # def load_config(self):
    #     with open("jane_doe/config/config.json", "r") as file:
    #         return json.load(file)

    # def anonymize_text(self, text):
    #     # Anonymize emails
    #     text = re.sub(
    #         r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    #         self.placeholder,
    #         text
    #     )

    #     # Anonymize names (Generalized: Capitalized, Uppercase)
    #     # Capitalized format: "Firstname Lastname"
    #     text = re.sub(
    #         r'\b[A-Z][a-z]+ [A-Z][a-z]+\b',
    #         self.placeholder,
    #         text
    #     )
    #     # Uppercase format: "FIRSTNAME LASTNAME"
    #     text = re.sub(
    #         r'\b[A-Z]+ [A-Z]+\b',
    #         self.placeholder,
    #         text
    #     )

    #     # Anonymize phone numbers
    #     text = re.sub(
    #         r'\b(\+?\d{1,3})?[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}\b',
    #         self.placeholder,
    #         text
    #     )

    #     return text

    # def anonymize_file(self, file_path):
    #     doc = Document(file_path)
    #     for paragraph in doc.paragraphs:
    #         paragraph.text = self.anonymize_text(paragraph.text)
    #     for table in doc.tables:
    #         for row in table.rows:
    #             for cell in row.cells:
    #                 cell.text = self.anonymize_text(cell.text)
    #     doc.save(file_path)