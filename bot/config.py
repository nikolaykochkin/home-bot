import os
from dotenv import load_dotenv


def get_qbt_conn_info():
    qbt_host: str = os.getenv("QBT_HOST")
    qbt_port: int = int(os.getenv("QBT_PORT"))
    qbt_user: str = os.getenv("QBT_USER")
    qbt_pass: str = os.getenv("QBT_PASS")
    return {
        'host': qbt_host,
        'port': qbt_port,
        'username': qbt_user,
        'password': qbt_pass,
    }


def get_server_config():
    server_host: str = os.getenv("SRV_HOST")
    server_port: int = int(os.getenv("SRV_PORT"))
    return {
        'host': server_host,
        'port': server_port,
    }


# Load environment variables from the .env file
load_dotenv()

# Access environment variables
# Telegram config
tg_token: str = os.getenv("TG_TOKEN")

# qBittorrent config
qbt_conn_info = get_qbt_conn_info()

# Uvicorn server config
server_config = get_server_config()
