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


class GetStickers(BaseObject):
    """
    Returns stickers from the installed sticker sets that correspond to any of the given emoji or can be found by sticker-specific keywords. If the query is non-empty, then favorite, recently used or trending stickers may also be returned

    :param sticker_type: Type of the stickers to return
    :type sticker_type: :class:`StickerType`
    :param query: Search query; a space-separated list of emoji or a keyword prefix. If empty, returns all known installed stickers
    :type query: :class:`String`
    :param limit: The maximum number of stickers to be returned
    :type limit: :class:`Int32`
    :param chat_id: Chat identifier for which to return stickers. Available custom emoji stickers may be different for different chats
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getStickers"] = "getStickers"
    sticker_type: StickerType
    query: String
    limit: Int32
    chat_id: Int53
