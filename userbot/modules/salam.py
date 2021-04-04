from platform import uname

from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.P(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "Assalamu'alaikum, Shalom, Om Swastyastu, Namo Buddhaya, Salam Kebajikan."
    )


@register(outgoing=True, pattern="^.p(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Assalamu'alaikum")


@register(outgoing=True, pattern="^.L(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "Wa'alaikumsalam, Shalom, Om Swastyastu, Namo Buddhaya, Salam Kebajikan."
    )


@register(outgoing=True, pattern="^.l(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Wa'alaikumsalam")


@register(outgoing=True, pattern="^.alay(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`mainnya bot, alay`")


@register(outgoing=True, pattern="^warvcg(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**NGAPAIN WAR DI VCG TOLOL? VCG TUH BUAT NGOBROL, NORAK LU SEMENJAK ADA VCG WAR NYA DI VCG BHAHAHA**"
    )


@register(outgoing=True, pattern="^warpp(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**WAR KO HARUS PAKE PP? SITU MAU WAR APA MAU BIKIN KTP? KOSA KATA LU GARING NGENTOT HUEK CUIHH**"
    )


@register(outgoing=True, pattern="^warbadut(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**KOSA KATA LU GAADA YANG LAIN? LUCU KAGA NGEBOSENIN IYA LU BADUT, HIDUP LU DI HUTAN SI TOLOL JADI LAWAKANNYA GITU GITU DOANG**"
    )


@register(outgoing=True, pattern="^warmiskin(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**MENDING LU SEKOLAH DAH, SADAR LU TUH UDAH MISKIN GOBLOK PULA, SEKOLAH GA MAMPU HARUS MINJEM DUIT DULU MAKANYA KOSA KATA LU TERBATAS. INGET KALO LU TUH GOBLOK, LU MISKIN, LU TOLOL, LU JELEK\n\nPERBANYAK KUANTITAS TINGKATKAN KUALITAS HUEK CUIHH**"
    )


CMD_HELP.update(
    {
        "salam": "`.P`\
\nUsage: Untuk Memberi salam.\
\n\n`.L`\
\nUsage: Untuk Menjawab Salam.\
\n\n`.bot`"
    }
)
