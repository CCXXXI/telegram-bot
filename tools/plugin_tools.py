from importlib import import_module
from os import listdir
from typing import List

from telegram.ext import CommandHandler

cmd_list: List[CommandHandler] = []


def on_cmd(func):
    """装饰器，用func对应的CommandHandler更新cmd_list"""
    cmd_list.append(CommandHandler(func.__name__.strip('_'), func))
    return func


def load_plugins():
    """遍历import所有plugins，以生成cmd_list"""
    for filename in listdir('plugins'):
        if filename.endswith('.py'):
            import_module(f'plugins.{filename[:-3]}')
