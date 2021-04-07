# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetMessageEmbeddingCode(BaseObject):
    """
    Returns an HTML code for embedding the message. Available only for messages in supergroups and channels with a username
    
    Params:
        chat_id (:class:`int`)
            Identifier of the chat to which the message belongs
        
        message_id (:class:`int`)
            Identifier of the message
        
        for_album (:class:`bool`)
            Pass true to return an HTML code for embedding of the whole media album
        
    """

    ID: str = Field("getMessageEmbeddingCode", alias="@type")
    chat_id: int
    message_id: int
    for_album: bool

    @staticmethod
    def read(q: dict) -> GetMessageEmbeddingCode:
        return GetMessageEmbeddingCode.construct(**q)
