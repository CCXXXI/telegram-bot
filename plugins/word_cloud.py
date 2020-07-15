from nonebot import on_command, CommandSession
from config import word_cloud_groups, SUPERUSERS
from nonebot import on_natural_language, NLPSession, IntentCommand
import nonebot
from datetime import date
from os.path import exists
from os import mkdir, getcwd
from create_word_cloud import gen
import asyncio

__plugin_name__ = 'word_cloud'
__plugin_usage__ = '【被动】记录聊天记录，定时生成词云并发送'


@on_command('add_log')
async def add_log_caller(session: CommandSession):
    if (gid := session.event.group_id) in word_cloud_groups:
        add_log(session.current_arg_text, gid)
    elif session.event.user_id in SUPERUSERS:
        add_log(session.current_arg_text, 0)


@on_natural_language(only_to_me=False)
async def catch_all_msg(session: NLPSession):
    if '[CQ:' not in session.msg and '/' not in session.msg:
        return IntentCommand(99.9, 'add_log', current_arg=session.msg)


def add_log(msg: str, gid: int):
    log_dir = f"word_cloud/{str(date.today())}"
    if not exists(log_dir):
        mkdir(log_dir)
    with open(f'{log_dir}/{gid}.txt', 'a', encoding='utf-8') as f:
        f.write(msg + '\n')


@nonebot.scheduler.scheduled_job('cron', hour=23, minute=55)
async def gen_and_send_caller():
    await gen_and_send()


async def gen_and_send():
    log_dir = f"word_cloud/{str(date.today())}"
    full_dir = getcwd() + rf'\word_cloud\{str(date.today())}'
    bot = nonebot.get_bot()
    for gid, text in word_cloud_groups.items():
        await asyncio.sleep(10)
        try:
            line_cnt = 0
            with open(f'{log_dir}/{gid}.txt', encoding='utf-8') as f:
                for _ in f:
                    line_cnt += 1
            if line_cnt > 10:
                gen(f'{log_dir}/{gid}.txt')
                to_send = text + rf'[CQ:image,file=file:///{full_dir}\{gid}.png]'
                await bot.send_group_msg(group_id=gid, message=to_send)
        except FileNotFoundError as e:
            print(e.args, e.filename)


print('词云目录：', getcwd() + rf'\word_cloud\{str(date.today())}')
