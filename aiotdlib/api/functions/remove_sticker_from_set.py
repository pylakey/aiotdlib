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


class RemoveStickerFromSet(BaseObject):
    """
    Removes a sticker from the set to which it belongs. The sticker set must be owned by the current user

    :param sticker: Sticker to remove from the set
    :type sticker: :class:`InputFile`
    """

    ID: typing.Literal["removeStickerFromSet"] = Field("removeStickerFromSet", validation_alias="@type", alias="@type")
    sticker: InputFile
