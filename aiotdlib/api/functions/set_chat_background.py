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
    BackgroundType,
    InputBackground,
)


class SetChatBackground(BaseObject):
    """
    Sets the background in a specific chat. Supported only in private and secret chats with non-deleted users, and in chats with sufficient boost level and can_change_info administrator right

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param dark_theme_dimming: Dimming of the background in dark themes, as a percentage; 0-100. Applied only to Wallpaper and Fill types of background
    :type dark_theme_dimming: :class:`Int32`
    :param only_for_self: Pass true to set background only for self; pass false to set background for all chat users. Always false for backgrounds set in boosted chats. Background can be set for both users only by Telegram Premium users and if set background isn't of the type inputBackgroundPrevious
    :type only_for_self: :class:`Bool`
    :param background: The input background to use; pass null to create a new filled or chat theme background, defaults to None
    :type background: :class:`InputBackground`, optional
    :param type_: Background type; pass null to use default background type for the chosen background; backgroundTypeChatTheme isn't supported for private and secret chats. Use chatBoostLevelFeatures.chat_theme_background_count and chatBoostLevelFeatures.can_set_custom_background to check whether the background type can be set in the boosted chat, defaults to None
    :type type_: :class:`BackgroundType`, optional
    """

    ID: typing.Literal["setChatBackground"] = Field("setChatBackground", validation_alias="@type", alias="@type")
    chat_id: Int53
    dark_theme_dimming: Int32
    only_for_self: Bool = False
    background: typing.Optional[InputBackground] = None
    type_: typing.Optional[BackgroundType] = Field(None, alias="type")
