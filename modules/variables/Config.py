import json
from os.path import dirname, join as path_join, exists

TOKEN_FILE = path_join(dirname(__file__), 'tokens.json')

def get_token(name: str) -> str:
    """Retrieve token from the JSON file."""
    if not exists(TOKEN_FILE):
        return None
    with open(TOKEN_FILE, 'r') as file:
        tokens = json.load(file)
    return tokens.get(name)

def save_token(name: str, value: str):
    """Save token into the JSON file."""
    tokens = {}
    try:
        if exists(TOKEN_FILE):
            with open(TOKEN_FILE, 'r') as file:
                tokens = json.load(file)
        tokens[name] = value
        with open(TOKEN_FILE, 'w') as file:
            json.dump(tokens, file, indent=4)
        return True
    except:
        return False
