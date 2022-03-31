from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.exceptions import AlreadyJoinedError
from telethon.utils import get_display_name
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl import types, emoji


from ibels import ibel
from ..core.managers import edit_delete, edit_or_reply
from ..core.session import call_py


plugin_category = "tools"

def vcmention(user):
    full_name = get_display_name(user)
    if not isinstance(user, types.User):
        return full_name
    return f"[{full_name}](tg://user?id={user.id})"


@ibel.sad_cmd(
    pattern="joinvc(?:\s|$)([\s\S]*)",
    command=("joinvc", plugin_category),
    info={
        "header": "for joining voice chat group.",
        "description": "for joining voice chat group.",
        "usage": "{tr}joinvc",
        "note": "Ported from Geez Project",
    },
)
async def join_(event):
    geezav = await edit_or_reply(event, f"**Processing**")
    if len(event.text.split()) > 1:
        chat_id = event.text.split()[1]
        try:
            chat_id = await event.client(GetFullUserRequest(chat_id))
        except Exception as e:
            await edit_delete(event, f"**ERROR:** `{e}`", 30)
    else:
        chat_id = event.chat_id
        await event.get_chat()
        from_user = vcmention(event.sender)
    if chat_id:
        try:
            await call_py.join_group_call(
                chat_id,
                AudioPiped(
                    'http://duramecho.com/Misc/SilentCd/Silence01s.mp3'
                ),
            stream_type=StreamType().pulse_stream,
            )
            await edit_delete(geezav, f"{emoji.CHECK_MARK_BUTTON}**{from_user} Berhasil Naik Ke VC Group!**")
        except AlreadyJoinedError:
            await call_py.leave_group_call(chat_id)
            await edit_delete(
                geezav,
                f"**ERROR:** `Akun Anda Sudah Berada Di VC Group!`\n\n**Noted :** __Silahkan Ketik__ `joinvc` __untuk menggunakan command kembali.__",
                30,
            )
        except Exception as e:
            await geezav.edit(f"**INFO:** `{e}`")

@ibel.sad_cmd(
    pattern="joinvc(?:\s|$)([\s\S]*)",
    command=("joinvc", plugin_category),
    info={
        "header": "for joining voice chat group.",
        "description": "for joining voice chat group.",
        "usage": "{tr}joinvc",
        "note": "Ported from Geez Project",
    },
)
async def leavevc(event):
    geezav = await edit_or_reply(event, "`Processing...`")
    if len(event.text.split()) > 1:
        chat_id = event.text.split()[1]
        try:
            chat_id = await event.client(GetFullUserRequest(chat_id))
        except Exception as e:
            return await geezav.edit(f"**ERROR:** `{e}`")
    else:
        chat_id = event.chat_id
        from_user = vcmention(event.sender)
    if chat_id:
        try:
            await call_py.leave_group_call(chat_id)
            await edit_delete(
                geezav,
                f"{emoji.CHECK_MARK_BUTTON}{from_user} Berhasil Turun Dari VC Group!",
            )
        except Exception as e:
            await geezav.edit(f"**INFO:** `{e}`")
