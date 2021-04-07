# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetAvailableVoiceChatAliases(BaseObject):
    """
    Returns list of user and chat, which can be used as aliases to join a voice chat in the chat
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
    """

    ID: str = Field("getAvailableVoiceChatAliases", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> GetAvailableVoiceChatAliases:
        return GetAvailableVoiceChatAliases.construct(**q)
