# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .background import Background
from .background_fill import BackgroundFill
from ..base_object import BaseObject


class ThemeSettings(BaseObject):
    """
    Describes theme settings
    
    :param accent_color: Theme accent color in ARGB format
    :type accent_color: :class:`int`
    
    :param background: The background to be used in chats; may be null, defaults to None
    :type background: :class:`Background`, optional
    
    :param outgoing_message_fill: The fill to be used as a background for outgoing messages
    :type outgoing_message_fill: :class:`BackgroundFill`
    
    :param animate_outgoing_message_fill: If true, the freeform gradient fill needs to be animated on every sent message
    :type animate_outgoing_message_fill: :class:`bool`
    
    :param outgoing_message_accent_color: Accent color of outgoing messages in ARGB format
    :type outgoing_message_accent_color: :class:`int`
    
    """

    ID: str = Field("themeSettings", alias="@type")
    accent_color: int
    background: typing.Optional[Background] = None
    outgoing_message_fill: BackgroundFill
    animate_outgoing_message_fill: bool
    outgoing_message_accent_color: int

    @staticmethod
    def read(q: dict) -> ThemeSettings:
        return ThemeSettings.construct(**q)
