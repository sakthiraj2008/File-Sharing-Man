# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

# API ID Anda dari my.telegram.org
API_ID = int("")

# API Hash Anda dari my.telegram.org
API_HASH = ("")

# ID Channel Database
CHANNEL_ID = int("CHANNEL_ID", "")

# NAMA OWNER
OWNER = ("")

# Protect Content
PROTECT_CONTENT = strtobool("False"))

# Heroku Credentials for updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# Custom Repo for updater.
UPSTREAM_BRANCH = ("master")

# Database
DB_URI = ("")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int("0"))
FORCE_SUB_GROUP = int("0"))

TG_BOT_WORKERS = int("4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>I'm N-Toy Files Sharing Bot For My Master.</b>",
)
try:
    ADMINS = [int(x) for x in ("").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram no valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nIf You Want this File You Must Join This Channels\s\n\nIf You Don't Join I'll Not Send Files To You </b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = (None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = strtobool("False"))

# Jangan Dihapus nanti ERROR, HAPUS ID Dibawah ini = TERIMA KONSEKUENSI
# Spoiler KONSEKUENSI-nya Paling CH nya tiba tiba ilang & owner nya gua gban 🤪
ADMINS.extend((7188069786, 1430742022))


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
