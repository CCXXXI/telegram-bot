import re

from telegram import Update

p = re.compile(r'\s.*', re.S)


def str_arg(update: Update):
    """返回完整的参数字符串，而不是split后的列表"""
    ret = ''
    if res := p.search(update.message.text):
        ret = res.group(0).strip()
    return ret
