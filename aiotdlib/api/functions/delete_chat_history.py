# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class DeleteChatHistory(BaseObject):
    """
    Deletes all messages in the chat. Use Chat.can_be_deleted_only_for_self and Chat.can_be_deleted_for_all_users fields to find whether and how the method can be applied to the chat
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        remove_from_chat_list (:class:`bool`)
            Pass true if the chat should be removed from the chat list
        
        revoke (:class:`bool`)
            Pass true to try to delete chat history for all users
        
    """

    ID: str = Field("deleteChatHistory", alias="@type")
    chat_id: int
    remove_from_chat_list: bool
    revoke: bool

    @staticmethod
    def read(q: dict) -> DeleteChatHistory:
        return DeleteChatHistory.construct(**q)
