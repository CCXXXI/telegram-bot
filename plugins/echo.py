from telegram import Update
from telegram.ext import CallbackContext

from plugin_tools import add_cmd


def echo(update: Update, context: CallbackContext):
    update.message.reply_text(' '.join(context.args))


add_cmd('echo', echo)
