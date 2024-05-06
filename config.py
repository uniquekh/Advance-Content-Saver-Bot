from os import environ 

class Config:
    API_ID = environ.get("API_ID", "21233086")
    API_HASH = environ.get("API_HASH", "2892db755e485aaf8e55b4b70e8953f6")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6749483929:AAEh5WwJFEUDe9DXQ-PsibVdZkavDzZtP0o") 
    BOT_SESSION = environ.get("BOT_SESSION", "BQFD_b4AbWZBI8YFXZw_NsoqFtpReuRGAjb7boCz76O3entC9nVnrRSg2RwoDTys_wuJsJWLtQdMqp3WTFZ8m6LS6LFGTwvIm4Czclvt8yUBE9NIMQHqtAWJXSYPHZF893NNOQPl2y1sxfp6nFWLUb87sUzPn9kaBekZIbDFcYDPIKtUvJXM1a9PU5qV5qgSIE_OwXzgum9sl3IuPj62-F1dZGo0SLUHH1cxx1V--dG3FojJRsROhDJ4lzz1QOxQXShxuPduWwezf3Rb_rOmk0RVXWRgOxqOGGBZBVUhVkWEX2aewIdmaxBHnBbLNW9nuiQ8y6R4K7pAQlKqx3bL_3DbncEYzAAAAAGnqYHnAA") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6964148334').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
