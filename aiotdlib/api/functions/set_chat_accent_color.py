# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetChatAccentColor(BaseObject):
    """
    Changes accent color and background custom emoji of a channel chat. Requires can_change_info administrator right

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param accent_color_id: Identifier of the accent color to use. The chat must have at least accentColor.min_channel_chat_boost_level boost level to pass the corresponding color
    :type accent_color_id: :class:`Int32`
    :param background_custom_emoji_id: Identifier of a custom emoji to be shown on the reply header and link preview background; 0 if none. Use chatBoostLevelFeatures.can_set_background_custom_emoji to check whether a custom emoji can be set, defaults to None
    :type background_custom_emoji_id: :class:`Int64`, optional
    """

    ID: typing.Literal["setChatAccentColor"] = Field("setChatAccentColor", validation_alias="@type", alias="@type")
    chat_id: Int53
    accent_color_id: Int32
    background_custom_emoji_id: typing.Optional[Int64] = 0
