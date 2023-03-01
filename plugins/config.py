import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5890096796:AAGP3-64p7gLIMzARKa6OJ0DinHGbuKzamU")

    API_ID = int(os.environ.get("API_ID", "14782914"))

    API_HASH = os.environ.get("API_HASH",'3aa2fabe1074632cf6e2b01da083a2c6')

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1930954213").split())

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    START_IMG_URL = os.environ.get("START_IMG_URL", "https://telegra.ph/file/e17f42bc195635b668d6d.jpg")

    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "-1001651563551")

    MAX_FILE_SIZE = 419430400091919919199191919919191

    TG_MAX_FILE_SIZE = 4194304000727282828828282882828

    FREE_USER_MAX_FILE_SIZE = 104857600

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    OUO_IO_API_KEY = ""

    MAX_MESSAGE_LENGTH = 4096

    PROCESS_MAX_TIMEOUT = 0

    DEF_WATER_MARK_FILE = "Use this bot @MoviePlaynewbot"

    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://sidhu:20092001@cluster0.zwqdbmf.mongodb.net/?retryWrites=true&w=majority")

    SESSION_NAME = os.environ.get("SESSION_NAME", "URLFILESUPLOADERRBOT")

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", '-1001806753811'))

    LOGGER = logging

    OWNER_ID = int(os.environ.get("OWNER_ID", "1930954213"))

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001651563551")
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "URLFILESUPLOADERRBOT")
