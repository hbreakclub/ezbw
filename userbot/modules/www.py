# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import time
from datetime import datetime

from speedtest import Speedtest

from userbot import ALIVE_NAME, CMD_HELP, StartTime
from userbot.events import register


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^.lping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("⚡⚡")
    await pong.edit("__**PING⚡**__")
    await pong.edit("__**PIN⚡G**__")
    await pong.edit("__**PI⚡NG**__")
    await pong.edit("__**P⚡ING**__")
    await pong.edit("__**⚡PING⚡**__")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**⚡ ᴘɪɴɢ ⚡**\n"
        f"⚡ **ᴘɪɴɢ:** "
        f"`%sms` \n"
        f"⚡ **ᴏɴʟɪɴᴇ:** "
        f"`{uptime}` \n" % (duration)
    )


@register(outgoing=True, pattern="^.awping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("`ping`")
    await pong.edit("`pong`")
    await pong.edit("`sepong`")
    await pong.edit("`ahh mantap..`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit("`✧ Crott avv\n✧ %sms`" % (duration))


@register(outgoing=True, pattern="^.ping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("`.`")
    await pong.edit("`..`")
    await pong.edit("`...`")
    await pong.edit("`....`")
    await pong.edit("`𝙚...`")
    await pong.edit("`𝙚𝙯..`")
    await pong.edit("`𝙚𝙯𝙗.`")
    await pong.edit("`𝙚𝙯𝙗𝙬`")
    await pong.edit("`✇ 𝙚𝙯𝙗𝙬`")
    await pong.edit("`✇ㅤㅤㅤㅤ`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"`✇ {ALIVE_NAME}\n✇ %sms`" % (duration))


@register(outgoing=True, pattern="^ping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("`....`ㅤㅤㅤㅤㅤㅤㅤ ㅤ")
    await pong.edit("**ᴜꜱᴇʀ    :**ㅤㅤㅤㅤㅤ  \n`....`")
    await pong.edit("**ᴜꜱᴇʀ    :** \n**ᴘɪɴɢㅤ :**ㅤㅤㅤㅤㅤ  \n`....`")
    await pong.edit("**ᴜꜱᴇʀ    :** \n**ᴘɪɴɢㅤ :** \n**ᴏɴʟɪɴᴇ :**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**ᴜꜱᴇʀ    :** {ALIVE_NAME}\n"
        f"**ᴘɪɴɢㅤ :** `%sms`\n"
        f"**ᴏɴʟɪɴᴇ :** `{uptime}` \n" % (duration)
        )


@register(outgoing=True, pattern="^.sinyal$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Mengecek Sinyal...`")
    await pong.edit("**0% ▒▒▒▒▒▒▒▒▒▒**")
    await pong.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await pong.edit("**40% ████▒▒▒▒▒▒**")
    await pong.edit("**60% ██████▒▒▒▒**")
    await pong.edit("**80% ████████▒▒**")
    await pong.edit("**100% ██████████**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"- 𝙚 𝙯 𝙗 𝙬 -\n"
        f"**• ꜱɪɴʏᴀʟ  :** "
        f"`%sms` \n"
        f"**• ᴏɴʟɪɴᴇ  :** "
        f"`{uptime}` \n"
        f"**• ᴏᴡɴᴇʀ  :** `{ALIVE_NAME}`" % (duration)
    )


@register(outgoing=True, pattern="^.speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Menjalankan Tes Kecepatan Tinggi...🚀`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit(
        "**Hasil Tes:\n**"
        "❃ **Dimulai Pada:** "
        f"`{result['timestamp']}` \n"
        f" **━━━━━━━━━━━━━━━━━**\n\n"
        "❃ **Download:** "
        f"`{speed_convert(result['download'])}` \n"
        "❃ **Upload:** "
        f"`{speed_convert(result['upload'])}` \n"
        "❃ **Ping:** "
        f"`{result['ping']}` \n"
        "❃ **ISP:** "
        f"`{result['client']['isp']}` \n"
        "❃ **BOT:** 𝙚𝙯𝙗𝙬"
    )


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2 ** 10
    zero = 0
    units = {0: "", 1: "Kb/s", 2: "Mb/s", 3: "Gb/s", 4: "Tb/s"}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^.pong$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("`Pong.....🔨`")
    await pong.edit("`Pong....🔨.`")
    await pong.edit("`Pong...🔨..`")
    await pong.edit("`Pong..🔨...`")
    await pong.edit("`Pong.🔨....`")
    await pong.edit("`Pong🔨.....`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit("✘ **Ping!**\n`%sms`" % (duration))


CMD_HELP.update(
    {
        "ping": "`.awping` ; `.lping`\
    \nPenjelasan: Untuk menunjukkan ping bot.\
    \n\n`.speed`\
    \nPenjelasan: Untuk menunjukkan kecepatan.\
    \n\n`.pong`\
    \nPenjelasan: sama kaya perintah ping."
    }
)
CMD_HELP.update(
    {
        "sinyal": "**Modules:** `Sinyal`\
    \n\n**• Perintah :** `.sinyal`\
    \n  ➥ **Penjelasan :** __Untuk melihat sinyal bot__"
    }
)
