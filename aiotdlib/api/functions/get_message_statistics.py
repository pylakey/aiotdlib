# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetMessageStatistics(BaseObject):
    """
    Returns detailed statistics about a message. Can be used only if message.can_get_statistics == true
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param message_id: Message identifier
    :type message_id: :class:`int`
    
    :param is_dark: Pass true if a dark theme is used by the application
    :type is_dark: :class:`bool`
    
    """

    ID: str = Field("getMessageStatistics", alias="@type")
    chat_id: int
    message_id: int
    is_dark: bool

    @staticmethod
    def read(q: dict) -> GetMessageStatistics:
        return GetMessageStatistics.construct(**q)
