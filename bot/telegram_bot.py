import logging

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from torrent import TorrentService

from config import TG_TOKEN

# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


class TelegramBot:
    def __init__(self, torrent_service: TorrentService):
        self.torrent_service = torrent_service

        # Create the Application and pass it your bot's token.
        self.application = Application.builder().token(TG_TOKEN).build()

        # on different commands - answer in Telegram
        self.application.add_handler(CommandHandler("start", self.__start))
        self.application.add_handler(CommandHandler("help", self.__help_command))
        self.application.add_handler(CommandHandler("torrents", self.__torrents))

        # on non command i.e message - echo the message on Telegram
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.__echo))

    def run(self) -> None:
        """Run the bot until the user presses Ctrl-C"""
        logger.info("Running bot application")
        self.application.run_polling(allowed_updates=Update.ALL_TYPES)
        logger.info("Bot application stopped")

    async def __start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a message when the command /start is issued."""
        user = update.effective_user
        await update.message.reply_html(
            rf"Hi {user.mention_html()}!",
            reply_markup=ForceReply(selective=True),
        )

    async def __help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a message when the command /help is issued."""
        await update.message.reply_text("Help!")

    async def __echo(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Echo the user message."""
        await update.message.reply_text(update.message.text)

    async def __torrents(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        info = self.torrent_service.get_torrents_info()
        await update.message.reply_text(info)
