from telegram.ext import Updater

import plugin_tools
from config import token

updater = Updater(
    token=token,
    use_context=True)  # `use_context=True` only needed for version 12

plugin_tools.load_plugins()

for cmd in plugin_tools.cmd_list:
    updater.dispatcher.add_handler(cmd)
    print('cmd added:', *cmd.command)

if __name__ == '__main__':
    updater.start_polling()
    print('updater running')
    updater.idle()
