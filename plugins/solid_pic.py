from nonebot import on_command, CommandSession
from config import group_white_list, user_white_list
from PIL import Image
from random import randint
from os import getcwd

__plugin_name__ = 'solid_pic'
__plugin_usage__ = '命令【纯色图】：发送随机纯色图片，无可选参数'


def rd():
    return randint(0, 255)


@on_command('纯色图')
async def solid_pic_send(session: CommandSession):
    if session.event.group_id in group_white_list or session.event.user_id in user_white_list:
        img = Image.new('RGB', (231, 231), color=(rd(), rd(), rd()))
        img.save(f'solid_pic_tmp.png')
        await session.send(
            rf'[CQ:image,file=file:///{getcwd()}\solid_pic_tmp.png]')
    else:
        print('来源不明，pass')
