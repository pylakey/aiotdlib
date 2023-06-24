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


class SetStickerKeywords(BaseObject):
    """
    Changes the list of keywords of a sticker; for bots only. The sticker must belong to a regular or custom emoji sticker set created by the bot

    :param sticker: Sticker
    :type sticker: :class:`InputFile`
    :param keywords: List of up to 20 keywords with total length up to 64 characters, which can be used to find the sticker
    :type keywords: :class:`Vector[String]`
    """

    ID: typing.Literal["setStickerKeywords"] = "setStickerKeywords"
    sticker: InputFile
    keywords: Vector[String]
