from importlib import import_module
from os import listdir

from telegram.ext import CommandHandler

from config import cmd_list


def add_cmd(cmd, func):
    cmd_list.append(CommandHandler(cmd, func))


def load_plugins():
    for filename in listdir('plugins'):
        import_module(f'plugins.{filename[:-3]}')


if __name__ == '__main__':
    load_plugins()
    for test in cmd_list:
        print(*test.command)
