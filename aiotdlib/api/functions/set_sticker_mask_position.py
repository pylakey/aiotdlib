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
    Changes the mask position of a mask sticker. The sticker must belong to a mask sticker set that is owned by the current user

    :param sticker: Sticker
    :type sticker: :class:`InputFile`
    :param mask_position: Position where the mask is placed; pass null to remove mask position, defaults to None
    :type mask_position: :class:`MaskPosition`, optional
    """

    ID: typing.Literal["setStickerMaskPosition"] = Field(
        "setStickerMaskPosition", validation_alias="@type", alias="@type"
    )
    sticker: InputFile
    mask_position: typing.Optional[MaskPosition] = None
