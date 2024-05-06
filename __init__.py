#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = config("21233086", default=None, cast=int)
API_HASH = config("2892db755e485aaf8e55b4b70e8953f6", default=None)
BOT_TOKEN = config("6749483929:AAEh5WwJFEUDe9DXQ-PsibVdZkavDzZtP0o", default=None)
SESSION = config("BQFD_b4AbWZBI8YFXZw_NsoqFtpReuRGAjb7boCz76O3entC9nVnrRSg2RwoDTys_wuJsJWLtQdMqp3WTFZ8m6LS6LFGTwvIm4Czclvt8yUBE9NIMQHqtAWJXSYPHZF893NNOQPl2y1sxfp6nFWLUb87sUzPn9kaBekZIbDFcYDPIKtUvJXM1a9PU5qV5qgSIE_OwXzgum9sl3IuPj62-F1dZGo0SLUHH1cxx1V--dG3FojJRsROhDJ4lzz1QOxQXShxuPduWwezf3Rb_rOmk0RVXWRgOxqOGGBZBVUhVkWEX2aewIdmaxBHnBbLNW9nuiQ8y6R4K7pAQlKqx3bL_3DbncEYzAAAAAGnqYHnAA", default=None)
FORCESUB = config("scammer_ji", default=None)
AUTH = config("7107871207", default=None)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
