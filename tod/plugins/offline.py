import os
import urllib

from telethon.tl import functions
from tod import tod
from ..core.managers import edit_or_reply, edit_delete
from ..Config import Config
from ..core.logger import logging

eod = edit_delete
eor = edit_or_reply
OFFLINE_TAG = "[ • OFFLINE • ]"
ONLINE_TAG = "[ • ONLINE • ]"
PROFILE_IMAGE = "https://telegra.ph/file/9f0638dbfa028162a8682.jpg"
LOGS = logging.getLogger(__name__)
plugin_category = "fun"

@tod.tod_cmd(
    pattern="offline$",
    command=("offline", plugin_category),
    info={
        "header": "get Offline with pride .",
        "description": "to get Offline.",
        "usage": [
            "{tr}offline",
        ],
    },
)
async def _(event):
    zzy_it = "me"
    zzy = await event.client.get_entity(zzy_it)
    if zzy.first_name.startswith(OFFLINE_TAG):
        await eod(event, "**Already in Offline Mode.**")
        return
    zzy = await eor(event, "**Changing Profile to Offline...**")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    urllib.request.urlretrieve(
        "https://telegra.ph/file/249f27d5b52a87babcb3f.jpg", "donottouch.jpg"
    )
    photo = "donottouch.jpg"
    if photo:
        file = await event.client.upload_file(photo)
        try:
            await event.client(functions.photos.UploadProfilePhotoRequest(file))
        except Exception as e:
            await eod(zzy, str(e))
        else:
            await eod(zzy, "**Changed profile to OffLine.**")
    try:
        os.system("rm -fr donottouch.jpg")
    except Exception as e:
        LOGS.warn(str(e))
    last_name = ""
    first_name = OFFLINE_TAG
    try:
        await event.client(
            functions.account.UpdateProfileRequest(
                last_name=last_name, first_name=first_name
            )
        )
        result = "**`{} {}`\nI am Offline now.**".format(first_name, last_name)
        await eod(zzy, result)
    except Exception as e:
        await eod(zzy, str(e))


@tod.tod_cmd(
    pattern="online$",
    command=("online", plugin_category),
    info={
        "header": "get Online with pride .",
        "description": "to get Online.",
        "usage": [
            "{tr}online",
        ],
    },
)
async def _(event):
    zzy_it = "me"
    zzy = await event.client.get_entity(zzy_it)
    if zzy.first_name.startswith(OFFLINE_TAG):
        await eor(event, "**Changing Profile to Online...**")
    else:
        await eod(event, "**Already Online.**")
        return
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    urllib.request.urlretrieve(PROFILE_IMAGE, "donottouch.jpg")
    photo = "donottouch.jpg"
    if photo:
        file = await event.client.upload_file(photo)
        try:
            await event.client(functions.photos.UploadProfilePhotoRequest(file))
        except Exception as e:
            await eod(zzy, str(e))
        else:
            await eod(zzy, "**Changed profile to Online.**")
    try:
        os.system("rm -fr donottouch.jpg")
    except Exception as e:
        LOGS.warn(str(e))
    first_name = ONLINE_TAG
    last_name = ""
    try:
        await event.client(
            functions.account.UpdateProfileRequest(
                last_name=last_name, first_name=first_name
            )
        )
        result = "**`{} {}`\nI am Online !**".format(first_name, last_name)
        await eod(zzy, result)
    except Exception as e:
        await eod(zzy, str(e))
