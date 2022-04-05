import sys
import tod
from tod import BOTLOG_CHATID, PM_LOGGER_GROUP_ID
from .Config import Config
from .core.logger import logging
from .core.session import tod
from .utils import (
    add_bot_to_logger_group,
    load_plugins,
    setup_bot,
    startupmessage,
    verifyLoggerGroup,
)

LOGS = logging.getLogger("todubot")

#print(tod.__copyright__)
#print("Licensed under the terms of the " + tod.__license__)

cmdhr = Config.COMMAND_HAND_LER

try:
    LOGS.info("Starting tod Userbot")
    tod.loop.run_until_complete(setup_bot())
    LOGS.info("tod Userbot Startup Completed")
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()


class sadcheck:
    def __init__(self):
        self.sucess = True


sadcheck = sadcheck()


async def startup_process():
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print("tod Userbot is officially working.!!!")
    print(
        f"Congratulation, now type {cmdhr}alive to see message if tod Userbot is live\
        \nIf you need assistance, head to https://t.me/Kang_keong17"
    )
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    sadcheck.sucess = True
    #await call_py.start()
    return
    
tod.loop.run_until_complete(startup_process())
#idle()
if len(sys.argv) not in (1, 3, 4):
    tod.disconnect()
else:
    try:
        tod.run_until_disconnected()
    except ConnectionError:
        pass

