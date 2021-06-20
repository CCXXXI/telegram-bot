from telegram import Update
from telegram.ext import CallbackContext

from tools.plugin_tools import on_cmd


# noinspection PyUnusedLocal
@on_cmd
def start_(update: Update, context: CallbackContext):
    update.message.reply_text("Started!")
