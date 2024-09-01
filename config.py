from os import environ 

class Config:
    API_ID = environ.get("API_ID", "21179966")
    API_HASH = environ.get("API_HASH", "d97919fb0a3c725e8bb2a25bbb37d57c")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7341089553:AAEaPugvHtTNnVSwGwSSlKQhGcb4kQ5-GZY") 
    BOT_SESSION = environ.get("BOT_SESSION", "AQFDLj4Ai_JaQIpnzCQGTF5O1Od73W7MG63gk-zfq6jQpXxFvyg07v8BWGRT4DqPV-dkWQxJIF6bMeUcJXltIgHcMDluylZCLJX0FvQsnxVfCpANAvLfEvuC1MSWE3l5FcOpJqrjR6blxnZNvBB8oqEKrZBhPPzDh1_BNVe42j6DgtJXuuTf9mFVQAY38iavcFrnFBHdL4gJgrT_5B_bQdTCIQarA2gnRc-MwbAy6tt98zLoF4TWGc0uXYhz_Fg324GUdjKKJ1fl5NnCV4X6frWZevPO4UMtLCvyUoDSHYBab3gB5BU2cP0h6u0n8cdaQ9d30y3OA4ckiHtSoQ0dUY7x_5FEhAAAAAG0r_Q_AA") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7326397503').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
