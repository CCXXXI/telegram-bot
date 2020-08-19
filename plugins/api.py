import logging

import requests
from telegram import Update
from telegram.ext import CallbackContext

from tools.plugin_tools import add_cmd

cmd_api_map = {
    'sucker': 'https://v1.alapi.cn/api/dog?format=text',
}

for cmd, api in cmd_api_map.items():
    # noinspection PyUnusedLocal
    def f(update: Update, context: CallbackContext):
        ret = requests.get(api)
        if ret.status_code == 200 and ret.text:
            msg = ret.text
        else:
            msg = 'api炸啦: ' + api
            logging.info(msg)
        update.message.reply_text(msg)


    add_cmd(cmd, f)
