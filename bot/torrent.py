import logging
import qbittorrentapi

from config import QBT_HOST, QBT_PORT, QBT_USER, QBT_PASS

logger = logging.getLogger(__name__)

# instantiate a Client using the appropriate WebUI configuration
conn_info = dict(
    host=QBT_HOST,
    port=QBT_PORT,
    username=QBT_USER,
    password=QBT_PASS,
)


class TorrentService:
    def __init__(self):
        self.qbt_client = qbittorrentapi.Client(**conn_info)

    def get_torrents_info(self) -> str:
        return str(self.qbt_client.torrents_info())

    def __enter__(self):
        logger.info("Initializing torrent client")
        try:
            self.qbt_client.auth_log_in()
        except Exception as e:
            logger.error(e)
            raise Exception("Failed to login qbt client", e)
        logger.info(f"qBittorrent: {self.qbt_client.app.version}")
        logger.info(f"qBittorrent Web API: {self.qbt_client.app.web_api_version}")
        logger.info(f"qBittorrent Build Info: {self.qbt_client.app.build_info}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        logger.info("Logging out torrent client")
        try:
            self.qbt_client.auth_log_out()
        except Exception as e:
            logger.error(e)
