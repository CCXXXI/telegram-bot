from telegram import Update
from telegram.ext import CallbackContext

from cmd_tools import str_arg
from plugin_tools import on_cmd


# noinspection PyUnusedLocal
@on_cmd
def echo(update: Update, context: CallbackContext):
    t = str_arg(update)
    update.message.reply_text(t if t else '?')
