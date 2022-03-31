from telethon.tl import types
from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import EditGroupCallTitleRequest as settitle
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc
from telethon.utils import get_display_name

from ibels import ibel
from ..core.managers import edit_delete, edit_or_reply

plugin_category = "tools"


async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call, limit=1))
    return xx.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


def vcmention(user):
    full_name = get_display_name(user)
    if not isinstance(user, types.User):
        return full_name
    return f"[{full_name}](tg://user?id={user.id})"


@ibel.sad_cmd(
    pattern="startvc(?:\s|$)([\s\S]*)",
    command=("startvc", plugin_category),
    info={
        "header": "start voice chat group.",
        "description": "To start voice chat group.",
        "usage": "{tr}startvc",
        "note": "admin right required",
    },
)
async def start_voice(c):
    me = await c.client.get_me()
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await edit_delete(c, f"**Sorry {me.first_name} you are not an admin 👮**")
        return
    try:
        await c.client(startvc(c.chat_id))
        await edit_or_reply(c, "`Voice Chat Started...`")
    except Exception as ex:
        await edit_delete(c, f"**ERROR:** `{ex}`")


@ibel.sad_cmd(
    pattern="stopvc(?:\s|$)([\s\S]*)",
    command=("stopvc", plugin_category),
    info={
        "header": "stop/end voice chat group.",
        "description": "To stop/end voice chat group.",
        "usage": "{tr}stopvc",
        "note": "admin right required",
    },
)
async def stop_voice(c):
    me = await c.client.get_me()
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await edit_delete(c, f"**Sorry {me.first_name} you are not an admin 👮**")
        return
    try:
        await c.client(stopvc(await get_call(c)))
        await edit_or_reply(c, "`Voice Chat Stopped...`")
    except Exception as ex:
        await edit_delete(c, f"**ERROR:** `{ex}`")


@ibel.sad_cmd(
    pattern="vcinvite(?:\s|$)([\s\S]*)",
    command=("vcinvite", plugin_category),
    info={
        "header": "inviting someone to voice chat group.",
        "description": "To inviting someone to voice chat group.",
        "usage": "{tr}vcinvite",
        "note": "admin right required",
    },
)
async def _(c):
    zy = await edit_or_reply(c, "`Inviting Members to Voice Chat...`")
    users = []
    z = 0
    async for x in c.client.iter_participants(c.chat_id):
        if not x.bot:
            users.append(x.id)
    anuan = list(user_list(users, 6))
    for p in anuan:
        try:
            await c.client(invitetovc(call=await get_call(c), users=p))
            z += 6
        except BaseException:
            pass
    await zy.edit(f"`{z}` **succesfully invited**")


@ibel.sad_cmd(
    pattern="vctitle(?:\s|$)([\s\S]*)",
    command=("vctitle", plugin_category),
    info={
        "header": "change title of voice chat group.",
        "description": "To change title of voice chat group.",
        "usage": "{tr}vctitle <some text for new title>",
        "note": "admin right required",
    },
)
async def change_title(e):
    title = e.pattern_match.group(1)
    me = await e.client.get_me()
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not title:
        return await edit_delete(e, "**Please input new title**")

    if not admin and not creator:
        await edit_delete(e, f"**sorry {me.first_name} you are not an admin 👮**")
        return
    try:
        await e.client(settitle(call=await get_call(e), title=title.strip()))
        await edit_or_reply(e, f"**title changed** `{title}`")
    except Exception as ex:
        await edit_delete(e, f"**ERROR:** `{ex}`")


# Iraa
