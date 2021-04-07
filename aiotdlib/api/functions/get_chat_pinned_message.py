# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetChatPinnedMessage(BaseObject):
    """
    Returns information about a newest pinned message in the chat
    
    Params:
        chat_id (:class:`int`)
            Identifier of the chat the message belongs to
        
    """

    ID: str = Field("getChatPinnedMessage", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> GetChatPinnedMessage:
        return GetChatPinnedMessage.construct(**q)
