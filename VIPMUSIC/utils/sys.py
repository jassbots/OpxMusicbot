import time

import psutil

from VIPMUSIC.misc import _boot_
from VIPMUSIC.utils.formatters import get_readable_time


async def bot_sys_stats():
    bot_uptime = int(time.time() - _boot_)
    UP = f"{get_readable_time(bot_uptime)}"
    CPU = f"{psutil.cpu_percent(interval=0.5)}%"
    RAM = f"{psutil.virtual_memory().percent}%"
    DISK = f"{psutil.disk_usage('/').percent}%"
    return UP, CPU, RAM, DISK

async def bot_up_time():
    bot_up_time = int(time.time() - _boot_)
    BOT_UP = f"{get_readable_time(bot_up_time)}"
    return BOT_UP
