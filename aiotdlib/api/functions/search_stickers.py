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
    StickerType,
)


class SearchStickers(BaseObject):
    """
    Searches for stickers from public sticker sets that correspond to any of the given emoji

    :param sticker_type: Type of the stickers to return
    :type sticker_type: :class:`StickerType`
    :param emojis: Space-separated list of emoji to search for; must be non-empty
    :type emojis: :class:`String`
    :param limit: The maximum number of stickers to be returned; 0-100
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["searchStickers"] = "searchStickers"
    sticker_type: StickerType
    emojis: String
    limit: Int32
