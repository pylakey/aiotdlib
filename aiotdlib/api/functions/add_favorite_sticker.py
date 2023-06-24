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


class AddFavoriteSticker(BaseObject):
    """
    Adds a new sticker to the list of favorite stickers. The new sticker is added to the top of the list. If the sticker was already in the list, it is removed from the list first. Only stickers belonging to a sticker set can be added to this list. Emoji stickers can't be added to favorite stickers

    :param sticker: Sticker file to add
    :type sticker: :class:`InputFile`
    """

    ID: typing.Literal["addFavoriteSticker"] = "addFavoriteSticker"
    sticker: InputFile
