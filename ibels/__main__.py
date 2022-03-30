import sys

import ibels
from ibels import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID

from .Config import Config
from .core.logger import logging
from .core.session import ibel
from .utils import (
    add_bot_to_logger_group,
    ipchange,
    load_plugins,
    setup_bot,
    startupmessage,
    verifyLoggerGroup,
)
import os
from pyrogram import Client, idle
from ..Config import Config

LOGS = logging.getLogger("ibelubot")

print(ibels.__copyright__)
print("Licensed under the terms of the " + ibels.__license__)

cmdhr = Config.COMMAND_HAND_LER

try:
    LOGS.info("Starting Ibel's Userbot")
    ibel.loop.run_until_complete(setup_bot())
    LOGS.info("Ibel's Userbot Startup Completed")
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()


class sadcheck:
    def __init__(self):
        self.sucess = True


sadcheck = sadcheck()

APP_ID = Config.APP_ID or int(os.environ.get("APP_ID"))
APP_HASH = Config.APP_HASH or str(os.environ.get("APP_HASH"))
SESSION_NAME = Config.SESSION_NAME or os.environ.get("SESSION_NAME")

PLUGINS = dict(
    root="ibels/plugins",
    include=[
        "player",
    ]
)

app = Client(SESSION_NAME, APP_ID, APP_HASH, plugins=PLUGINS)
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> MUSIC MODULE STARTED')
idle()
app.stop()
print('\n>>> MUSIC MODULE STOPPED')

async def startup_process():
    check = await ipchange()
    if check is not None:
        sadcheck.sucess = False
        return
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print("Ibel's Userbot is officially working.!!!")
    print(
        f"Congratulation, now type {cmdhr}alive to see message if Ibel's Userbot is live\
        \nIf you need assistance, head to https://t.me/Kang_keong17"
    )
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    sadcheck.sucess = True
    return


ibel.loop.run_until_complete(startup_process())


if len(sys.argv) not in (1, 3, 4):
    ibel.disconnect()
elif not sadcheck.sucess:
    if HEROKU_APP is not None:
        HEROKU_APP.restart()
else:
    try:
        ibel.run_until_disconnected()
    except ConnectionError:
        pass
