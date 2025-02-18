import os

API_ID    = os.environ.get("API_ID", "3737117")
API_HASH  = os.environ.get("API_HASH", "f466ca6ff400954d192ce0992ddf8b5d")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 6969))  # Default to 8000 if not set
