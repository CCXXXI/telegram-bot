import nonebot
from nonebot import on_command, CommandSession

__plugin_name__ = 'help'
__plugin_usage__ = '命令【help】：不带参数则发送插件列表，否则发送参数对应插件的文档'


@on_command('help')
async def show_help(session: CommandSession):
    plugins = list(filter(lambda p: p.name, nonebot.get_loaded_plugins()))
    arg = session.current_arg_text.strip().lower()
    if not arg:
        await session.send('插件列表：\n' + '\n'.join(p.name for p in plugins))
        return
    for p in plugins:
        if p.name.lower() == arg:
            await session.send(p.usage)
