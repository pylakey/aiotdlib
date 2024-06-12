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
    Changes the position of a sticker in the set to which it belongs. The sticker set must be owned by the current user

    :param sticker: Sticker
    :type sticker: :class:`InputFile`
    :param position: New position of the sticker in the set, 0-based
    :type position: :class:`Int32`
    """

    ID: typing.Literal["setStickerPositionInSet"] = Field(
        "setStickerPositionInSet", validation_alias="@type", alias="@type"
    )
    sticker: InputFile
    position: Int32
