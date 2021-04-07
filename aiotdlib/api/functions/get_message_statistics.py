# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetMessageStatistics(BaseObject):
    """
    Returns detailed statistics about a message. Can be used only if Message.can_get_statistics == true
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        message_id (:class:`int`)
            Message identifier
        
        is_dark (:class:`bool`)
            Pass true if a dark theme is used by the application
        
    """

    ID: str = Field("getMessageStatistics", alias="@type")
    chat_id: int
    message_id: int
    is_dark: bool

    @staticmethod
    def read(q: dict) -> GetMessageStatistics:
        return GetMessageStatistics.construct(**q)
