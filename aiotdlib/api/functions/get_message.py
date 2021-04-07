# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetMessage(BaseObject):
    """
    Returns information about a message
    
    Params:
        chat_id (:class:`int`)
            Identifier of the chat the message belongs to
        
        message_id (:class:`int`)
            Identifier of the message to get
        
    """

    ID: str = Field("getMessage", alias="@type")
    chat_id: int
    message_id: int

    @staticmethod
    def read(q: dict) -> GetMessage:
        return GetMessage.construct(**q)
