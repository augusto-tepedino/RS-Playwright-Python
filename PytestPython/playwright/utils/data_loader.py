import json
from pathlib import Path

file_path = Path(__file__).parent.parent / "data" / "credentials.json"
with open(file_path) as f:
    USER_CREDENTIAL_LIST = json.load(f)["user_credentials"]