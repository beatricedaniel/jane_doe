import os

import json

def load_settings(file_path: str) -> dict:
    """
    Load settings from a JSON file.
    
    Args:
        file_path (str): Path to the settings JSON file.
    
    Returns:
        dict: A dictionary containing settings.
    """
    try:
        with open(file_path, 'r') as file:
            settings = json.load(file)
        return settings
    except FileNotFoundError:
        raise FileNotFoundError(f"Settings file not found at {file_path}")
    except json.JSONDecodeError:
        raise ValueError("Error parsing the settings file.")