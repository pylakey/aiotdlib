# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetMessages(BaseObject):
    """
    Returns information about messages. If a message is not found, returns null on the corresponding position of the result
    
    Params:
        chat_id (:class:`int`)
            Identifier of the chat the messages belong to
        
        message_ids (:obj:`list[int]`)
            Identifiers of the messages to get
        
    """

    ID: str = Field("getMessages", alias="@type")
    chat_id: int
    message_ids: list[int]

    @staticmethod
    def read(q: dict) -> GetMessages:
        return GetMessages.construct(**q)
