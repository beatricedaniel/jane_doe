# DOCX Anonymizer

A Python tool to anonymize `.docx` files by replacing sensitive information. It ensures all identifiable information like names, emails, locations, are replaced with placeholders.

## Features
- **Custom patterns**; use config.json to configure the patterns of sensitive informations you want to anonymized. You can also configure patterns you want to exclude from this anonymization.
- **NLP PII recognition**; this script uses Spacy NLP model to recognize true PII from expressions identified by regex.
- **Exclude acronyms**; as this script is designed for administration, input documents contains a lot of acronyms which are false positiv. You can load a .csv file with a list of acronyms to exclude.
- **Monitor**; in addition to the anonymized documents, this script generates a .csv file with all expressions identified by regex and if they are truely recognized as PII by the NLP model.

## Prerequires
- install pipx
- install poetry
- `poetry init`
- `poetry install`

## Installation
1. Clone this repository;
   ```bash
   git clone https;//github.com/your-username/docx-anonymizer.git
   cd docx-anonymizer

## Script usage
`poetry run python main.py /path/to/your/docx/files`# jane_doe
