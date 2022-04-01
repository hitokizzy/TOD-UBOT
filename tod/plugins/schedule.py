from asyncio import sleep

from tod import tod

plugin_category = "utils"


@tod.tod_cmd(
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
    tod = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = tod[1]
    ttl = int(tod[0])
    await event.delete()
    await sleep(ttl)
    await event.respond(message)
