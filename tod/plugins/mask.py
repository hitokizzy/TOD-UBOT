# credits to @mrconfused and @hitokizzy

import os

from telegraph import exceptions, upload_file
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from tod import tod

from ..Config import Config
from ..core.managers import edit_or_reply
from . import awooify, baguette, convert_toimage, iphonex, lolice

plugin_category = "extra"


@tod.tod_cmd(
    pattern="mask$",
    command=("mask", plugin_category),
    info={
        "header": "reply to image to get hazmat suit for that image.",
        "usage": "{tr}mask",
    },
)
async def _(sadbot):
    "Hazmat suit maker"
    reply_message = await sadbot.get_reply_message()
    if not reply_message.media or not reply_message:
        return await edit_or_reply(sadbot, "```reply to media message```")
    chat = "@hazmat_suit_bot"
    if reply_message.sender.bot:
        return await edit_or_reply(sadbot, "```Reply to actual users message.```")
    event = await sadbot.edit("```Processing```")
    async with sadbot.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=905164246)
            )
            await sadbot.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            return await event.edit(
                "```Please unblock @hazmat_suit_bot and try again```"
            )
        if response.text.startswith("Forward"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await sadbot.client.send_file(event.chat_id, response.message.media)
            await event.delete()


@tod.tod_cmd(
    pattern="awooify$",
    command=("awooify", plugin_category),
    info={
        "header": "Check yourself by replying to image.",
        "usage": "{tr}awooify",
    },
)
async def sadbot(sadmemes):
    "replied Image will be face of other image"
    replied = await sadmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await edit_or_reply(sadmemes, "reply to a supported media file")
    if replied.media:
        sadevent = await edit_or_reply(sadmemes, "passing to telegraph...")
    else:
        return await edit_or_reply(sadmemes, "reply to a supported media file")
    download_location = await sadmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await sadevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
        await sadevent.edit("generating image..")
    else:
        os.remove(download_location)
        return await sadevent.edit("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await sadevent.edit("ERROR: " + str(exc))
    tod = f"https://telegra.ph{response[0]}"
    tod = await awooify(tod)
    await sadevent.delete()
    await sadmemes.client.send_file(sadmemes.chat_id, tod, reply_to=replied)


@tod.tod_cmd(
    pattern="lolice$",
    command=("lolice", plugin_category),
    info={
        "header": "image masker check your self by replying to image.",
        "usage": "{tr}lolice",
    },
)
async def sadbot(sadmemes):
    "replied Image will be face of other image"
    replied = await sadmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await edit_or_reply(sadmemes, "reply to a supported media file")
    if replied.media:
        sadevent = await edit_or_reply(sadmemes, "passing to telegraph...")
    else:
        return await edit_or_reply(sadmemes, "reply to a supported media file")
    download_location = await sadmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await sadevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
        await sadevent.edit("generating image..")
    else:
        os.remove(download_location)
        return await sadevent.edit("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await sadevent.edit("ERROR: " + str(exc))
    tod = f"https://telegra.ph{response[0]}"
    tod = await lolice(tod)
    await sadevent.delete()
    await sadmemes.client.send_file(sadmemes.chat_id, tod, reply_to=replied)


@tod.tod_cmd(
    pattern="bun$",
    command=("bun", plugin_category),
    info={
        "header": "reply to image and check yourself.",
        "usage": "{tr}bun",
    },
)
async def sadbot(sadmemes):
    "replied Image will be face of other image"
    replied = await sadmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await edit_or_reply(sadmemes, "reply to a supported media file")
    if replied.media:
        sadevent = await edit_or_reply(sadmemes, "passing to telegraph...")
    else:
        return await edit_or_reply(sadmemes, "reply to a supported media file")
    download_location = await sadmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await sadevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
        await sadevent.edit("generating image..")
    else:
        os.remove(download_location)
        return await sadevent.edit("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await sadevent.edit("ERROR: " + str(exc))
    tod = f"https://telegra.ph{response[0]}"
    tod = await baguette(tod)
    await sadevent.delete()
    await sadmemes.client.send_file(sadmemes.chat_id, tod, reply_to=replied)


@tod.tod_cmd(
    pattern="iphx$",
    command=("iphx", plugin_category),
    info={
        "header": "replied image as iphone x wallpaper.",
        "usage": "{tr}iphx",
    },
)
async def sadbot(sadmemes):
    "replied image as iphone x wallpaper."
    replied = await sadmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await edit_or_reply(sadmemes, "reply to a supported media file")
    if replied.media:
        sadevent = await edit_or_reply(sadmemes, "passing to telegraph...")
    else:
        return await edit_or_reply(sadmemes, "reply to a supported media file")
    download_location = await sadmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await sadevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
        await sadevent.edit("generating image..")
    else:
        os.remove(download_location)
        return await sadevent.edit("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await sadevent.edit("ERROR: " + str(exc))
    tod = f"https://telegra.ph{response[0]}"
    tod = await iphonex(tod)
    await sadevent.delete()
    await sadmemes.client.send_file(sadmemes.chat_id, tod, reply_to=replied)
