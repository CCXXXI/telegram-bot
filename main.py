from os import path, getcwd

import nonebot

import config

if __name__ == '__main__':
    print(f'{getcwd()=}')
    nonebot.init(config)
    nonebot.load_plugins(path.join(path.dirname(__file__), 'plugins'),
                         'plugins')
    nonebot.run()
