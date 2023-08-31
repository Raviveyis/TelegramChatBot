import os

class Config():
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH",)
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    BOT_NAME = os.environ.get("BOT_NAME")
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
    SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP")
    SUPPORT_CHANNEL = os.environ.get("SUPPORT_CHANNEL")
    START_IMG = os.environ.get("START_IMG")
