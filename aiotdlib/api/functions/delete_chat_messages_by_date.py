# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class DeleteChatMessagesByDate(BaseObject):
    """
    Deletes all messages between the specified dates in a chat. Supported only for private chats and basic groups. Messages sent in the last 30 seconds will not be deleted
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param min_date: The minimum date of the messages to delete
    :type min_date: :class:`int`
    
    :param max_date: The maximum date of the messages to delete
    :type max_date: :class:`int`
    
    :param revoke: Pass true to delete chat messages for all users; private chats only
    :type revoke: :class:`bool`
    
    """

    ID: str = Field("deleteChatMessagesByDate", alias="@type")
    chat_id: int
    min_date: int
    max_date: int
    revoke: bool

    @staticmethod
    def read(q: dict) -> DeleteChatMessagesByDate:
        return DeleteChatMessagesByDate.construct(**q)
