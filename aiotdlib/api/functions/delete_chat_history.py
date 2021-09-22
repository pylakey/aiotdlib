# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class DeleteChatHistory(BaseObject):
    """
    Deletes all messages in the chat. Use chat.can_be_deleted_only_for_self and chat.can_be_deleted_for_all_users fields to find whether and how the method can be applied to the chat
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param remove_from_chat_list: Pass true if the chat should be removed from the chat list
    :type remove_from_chat_list: :class:`bool`
    
    :param revoke: Pass true to try to delete chat history for all users
    :type revoke: :class:`bool`
    
    """

    ID: str = Field("deleteChatHistory", alias="@type")
    chat_id: int
    remove_from_chat_list: bool
    revoke: bool

    @staticmethod
    def read(q: dict) -> DeleteChatHistory:
        return DeleteChatHistory.construct(**q)
