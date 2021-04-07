# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetMessageLink(BaseObject):
    """
    Returns an HTTPS link to a message in a chat. Available only for already sent messages in supergroups and channels. This is an offline request
    
    Params:
        chat_id (:class:`int`)
            Identifier of the chat to which the message belongs
        
        message_id (:class:`int`)
            Identifier of the message
        
        for_album (:class:`bool`)
            Pass true to create a link for the whole media album
        
        for_comment (:class:`bool`)
            Pass true to create a link to the message as a channel post comment, or from a message thread
        
    """

    ID: str = Field("getMessageLink", alias="@type")
    chat_id: int
    message_id: int
    for_album: bool
    for_comment: bool

    @staticmethod
    def read(q: dict) -> GetMessageLink:
        return GetMessageLink.construct(**q)
