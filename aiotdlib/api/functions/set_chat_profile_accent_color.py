# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetChatProfileAccentColor(BaseObject):
    """
    Changes accent color and background custom emoji for profile of a supergroup or channel chat. Requires can_change_info administrator right

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param profile_accent_color_id: Identifier of the accent color to use for profile; pass -1 if none. The chat must have at least profileAccentColor.min_supergroup_chat_boost_level for supergroups or profileAccentColor.min_channel_chat_boost_level for channels boost level to pass the corresponding color
    :type profile_accent_color_id: :class:`Int32`
    :param profile_background_custom_emoji_id: Identifier of a custom emoji to be shown on the chat's profile photo background; 0 if none. Use chatBoostLevelFeatures.can_set_profile_background_custom_emoji to check whether a custom emoji can be set, defaults to None
    :type profile_background_custom_emoji_id: :class:`Int64`, optional
    """

    ID: typing.Literal["setChatProfileAccentColor"] = Field(
        "setChatProfileAccentColor", validation_alias="@type", alias="@type"
    )
    chat_id: Int53
    profile_accent_color_id: Int32
    profile_background_custom_emoji_id: typing.Optional[Int64] = 0
