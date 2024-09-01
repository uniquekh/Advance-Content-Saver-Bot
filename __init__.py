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
API_ID = config("21179966", default=None, cast=int)
API_HASH = config("d97919fb0a3c725e8bb2a25bbb37d57c", default=None)
BOT_TOKEN = config("7341089553:AAEaPugvHtTNnVSwGwSSlKQhGcb4kQ5-GZY", default=None)
SESSION = config("AQFDLj4Ai_JaQIpnzCQGTF5O1Od73W7MG63gk-zfq6jQpXxFvyg07v8BWGRT4DqPV-dkWQxJIF6bMeUcJXltIgHcMDluylZCLJX0FvQsnxVfCpANAvLfEvuC1MSWE3l5FcOpJqrjR6blxnZNvBB8oqEKrZBhPPzDh1_BNVe42j6DgtJXuuTf9mFVQAY38iavcFrnFBHdL4gJgrT_5B_bQdTCIQarA2gnRc-MwbAy6tt98zLoF4TWGc0uXYhz_Fg324GUdjKKJ1fl5NnCV4X6frWZevPO4UMtLCvyUoDSHYBab3gB5BU2cP0h6u0n8cdaQ9d30y3OA4ckiHtSoQ0dUY7x_5FEhAAAAAG0r_Q_AA", default=None)
FORCESUB = config("scammer_ji", default=None)
AUTH = config("7326397503", default=None)
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
