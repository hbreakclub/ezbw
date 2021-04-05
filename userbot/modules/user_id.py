from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.getid(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Balas Ke Pesan`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("```Balas Ke Pesan```")
        return
    chat = "@getidsbot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("`Balas Ke Pesan`")
        return
    await event.edit("`↺ Mencari ID.......`")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=186675376)
            )
            await bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("`Bot Sedang Tidak Mood`")
            return
        if response.text.startswith("Forward"):
            await event.edit("`Orang Ini Tidak Mempunyai ID`")
        else:
            await event.edit(f"{response.message.message}")


CMD_HELP.update(
    {"getid": "`.gid`" "\nUsage: Balas Ke Pesan Pengguna Untuk Mendapatkan ID Nya."}
)
