from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access environment variables

# Telegram config
TG_TOKEN: str = os.getenv("TG_TOKEN")

# qBittorrent config
QBT_HOST: str = os.getenv("QBT_HOST")
QBT_PORT: str = os.getenv("QBT_PORT")
QBT_USER: str = os.getenv("QBT_USER")
QBT_PASS: str = os.getenv("QBT_PASS")
