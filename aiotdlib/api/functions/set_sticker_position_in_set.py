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


class SetStickerPositionInSet(BaseObject):
    """
    Changes the position of a sticker in the set to which it belongs; for bots only. The sticker set must have been created by the bot

    :param sticker: Sticker
    :type sticker: :class:`InputFile`
    :param position: New position of the sticker in the set, 0-based
    :type position: :class:`Int32`
    """

    ID: typing.Literal["setStickerPositionInSet"] = "setStickerPositionInSet"
    sticker: InputFile
    position: Int32
