"""
:project: telegram-onedrive
:author: L-ING
:copyright: (C) 2023 L-ING <hlf01@icloud.com>
:license: MIT, see LICENSE for more details.
"""

from telethon import events
import os
from modules.client import tg_bot
from modules.env import tg_user_name
from modules.utils import check_in_group, check_login


@tg_bot.on(events.NewMessage(pattern="/clearLogs", incoming=True, from_users=tg_user_name))
@check_in_group
@check_login
async def clear_logs_handler(event):
    os.system("rm log")
    await event.respond("Logs cleared")
    raise events.StopPropagation