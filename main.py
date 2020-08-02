from telegram.ext import Updater

from config import cmd_list, token
from plugin_tools import load_plugins

updater = Updater(token=token, use_context=True)  # only needed for version 12

load_plugins()
for cmd in cmd_list:
    updater.dispatcher.add_handler(cmd)

if __name__ == '__main__':
    updater.start_polling()
    updater.idle()
