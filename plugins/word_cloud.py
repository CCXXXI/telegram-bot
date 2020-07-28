import asyncio
from datetime import date
from os import mkdir, getcwd
from os.path import exists

import nonebot
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand

from config import word_cloud_groups, SUPERUSERS
from word_cloud_tools import gen_word_cloud

msg_black_list = ['[CQ:', '/', '请使用新版手机QQ', '你的QQ暂不支持']


@on_natural_language(only_to_me=False)
async def catch_all_msg(session: NLPSession):
    return IntentCommand(60, 'add_log', current_arg=session.msg)


@on_command('add_log')
async def add_log_caller(session: CommandSession):
    gid, msg = session.event.group_id, session.current_arg_text.strip()
    if gid in word_cloud_groups and len(msg) > 1\
            and all(s not in msg for s in msg_black_list):
        add_log(msg, gid)


def add_log(msg: str, gid: int):
    log_dir = f"word_cloud/{str(date.today())}"
    if not exists(log_dir):
        mkdir(log_dir)
    with open(f'{log_dir}/{gid}.txt', 'a', encoding='utf-8') as f:
        f.write(msg + '\n')


@nonebot.scheduler.scheduled_job('cron',
                                 hour=23,
                                 minute=55,
                                 misfire_grace_time=10)
async def gen_and_send_caller():
    await gen_and_send()


async def gen_and_send():
    log_dir = f"word_cloud/{str(date.today())}"
    full_dir = getcwd() + rf'\word_cloud\{str(date.today())}'
    bot = nonebot.get_bot()
    for gid, text in word_cloud_groups.items():
        try:
            line_cnt = 0
            with open(f'{log_dir}/{gid}.txt', encoding='utf-8') as f:
                for _ in f:
                    line_cnt += 1
            if line_cnt > 30:
                gen_word_cloud(f'{log_dir}/{gid}.txt')
                to_send = text + rf'[CQ:image,file=file:///{full_dir}\{gid}.png]'
            else:
                to_send = '今日无事'
            await bot.send_group_msg(group_id=gid, message=to_send)
            await asyncio.sleep(10)
        except FileNotFoundError as e:
            print(e.args, e.filename)
