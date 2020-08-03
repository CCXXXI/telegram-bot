import re
from ast import literal_eval

from telegram import Update
from telegram.ext import CallbackContext

from tools.cmd_tools import str_arg
from tools.plugin_tools import on_cmd


# noinspection PyUnusedLocal
@on_cmd
def eval_(update: Update, context: CallbackContext):
    t = str_arg(update)
    t = safe_eval(t) if t else '?'
    t = t if t else '?'
    update.message.reply_text(t)


def safe_eval(x: str) -> str:
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
