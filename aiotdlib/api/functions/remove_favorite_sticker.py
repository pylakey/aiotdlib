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


class RemoveFavoriteSticker(BaseObject):
    """
    Removes a sticker from the list of favorite stickers

    :param sticker: Sticker file to delete from the list
    :type sticker: :class:`InputFile`
    """

    ID: typing.Literal["removeFavoriteSticker"] = "removeFavoriteSticker"
    sticker: InputFile
