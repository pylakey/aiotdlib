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
    Changes the background in a specific chat. Supported only in private and secret chats with non-deleted users

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param dark_theme_dimming: Dimming of the background in dark themes, as a percentage; 0-100
    :type dark_theme_dimming: :class:`Int32`
    :param background: The input background to use; pass null to create a new filled background or to remove the current background, defaults to None
    :type background: :class:`InputBackground`, optional
    :param type_: Background type; pass null to remove the current background, defaults to None
    :type type_: :class:`BackgroundType`, optional
    """

    ID: typing.Literal["setChatBackground"] = "setChatBackground"
    chat_id: Int53
    dark_theme_dimming: Int32
    background: typing.Optional[InputBackground] = None
    type_: typing.Optional[BackgroundType] = Field(None, alias="type")
