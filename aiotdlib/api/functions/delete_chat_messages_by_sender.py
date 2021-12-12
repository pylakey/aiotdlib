# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import MessageSender


class DeleteChatMessagesBySender(BaseObject):
    """
    Deletes all messages sent by the specified message sender in a chat. Supported only for supergroups; requires can_delete_messages administrator privileges
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param sender_id: Identifier of the sender of messages to delete
    :type sender_id: :class:`MessageSender`
    
    """

    ID: str = Field("deleteChatMessagesBySender", alias="@type")
    chat_id: int
    sender_id: MessageSender

    @staticmethod
    def read(q: dict) -> DeleteChatMessagesBySender:
        return DeleteChatMessagesBySender.construct(**q)
