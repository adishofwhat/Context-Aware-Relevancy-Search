import json
from pathlib import Path

def load_json(file_path):
    """Load a JSON file."""
    if not Path(file_path).exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def validate_query(query):
    """Validate that the query is not empty."""
    if not query.strip():
        raise ValueError("Query cannot be empty.")
    return query.strip()