# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio

from userbot import CMD_HELP
from userbot.events import register

modules = CMD_HELP


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("`â 404 NOT FOUND!`")
            await asyncio.sleep(200)
            await event.delete()
    else:
        await event.edit("ğğ¯ğğ¬")
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\tâ± â â°"
        await event.edit(
            f"ã¤ã¤**ã¤ INFORMASI DYNO ã¤**\n\n**âââââââââââââââââââ**\n"
            f"â°{string}"
            f"\nâââââââââââââââââââ\n"
            f"**Ketik Contoh** `.help afk` **Dengan nama perintah untuk melihat cara menggunakannya.**"
        )
        await asyncio.sleep(1000)
        await event.delete()
