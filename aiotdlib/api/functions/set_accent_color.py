# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetAccentColor(BaseObject):
    """
    Changes accent color and background custom emoji for the current user; for Telegram Premium users only

    :param accent_color_id: Identifier of the accent color to use
    :type accent_color_id: :class:`Int32`
    :param background_custom_emoji_id: Identifier of a custom emoji to be shown on the reply header and link preview background; 0 if none, defaults to None
    :type background_custom_emoji_id: :class:`Int64`, optional
    """

    ID: typing.Literal["setAccentColor"] = Field("setAccentColor", validation_alias="@type", alias="@type")
    accent_color_id: Int32
    background_custom_emoji_id: typing.Optional[Int64] = 0
