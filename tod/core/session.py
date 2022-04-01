import sys
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession
from ..Config import Config
from .client import todubotClient


__version__ = "2.0.0"

loop = None

if Config.STRING_SESSION:
    session = StringSession(str(Config.STRING_SESSION))
else:
    session = "todubot"

try:
    tod = todubotClient(
        session=session,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    #call_py = PyTgCalls(tod)
except Exception as e:
    print(f"STRING_SESSION - {e}")
    sys.exit()

tod.tgbot = tgbot = todubotClient(
    session="IbelTgbot",
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    loop=loop,
    app_version=__version__,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
).start(bot_token=Config.TG_BOT_TOKEN)

