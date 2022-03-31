import sys
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession
from ..Config import Config
from .client import ibelubotClient
from pytgcalls import PyTgCalls
from telethon.sync import TelegramClient

__version__ = "2.0.0"

loop = None

if Config.STRING_SESSION:
    session = StringSession(str(Config.STRING_SESSION))
else:
    session = "ibelubot"

try:
    ibel = ibelubotClient(
        session=session,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
    call_py = PyTgCalls(ibel)
except Exception as e:
    print(f"STRING_SESSION - {e}")
    sys.exit()



