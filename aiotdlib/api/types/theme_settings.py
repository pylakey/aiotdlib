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
    
    Params:
        accent_color (:class:`int`)
            Theme accent color in ARGB format
        
        background (:class:`Background`)
            The background to be used in chats; may be null
        
        message_fill (:class:`BackgroundFill`)
            The fill to be used as a background for outgoing messages
        
        animate_message_fill (:class:`bool`)
            If true, the freeform gradient fill needs to be animated on every sent message
        
    """

    ID: str = Field("themeSettings", alias="@type")
    accent_color: int
    background: typing.Optional[Background] = None
    message_fill: BackgroundFill
    animate_message_fill: bool

    @staticmethod
    def read(q: dict) -> ThemeSettings:
        return ThemeSettings.construct(**q)
