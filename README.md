# DOCX Anonymizer

A Python tool to anonymize `.docx` files by replacing sensitive information while preserving document formatting. It ensures all identifiable information like names, emails, phone numbers, and addresses are removed or replaced with placeholders.

## Features
- **Maintains Formatting**; Ensures all text formatting is preserved.
- **Customizable Rules**; Use the `config.json` file to specify the placeholder replacing sensitive oinformation.
- **Batch Processing**; Handles multiple `.docx` files.

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
