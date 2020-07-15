from nonebot import on_command, CommandSession
import asyncio


@on_command('Problem:')
async def _(session: CommandSession):
    if len(t := session.current_arg_text) > 500:
        t = t.replace('n', '')
        ans = f'/game answer {eval(t)}'
        await session.send(ans)
        await asyncio.sleep(10)
        await session.send('/game earn')
