import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", 20718334))
API_HASH = getenv("API_HASH", "4e81464b29d79c58d0ad8a0c55ece4a5")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Umaid:umaid@cluster0.k2yxsvu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 777777))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = int(getenv("LOGGER_ID", -1002078429106))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 5585016974))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/arindam69x/Shukun-music",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/team_society_1")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Pika_Discussion")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "df4340d7535741cf945b1848c20c2fd8")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "5bec438b8cb4495dac757db614c51494")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQFJ9mQAcOb_pbrDY2ll1WAeQDMDEn1HlggUZIfw3BBrV224U0cPlgS8s9NmqBq4Jt0xSs-3UZt3LIBaxAShuSmFHbMsMHwO_AHDDY-7mubNye1ZAkPaKn5Q9-SjPsZo-osTFPVGQM7EzjYzW1-MfUY_3CgzoXwtznLk7tw1qC53pHxss-NdqkNCpByDM8zkhUWCbWnTIWrJUnmhq4Cfinv4tgJhqTXNH0xQHdunECDZF0lFvVxJb0kVRKhjYLcsJ9NvttdzqYuDnqfgZo0bE5SCEz89QN9XmXfDeKVJETLM3bv0q8JScWr0pabMgC4TQFx-isQqTKnRtL3YkWIYN6HwlthVZQAAAAG9uewXAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/96ad3e2e58da9ded5d4ac.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/96ad3e2e58da9ded5d4ac.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/cfa72a62efa7e728197f6.jpg"
STATS_IMG_URL = "https://telegra.ph/file/f0c934035d3c928334a14.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/504de8bd60108a6c188e8.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/504de8bd60108a6c188e8.jpg"
STREAM_IMG_URL = "https://telegra.ph//file/7c896988bd3d0b91b8e46.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph//file/1df85370be3f13663a2d9.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph//file/38124ca6dea236fb7e4ef.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph//file/adf5178b6e62a11b2c402.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph//file/9a258a9e3c9c3b6f61169.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph//file/b3b2e9a46166f3ee1a5cf.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
    )
