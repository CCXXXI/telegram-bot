import requests
from telegram import Update
from telegram.ext import CallbackContext

from cmd_tools import str_arg
from config import safe_exec_api
from plugin_tools import on_cmd


# noinspection PyUnusedLocal
@on_cmd
def exec_(update: Update, context: CallbackContext):
    t = str_arg(update)
    t = safe_exec(t) if t else '?'
    t = t if t else '?'
    update.message.reply_text(t)


def safe_exec(s: str) -> str:
    ret = requests.get(safe_exec_api + s)
    if ret.status_code == 200 and ret.text:
        return ret.text
    return '?'
