from os import listdir, getcwd
from random import choice

from nonebot import on_command, CommandSession

from config import group_white_list, user_white_list


@on_command('gkd')
async def gkd_caller(session: CommandSession):
    if session.event.group_id in group_white_list or session.event.user_id in user_white_list:
        await gkd_local(session)
    else:
        print('来源不明，pass')


async def gkd_local(session: CommandSession):
    img_name = choice(listdir('img_gkd'))
    img_path = getcwd() + rf'\img_gkd\{img_name}'
    print(f'{img_path=}')
    msg = f'[CQ:image,file=file:///{img_path}]'
    await session.send(msg)
