import os
from pyrogram import Client, idle

APP_ID = int(os.environ.get("APP_ID", 6))
API_HASH = os.environ.get("API_HASH") or None
SESSION_NAME = os.environ.get("SESSION_NAME", None)

PLUGINS = dict(
    root="tod",
    include=[
        "vc.player"
    ]
)

app = Client(SESSION_NAME, APP_ID, API_HASH)
app.start()
print('Music Module Started')
idle()
app.stop()
print('\nMusic MOdule Stopped')
