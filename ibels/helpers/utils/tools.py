import os
from typing import Optional

from moviepy.editor import VideoFileClip
from PIL import Image

from ...core.logger import logging
from ...core.managers import edit_or_reply
from ..tools import media_type
from .utils import runcmd

LOGS = logging.getLogger(__name__)


async def media_to_pic(event, reply, noedits=False):  # sourcery no-metrics
    mediatype = media_type(reply)
    if mediatype not in [
        "Photo",
        "Round Video",
        "Gif",
        "Sticker",
        "Video",
        "Voice",
        "Audio",
        "Document",
    ]:
        return event, None
    if not noedits:
        sadevent = await edit_or_reply(
            event, "`Transfiguration Time! Converting to ....`"
        )

    else:
        sadevent = event
    sadmedia = None
    sadfile = os.path.join("./temp/", "meme.png")
    if os.path.exists(sadfile):
        os.remove(sadfile)
    if mediatype == "Photo":
        sadmedia = await reply.download_media(file="./temp")
        im = Image.open(sadmedia)
        im.save(sadfile)
    elif mediatype in ["Audio", "Voice"]:
        await event.client.download_media(reply, sadfile, thumb=-1)
    elif mediatype == "Sticker":
        sadmedia = await reply.download_media(file="./temp")
        if sadmedia.endswith(".tgs"):
            sadcmd = f"lottie_convert.py --frame 0 -if lottie -of png '{sadmedia}' '{sadfile}'"
            stdout, stderr = (await runcmd(sadcmd))[:2]
            if stderr:
                LOGS.info(stdout + stderr)
        elif sadmedia.endswith(".webp"):
            im = Image.open(sadmedia)
            im.save(sadfile)
    elif mediatype in ["Round Video", "Video", "Gif"]:
        await event.client.download_media(reply, sadfile, thumb=-1)
        if not os.path.exists(sadfile):
            sadmedia = await reply.download_media(file="./temp")
            clip = VideoFileClip(media)
            try:
                clip = clip.save_frame(sadfile, 0.1)
            except Exception:
                clip = clip.save_frame(sadfile, 0)
    elif mediatype == "Document":
        mimetype = reply.document.mime_type
        mtype = mimetype.split("/")
        if mtype[0].lower() == "image":
            sadmedia = await reply.download_media(file="./temp")
            im = Image.open(sadmedia)
            im.save(sadfile)
    if sadmedia and os.path.lexists(sadmedia):
        os.remove(sadmedia)
    if os.path.lexists(sadfile):
        return sadevent, sadfile, mediatype
    return sadevent, None


async def take_screen_shot(
    video_file: str, duration: int, path: str = ""
) -> Optional[str]:
    thumb_image_path = path or os.path.join(
        "./temp/", f"{os.path.basename(video_file)}.jpg"
    )
    command = f"ffmpeg -ss {duration} -i '{video_file}' -vframes 1 '{thumb_image_path}'"
    err = (await runcmd(command))[1]
    if err:
        LOGS.error(err)
    return thumb_image_path if os.path.exists(thumb_image_path) else None
