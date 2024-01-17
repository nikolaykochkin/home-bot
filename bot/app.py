import asyncio
import logging

from telegram_bot import TelegramBot
from torrent import TorrentService
from api import server

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


async def main() -> None:
    with TorrentService() as torrent_service:
        bot = TelegramBot(torrent_service)
        async with bot.application:
            await bot.start()
            await server.serve()
            await bot.stop()


if __name__ == "__main__":
    asyncio.run(main())
