from enum import IntEnum, auto
from os import listdir, getcwd
from random import choice

from nonebot import on_command, CommandSession

from config import group_white_list, user_white_list
from json_tools import get_conf, set_conf


class GkdMode(IntEnum):
    local = auto()
    forward = auto()


valid_gkd_mode = GkdMode.__members__.keys()


@on_command('set_gkd_mode')
async def set_gkd_mode(session: CommandSession):
    if session.event.group_id in group_white_list or session.event.user_id in user_white_list:
        name = session.current_arg_text
        if name in valid_gkd_mode:
            set_conf('gkd_mode', GkdMode[name])
            await session.send(f'gkd_mode已设定为{name}')
        else:
            await session.send(f'{valid_gkd_mode=}')
    else:
        print('来源不明，pass')


@on_command('gkd')
async def gkd_caller(session: CommandSession):
    if session.event.group_id in group_white_list or session.event.user_id in user_white_list:
        gkd_mode = GkdMode(get_conf('gkd_mode'))
        func_map = {
            GkdMode.local: gkd_local,
            GkdMode.forward: gkd_forward,
        }
        await func_map[gkd_mode](session)
    else:
        print('来源不明，pass')


async def gkd_local(session: CommandSession):
    img_name = choice(listdir('img_gkd'))
    img_path = getcwd() + rf'\img_gkd\{img_name}'
    print(f'{img_path=}')
    msg = f'[CQ:image,file=file:///{img_path}]'
    await session.send(msg)


async def gkd_forward(session: CommandSession):
    await session.send('/不色的图')
