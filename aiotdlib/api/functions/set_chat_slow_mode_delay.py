# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SetChatSlowModeDelay(BaseObject):
    """
    Changes the slow mode delay of a chat. Available only for supergroups; requires can_restrict_members rights
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param slow_mode_delay: New slow mode delay for the chat; must be one of 0, 10, 30, 60, 300, 900, 3600
    :type slow_mode_delay: :class:`int`
    
    """

    ID: str = Field("setChatSlowModeDelay", alias="@type")
    chat_id: int
    slow_mode_delay: int

    @staticmethod
    def read(q: dict) -> SetChatSlowModeDelay:
        return SetChatSlowModeDelay.construct(**q)
