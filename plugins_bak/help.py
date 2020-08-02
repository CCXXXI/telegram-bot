from nonebot import on_command, CommandSession

from config import group_white_list, user_white_list


@on_command('help')
async def show_help(session: CommandSession):
    if session.event.group_id in group_white_list or session.event.user_id in user_white_list:
        await session.send(
            '插件列表：https://github.com/CCXXXI/qq_bot/tree/master/plugins')
    else:
        print('来源不明，pass')
