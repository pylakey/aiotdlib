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
    Removes a sticker from the set to which it belongs; for bots only. The sticker set must have been created by the bot

    :param sticker: Sticker
    :type sticker: :class:`InputFile`
    """

    ID: typing.Literal["removeStickerFromSet"] = "removeStickerFromSet"
    sticker: InputFile
