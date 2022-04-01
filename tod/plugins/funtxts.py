import nekos

from tod import tod

from ..core.managers import edit_or_reply

plugin_category = "fun"


@tod.tod_cmd(
    pattern="tsad$",
    command=("tsad", plugin_category),
    info={
        "header": "Some random tod facial text art",
        "usage": "{tr}tsad",
    },
)
async def hmm(tod):
    "Some random tod facial text art"
    reactsad = nekos.textsad()
    await edit_or_reply(tod, reactsad)


@tod.tod_cmd(
    pattern="why$",
    command=("why", plugin_category),
    info={
        "header": "Sends you some random Funny questions",
        "usage": "{tr}why",
    },
)
async def hmm(tod):
    "Some random Funny questions"
    whysad = nekos.why()
    await edit_or_reply(tod, whysad)


@tod.tod_cmd(
    pattern="fact$",
    command=("fact", plugin_category),
    info={
        "header": "Sends you some random facts",
        "usage": "{tr}fact",
    },
)
async def hmm(tod):
    "Some random facts"
    factsad = nekos.fact()
    await edit_or_reply(tod, factsad)
