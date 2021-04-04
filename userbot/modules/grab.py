# imported from github.com/ravana69/PornHub to userbot by @heyworld
# please don't nuke my credits 😓
import logging

from telethon import *

from userbot import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY, bot
from userbot.events import register

normiefont = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
weebyfont = [
    "卂",
    "乃",
    "匚",
    "刀",
    "乇",
    "下",
    "厶",
    "卄",
    "工",
    "丁",
    "长",
    "乚",
    "从",
    "𠘨",
    "口",
    "尸",
    "㔿",
    "尺",
    "丂",
    "丅",
    "凵",
    "リ",
    "山",
    "乂",
    "丫",
    "乙",
]


logger = logging.getLogger(__name__)

thumb_image_path = TEMP_DOWNLOAD_DIRECTORY + "/thumb_image.jpg"


if 1 == 1:
    name = "Profile Photos"
    client = bot


@register(outgoing=True, pattern="^.grab(?: |$)(.*)")
async def potocmd(event):
    """Gets the profile photos of replied users, channels or chats"""
    id = "".join(event.raw_text.split(maxsplit=2)[1:])
    user = await event.get_reply_message()
    chat = event.input_chat
    if user:
        photos = await event.client.get_profile_photos(user.sender)
    else:
        photos = await event.client.get_profile_photos(chat)
    if id.strip() == "":
        try:
            await event.client.send_file(event.chat_id, photos)
        except a:
            photo = await event.client.download_profile_photo(chat)
            await bot.send_file(event.chat_id, photo)
    else:
        try:
            id = int(id)
            if id <= 0:
                await event.edit("`ID number you entered is invalid`")
                return
        except BaseException:
            await event.edit("`lol wtf`")
            return
        if int(id) <= (len(photos)):
            send_photos = await event.client.download_media(photos[id - 1])
            await bot.send_file(event.chat_id, send_photos)
        else:
            await event.edit("`No photo found of that Nigga , now u Die`")
            return


CMD_HELP.update(
    {
        "grab": "`.grab`\
    \nUsage:replay .grab or .grab <count> to grab profile picture."
    }
)
