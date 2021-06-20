import re
from math import ceil, log

from telegram import Update
from telegram.ext import CallbackContext

from tools.cmd_tools import str_arg
from tools.plugin_tools import on_cmd

p = re.compile(r"\d+")


# noinspection PyUnusedLocal
@on_cmd
def ecnu_(update: Update, context: CallbackContext):
    ab = p.findall(str_arg(update))
    if len(ab) != 2:
        res = "?"
    else:
        a, b = map(int, ab)
        res = str(f(a, b))
    update.message.reply_text(res)


def f(a, b):
    if a <= b:
        return 0
    if b == 0:
        return "?"
    return ceil(5 * (2 * a / b - 1) * log(a - b + 1))
