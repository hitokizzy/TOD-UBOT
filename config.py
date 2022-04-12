HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ

    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["APP_ID"])
    API_HASH = environ["API_HASH"]
    SESSION_NAME = environ["SESSION_NAME"]  # Check Readme for session
    ARQ_API_KEY = environ.get("ARQ_API_KEY") or "TLNKJI-TNQJAD-LNAJKJ-WHEHIG-ARQ"
    CHAT_ID = int(environ["CHAT_ID"] or "-1001692751821")
    DEFAULT_SERVICE = environ.get("DEFAULT_SERVICE") or "youtube"
    BITRATE = int(environ["BITRATE"])

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 1234
    API_HASH = ""
    ARQ_API_KEY = "Get this from @ARQRobot"
    CHAT_ID = -100546355432
    DEFAULT_SERVICE = "youtube"  
    BITRATE = 512  # Must be 512/320

# don't make changes below this line
ARQ_API = "https://thearq.tech"
