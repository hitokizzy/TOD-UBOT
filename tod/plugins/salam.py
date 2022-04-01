import asyncio

from . import edit_or_reply, tod

plugin_category = "extra"


@tod.tod_cmd(
    pattern="as$",
    command=("as", plugin_category),
    info={
        "header": "salam.",
        "usage": "{tr}as",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "as")
    await event.edit("yuuhuuuu")
    await asyncio.sleep(1)
    await event.edit("Assalamualaikum wr. wb.")


@tod.tod_cmd(
    pattern="ws$",
    command=("ws", plugin_category),
    info={
        "header": "answer the salam.",
        "usage": "{tr}ws",
    },
)
async def _(event):
    "animation command"
    event = await edit_or_reply(event, "ws")
    await event.edit("huuyyyy")
    await asyncio.sleep(1)
    await event.edit("Waalaikum salam wr. wb.")
