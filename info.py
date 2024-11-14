import re
import os
from os import environ
from pyrogram import enums
from Script import script
import asyncio
import json
from collections import defaultdict
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', '13305226'))
API_HASH = environ.get('API_HASH', '8cde2475d6b0cb1162b89ebbac71a95d')
BOT_TOKEN = environ.get('BOT_TOKEN', '6375200576:AAH0R5eaR_Tlp7308RF4oXoNI05zkbQhNtA')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1258310642 6577722992').split()]
USERNAME = environ.get('USERNAME', 'https://telegram.me/vis_hnu_bot')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001906470657'))
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002244828029 -1002232982072 -1002154239139 -1002228120220').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://v:v@cluster0.awn6r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_URI2 = environ.get('DATABASE_URI2', "mongodb+srv://v:v@cluster0.xehb2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "vishnu")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'vishnu')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1001906470657'))
QR_CODE = environ.get('QR_CODE', 'https://envs.sh/LR6.jpg')

#this vars is for when heroku or koyeb acc get banned, then change this vars as your file to link bot name
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1001906470657'))
URL = environ.get('URL', '')

# verify system vars
IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1001906470657'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/MalluTVserials/16")
TUTORIAL2 = environ.get("TUTORIAL2", "https://t.me/MalluTVserials/16")
TUTORIAL3 = environ.get("TUTORIAL3", "https://t.me/MalluTVserials/16")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/45a270fc6a0a1c183c614.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "fd85d405b577f2cd524e5d8a185505383d0d4e97")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "inshorturl.com")
SHORTENER_API2 = environ.get("SHORTENER_API2", "fd85d405b577f2cd524e5d8a185505383d0d4e97")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "inshorturl.com")
SHORTENER_API3 = environ.get("SHORTENER_API3", "fd85d405b577f2cd524e5d8a185505383d0d4e97")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "inshorturl.com")
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "36000"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "36000"))

# languages search
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam"]

auth_channel = environ.get('AUTH_CHANNEL', '-1002398203196')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002122722037'))

# bot settings
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '8080')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 600))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', False)
PM_SEARCH = is_enabled('PM_SEARCH', True)
