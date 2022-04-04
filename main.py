from os import environ
from pyrogram import Client, idle

APP_ID = int(environ["APP_ID"])
API_HASH = environ["API_HASH"]
SESSION_NAME = environ["SESSION_NAME"]

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