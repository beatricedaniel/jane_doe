import os

import json

def load_docx_files(directory_path):
    return [
        os.path.join(directory_path, f) 
        for f in os.listdir(directory_path) 
        if f.endswith(".docx")
    ]