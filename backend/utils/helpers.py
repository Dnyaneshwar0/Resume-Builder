# utils/helpers.py

import os
from datetime import datetime

def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def save_file(content, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        f.write(content)

def version_control_save(base_name, content):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"output/versions/{base_name}_{timestamp}.txt"
    save_file(content, path)
    return path
def extract_section(text, start_keyword, end_keywords):
    pattern = f'{start_keyword}(.*?)(?=' + '|'.join(end_keywords) + '|$)'
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    return match.group(1) if match else ''
