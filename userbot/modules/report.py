""" Userbot module for other small commands. """
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.report$")
async def usit(e):
    await e.edit(
        f"**Hai {DEFAULTUSER} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](https://t.me/NightCoreUserbot)"
        "\n[Repo](https://github.com/IrhamFadziilah/NightCore)"
    )


@register(outgoing=True, pattern="^.lordvar$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/IrhamFadzillah/NightCore/nightcore userbot/varshelper.txt)"
    )


CMD_HELP.update(
    {
        "report": "`.report`\
\nUsage: Bantuan Untuk NightCore Userbot.\
\n`.lordvar`\
\nUsage: Melihat Daftar Vars."
    }
)
