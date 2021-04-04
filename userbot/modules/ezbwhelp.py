""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.ezbw$")
async def usit(e):
    await e.edit(
        f"**Hai{DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/e69boys)"
        "\n[Repo](https://github.com/hbreakclub/ezbw)"
        "\n[Instagram](Instagram.com/aliparisp)")


@register(outgoing=True, pattern="^.ezbwvar$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/hbreakclub/ezbw/ezbw/varshelper.txt)")


CMD_HELP.update({
    "ezbwhelper":
    "`.ezbw`\
\nPenjelasan: Bantuan Untuk 𝙚𝙯𝙗𝙬.\
\n`.ezbwvar`\
\nPenjelasan: Untuk Melihat Beberapa Daftar Vars."
})
