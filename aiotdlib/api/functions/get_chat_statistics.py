# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetChatStatistics(BaseObject):
    """
    Returns detailed statistics about a chat. Currently this method can be used only for supergroups and channels. Can be used only if SupergroupFullInfo.can_get_statistics == true
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        is_dark (:class:`bool`)
            Pass true if a dark theme is used by the application
        
    """

    ID: str = Field("getChatStatistics", alias="@type")
    chat_id: int
    is_dark: bool

    @staticmethod
    def read(q: dict) -> GetChatStatistics:
        return GetChatStatistics.construct(**q)
