from nonebot import on_command, CommandSession
from config import group_white_list, user_white_list
import asyncio

__plugin_name__ = 'forward'
__plugin_usage__ = '命令【exec】【gkd】'


@on_command('exec')
async def exec_forward(session: CommandSession):
    if session.event.group_id in group_white_list or session.event.user_id in user_white_list:
        ret = await session.send(f'/exec {session.current_arg_text}')
        await asyncio.sleep(1)
        await session.bot.delete_msg(message_id=ret['message_id'])
    else:
        print('来源不明，pass')


@on_command('gkd')
async def gkd_forward(session: CommandSession):
    if session.event.group_id in group_white_list or session.event.user_id in user_white_list:
        ret = await session.send('/不色的图')
        await asyncio.sleep(1)
        await session.bot.delete_msg(message_id=ret['message_id'])
    else:
        print('来源不明，pass')
