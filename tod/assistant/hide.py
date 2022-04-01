import json
import os
import re

from telethon.events import CallbackQuery

from tod import tod


@tod.tgbot.on(CallbackQuery(data=re.compile(b"hide_(.*)")))
async def on_plug_in_callback_query_handler(event):
    timestamp = int(event.pattern_match.group(1).decode("UTF-8"))
    if os.path.exists("./tods/hide.txt"):
        jsondata = json.load(open("./tods/hide.txt"))
        try:
            reply_pop_up_alert = jsondata[f"{timestamp}"]["text"]
        except KeyError:
            reply_pop_up_alert = "This message no longer exists in tod server"
    else:
        reply_pop_up_alert = "This message no longer exists "
    await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
