import os
from dotenv import load_dotenv

# Load .env from project root (default behavior)
load_dotenv()

WANTED_API_KEY = os.getenv("WANTED_API_KEY", "").strip()

def require_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(f"Missing environment variable: {name}")
    return value
