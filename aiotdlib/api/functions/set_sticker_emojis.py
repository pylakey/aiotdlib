# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    InputFile,
)


class SetStickerEmojis(BaseObject):
    """
    Changes the list of emoji corresponding to a sticker; for bots only. The sticker must belong to a regular or custom emoji sticker set created by the bot

    :param sticker: Sticker
    :type sticker: :class:`InputFile`
    :param emojis: New string with 1-20 emoji corresponding to the sticker
    :type emojis: :class:`String`
    """

    ID: typing.Literal["setStickerEmojis"] = "setStickerEmojis"
    sticker: InputFile
    emojis: String
