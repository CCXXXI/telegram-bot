from random import randint
from typing import List

from PIL import Image
from telegram import Update
from telegram.ext import CallbackContext

from tools.plugin_tools import on_cmd

solid_pic_path = "temp/solid_pic.png"


@on_cmd
def solid_pic(update: Update, context: CallbackContext):
    gen_solid_pic(context.args)
    update.message.reply_photo(open(solid_pic_path, "rb"))


def gen_solid_pic(args: List[str] = None):
    color = [randint(0, 255) for _ in range(3)]
    size = [randint(11, 231) for _ in range(2)]

    if args:
        for i, v in enumerate(args[:3]):
            try:
                color[i] = int(v, base=0) % 255
            except ValueError:
                continue
        for i, v in enumerate(args[3:]):
            try:
                size[i] = int(v, base=0) % 220 + 11
            except ValueError:
                continue

    img = Image.new("RGB", size=tuple(size), color=tuple(color))
    img.save(solid_pic_path)
