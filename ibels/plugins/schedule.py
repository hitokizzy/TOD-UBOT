from asyncio import sleep

from ibels import ibel

plugin_category = "utils"


@ibel.sad_cmd(
    pattern="schd (\d*) ([\s\S]*)",
    command=("schd", plugin_category),
    info={
        "header": "To schedule a message after given time(in seconds).",
        "usage": "{tr}schd <time_in_seconds>  <message to send>",
        "examples": "{tr}schd 120 hello",
    },
)
async def _(event):
    "To schedule a message after given time"
    ibel = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = ibel[1]
    ttl = int(ibel[0])
    await event.delete()
    await sleep(ttl)
    await event.respond(message)
