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
    MaskPosition,
)


class SetStickerMaskPosition(BaseObject):
    """
    Changes the mask position of a mask sticker; for bots only. The sticker must belong to a mask sticker set created by the bot

    :param sticker: Sticker
    :type sticker: :class:`InputFile`
    :param mask_position: Position where the mask is placed; pass null to remove mask position, defaults to None
    :type mask_position: :class:`MaskPosition`, optional
    """

    ID: typing.Literal["setStickerMaskPosition"] = "setStickerMaskPosition"
    sticker: InputFile
    mask_position: typing.Optional[MaskPosition] = None
