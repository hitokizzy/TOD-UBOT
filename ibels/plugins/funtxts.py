import nekos

from ibels import ibel

from ..core.managers import edit_or_reply

plugin_category = "fun"


@ibel.sad_cmd(
    pattern="tsad$",
    command=("tsad", plugin_category),
    info={
        "header": "Some random ibel facial text art",
        "usage": "{tr}tsad",
    },
)
async def hmm(ibel):
    "Some random ibel facial text art"
    reactsad = nekos.textsad()
    await edit_or_reply(ibel, reactsad)


@ibel.sad_cmd(
    pattern="why$",
    command=("why", plugin_category),
    info={
        "header": "Sends you some random Funny questions",
        "usage": "{tr}why",
    },
)
async def hmm(ibel):
    "Some random Funny questions"
    whysad = nekos.why()
    await edit_or_reply(ibel, whysad)


@ibel.sad_cmd(
    pattern="fact$",
    command=("fact", plugin_category),
    info={
        "header": "Sends you some random facts",
        "usage": "{tr}fact",
    },
)
async def hmm(ibel):
    "Some random facts"
    factsad = nekos.fact()
    await edit_or_reply(ibel, factsad)
