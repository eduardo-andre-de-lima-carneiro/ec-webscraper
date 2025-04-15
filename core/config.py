import os
from dotenv import load_dotenv

load_dotenv()

def get_config():
    return {
        "HTML_SOURCE_TYPE": os.getenv("HTML_SOURCE_TYPE", "file"),
        "HTML_SOURCE_PATH": os.getenv("HTML_SOURCE_PATH", "page-to-analyse.html"),
        "WAIT_FOR_SELECTOR": os.getenv("WAIT_FOR_SELECTOR", ".vehicle-tile-inner"),
        "HEADLESS": os.getenv("HEADLESS", "true").lower() == "true",
        "EXPORT_PATH": os.getenv("EXPORT_PATH", "vehicles.json"),
    }
