import re
import json
from utils.load_settings import load_settings
from docx import Document

class Anonymizer():

    def read_settings(self, file_path):
        settings = load_settings(file_path)
        print(settings["anonymization_patterns"][0])


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