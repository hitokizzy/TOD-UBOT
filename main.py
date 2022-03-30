import os
from pyrogram import Client, idle
from ..Config import Config

APP_ID = Config.APP_ID or int(os.environ.get("APP_ID"))
APP_HASH = Config.APP_HASH or str(os.environ.get("APP_HASH"))
SESSION_NAME = Config.SESSION_NAME or os.environ.get("SESSION_NAME")

PLUGINS = dict(
    root="ibels/plugins",
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