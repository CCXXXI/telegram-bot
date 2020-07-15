import asyncio
from os import getcwd, listdir
from random import choice
import nonebot
from config import group_white_list

__plugin_name__ = 'img_daily'
__plugin_usage__ = '【被动】每日色图'


@nonebot.scheduler.scheduled_job('cron', hour=10)
async def img_daily_caller():
    await img_daily()


async def img_daily():
    bot = nonebot.get_bot()
    img_name = choice(listdir('img_daily'))
    img_path = getcwd() + rf'\img_daily\{img_name}'
    print(f'{img_path=}')
    for gid in group_white_list:
        await asyncio.sleep(10)
        await bot.send_group_msg(
            group_id=gid, message=f'早安\n[CQ:image,file=file:///{img_path}]')


test_img_path = getcwd() + rf"\img_daily\{choice(listdir('img_daily'))}"
print(f'{test_img_path=}')
