from random import choice

from telegram import Update
from telegram.ext import CallbackContext

from config import cheater_list
from tools.plugin_tools import on_cmd


# noinspection PyUnusedLocal
@on_cmd
def cheater(update: Update, context: CallbackContext):
    update.message.reply_text(choice(cheater_list))
