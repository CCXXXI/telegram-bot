from aiocqhttp import Event
from nonebot import get_bot
from nonebot import on_notice, NoticeSession

from config import dalao_delta_groups

bot = get_bot()
dalao_delta_nums = dict()
for gid_ in dalao_delta_groups:
    dalao_delta_nums[gid_] = 0


@on_notice('group_increase')
async def dalao_more(session: NoticeSession):
    if (gid := session.event.group_id) in dalao_delta_groups:
        dalao_delta_nums[gid] += 1


@on_notice('group_decrease')
async def dalao_less(session: NoticeSession):
    if (gid := session.event.group_id) in dalao_delta_groups:
        dalao_delta_nums[gid] -= 1


@bot.on_meta_event('heartbeat')
async def dalao_delta_print(event: Event):
    for gid in dalao_delta_groups:
        if (delta := dalao_delta_nums[gid]) != 0:
            dalao_delta_nums[gid] = 0
            await bot.send_group_msg(group_id=gid, message=f'群大佬{delta:+}')
