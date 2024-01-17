import logging
from telegram_bot import TelegramBot
from torrent import TorrentService

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


def main() -> None:
    with TorrentService() as torrent_service:
        bot = TelegramBot(torrent_service)
        bot.run()


if __name__ == "__main__":
    main()
