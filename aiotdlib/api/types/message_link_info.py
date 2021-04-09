# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .message import Message
from ..base_object import BaseObject


class MessageLinkInfo(BaseObject):
    """
    Contains information about a link to a message in a chat
    
    Params:
        is_public (:class:`bool`)
            True, if the link is a public link for a message in a chat
        
        chat_id (:class:`int`)
            If found, identifier of the chat to which the message belongs, 0 otherwise
        
        message (:class:`Message`)
            If found, the linked message; may be null
        
        for_album (:class:`bool`)
            True, if the whole media album to which the message belongs is linked
        
        for_comment (:class:`bool`)
            True, if the message is linked as a channel post comment or from a message thread
        
    """

    ID: str = Field("messageLinkInfo", alias="@type")
    is_public: bool
    chat_id: int
    message: typing.Optional[Message] = None
    for_album: bool
    for_comment: bool

    @staticmethod
    def read(q: dict) -> MessageLinkInfo:
        return MessageLinkInfo.construct(**q)
