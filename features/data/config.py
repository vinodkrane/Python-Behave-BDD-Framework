"""Config Reader to read test data from JSON."""
import os
import json

settings = None

def load_settings():
    """Load settings.json."""
    global settings
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.json')) as f:
        settings = json.load(f)

load_settings()