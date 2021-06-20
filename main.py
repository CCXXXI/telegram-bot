import logging

from telegram.ext import Updater

from config import token
from tools import plugin_tools

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)-5s - %(name)s - %(message)s"
)

updater = Updater(token=token)

plugin_tools.load_plugins()

for cmd in plugin_tools.cmd_list:
    updater.dispatcher.add_handler(cmd)
    logging.info(f"command added: {cmd.command}")

if __name__ == "__main__":
    updater.start_polling()
    logging.info("updater running")
    updater.idle()
