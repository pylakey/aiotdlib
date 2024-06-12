# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetProfileAccentColor(BaseObject):
    """
    Changes accent color and background custom emoji for profile of the current user; for Telegram Premium users only

    :param profile_accent_color_id: Identifier of the accent color to use for profile; pass -1 if none
    :type profile_accent_color_id: :class:`Int32`
    :param profile_background_custom_emoji_id: Identifier of a custom emoji to be shown on the user's profile photo background; 0 if none, defaults to None
    :type profile_background_custom_emoji_id: :class:`Int64`, optional
    """

    ID: typing.Literal["setProfileAccentColor"] = Field(
        "setProfileAccentColor", validation_alias="@type", alias="@type"
    )
    profile_accent_color_id: Int32
    profile_background_custom_emoji_id: typing.Optional[Int64] = 0
