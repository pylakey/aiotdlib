# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetCustomEmojiStickers(BaseObject):
    """
    Returns list of custom emoji stickers by their identifiers. Stickers are returned in arbitrary order. Only found stickers are returned

    :param custom_emoji_ids: Identifiers of custom emoji stickers. At most 200 custom emoji stickers can be received simultaneously
    :type custom_emoji_ids: :class:`Vector[Int64]`
    """

    ID: typing.Literal["getCustomEmojiStickers"] = "getCustomEmojiStickers"
    custom_emoji_ids: Vector[Int64]
