import logging
import os
import re

from telegram import Update
from telegram.ext import CallbackContext

# noinspection PyUnresolvedReferences
from tools.cmd_tools import str_arg
from tools.plugin_tools import on_cmd


# noinspection PyUnusedLocal
@on_cmd
def exec_(update: Update, context: CallbackContext):
    # t = str_arg(update)
    # t = safe_exec(t) if t else '?'
    # t = t if t else '?'
    t = "用来放pypy沙盒的服务器没钱续费了……"
    update.message.reply_text(t)


interact_path = "/root/pypy2.7-v7.3.1-src/pypy/sandbox/pypy_interact.py"
sandbox_path = "/root/pypy2.7-v7.3.1-src/pypy/goal/pypy-sandbox"
tmp_path = "/root/web/tmp"
untrusted_file = "/tmp/untrusted.py"
out_file = "test.out"
in_file = "test.in"


def safe_exec(input_code: str) -> str:
    """在pypy沙盒中执行输入代码，然后输出结果"""

    # 执行
    logging.debug("input: " + input_code)
    with open(tmp_path + "/untrusted.py", "w") as f:
        f.write(input_code)
    cmd_prefix = (
        f"pypy {interact_path} --heapsize=256m --timeout=1"
        f" --tmp={tmp_path} {sandbox_path}"
    )
    cmd_suffix = f"<{in_file} &>{out_file}"
    os.system(" ".join((cmd_prefix, untrusted_file, cmd_suffix)))
    with open(out_file) as f:
        ret = f.read(500)
        logging.debug("output: " + ret)

    # 返回结果处理
    er = re.search(r"\w+Error.*", ret)
    if er:
        ret = er.group(0)
        if ret == "MemoryError":
            return "Memory Limit Exceeded"
        return ret

    if ret.startswith("'import site' failed"):
        ret = ret[len("'import site' failed"):]
    ret = re.sub(r"\s+", " ", ret).strip()

    if ret == "[Subprocess killed by SIGTERM]":
        return "Time Limit Exceeded"
    if len(ret) > 100:
        ret = ret[:100] + "【后略】"

    return ret
