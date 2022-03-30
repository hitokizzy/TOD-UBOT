from os import environ
from pyrogram import Client, idle

APP_ID = int(environ["APP_ID"])
APP_HASH = environ["APP_HASH"]
SESSION_NAME = environ["SESSION_NAME"]

PLUGINS = dict(
    root="ibels",
    include=[
        "player",
    ]
)

app = Client(SESSION_NAME, APP_ID, APP_HASH, plugins=PLUGINS)
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> MUSIC MODULE STARTED')
idle()
app.stop()
print('\n>>> MUSIC MODULE STOPPED')