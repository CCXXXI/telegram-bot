import re
from ast import literal_eval

from nonebot import on_command, CommandSession

from config import group_white_list, user_white_list


@on_command('echo')
async def echo(session: CommandSession):
    if session.event.group_id in group_white_list or session.event.user_id in user_white_list:
        await session.send(session.current_arg_text)
    else:
        print('来源不明，pass')


@on_command('print')
async def py_print(session: CommandSession):
    if session.event.group_id in group_white_list or session.event.user_id in user_white_list:
        await session.send(safe_eval(session.current_arg_text))
    else:
        print('来源不明，pass')


def safe_eval(x: str):
    if len(x) > 100:
        return '太长啦'
    try:
        return str(literal_eval(x))
    except ValueError as ve:
        if '__import__' in x or '.system' in x:
            return "你也想 __import__('os').system('rm -rf /*') ？"
        e_name = re.search(r'_ast\.(\S+)', ve.args[0]).group(1)
        no_dict = {
            'Name': 'variable',
            'BinOp': 'operator',
            'JoinedStr': 'f-string',
            'Call': 'function',
            'GeneratorExp': 'generator',
            'ListComp': 'list comprehension',
            'SetComp': 'set comprehension',
            'DictComp': 'dict comprehension',
        }
        if e_name in no_dict:
            return f'{no_dict[e_name]} no'
        else:
            return f'{e_name.lower()} no'
    except SyntaxError:
        return 'invalid syntax'
    except TypeError as te:
        return te.args[0]


if __name__ == '__main__':
    while True:
        print(safe_eval(input()))
