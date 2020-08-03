from telegram import Update
from telegram.ext import CallbackContext

from plugin_tools import on_cmd


# noinspection PyUnusedLocal
@on_cmd
def help_(update: Update, context: CallbackContext):
    update.message.reply_text('https://github.com/CCXXXI/telegram_bot/tree/master/plugins')
