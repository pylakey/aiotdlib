# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetSupergroupCustomEmojiStickerSet(BaseObject):
    """
    Changes the custom emoji sticker set of a supergroup; requires can_change_info administrator right. The chat must have at least chatBoostFeatures.min_custom_emoji_sticker_set_boost_level boost level to pass the corresponding color

    :param supergroup_id: Identifier of the supergroup
    :type supergroup_id: :class:`Int53`
    :param custom_emoji_sticker_set_id: New value of the custom emoji sticker set identifier for the supergroup. Use 0 to remove the custom emoji sticker set in the supergroup
    :type custom_emoji_sticker_set_id: :class:`Int64`
    """

    ID: typing.Literal["setSupergroupCustomEmojiStickerSet"] = Field(
        "setSupergroupCustomEmojiStickerSet", validation_alias="@type", alias="@type"
    )
    supergroup_id: Int53
    custom_emoji_sticker_set_id: Int64
