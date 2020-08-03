from os import listdir
from random import choice

from telegram import Update
from telegram.ext import CallbackContext

from config import img_api_list
from tools.plugin_tools import on_cmd

local_img_path = 'images/'


@on_cmd
def gkd(update: Update, context: CallbackContext):
    if context.args:
        api = img_api_list[hash(tuple(context.args)) % len(img_api_list)]
        update.message.reply_photo(api.get())
    else:
        img_path = local_img_path + choice(listdir(local_img_path))
        update.message.reply_photo(open(img_path, 'rb'))
