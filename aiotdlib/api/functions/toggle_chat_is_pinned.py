# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import ChatList


class ToggleChatIsPinned(BaseObject):
    """
    Changes the pinned state of a chat. There can be up to GetOption("pinned_chat_count_max")/GetOption("pinned_archived_chat_count_max") pinned non-secret chats and the same number of secret chats in the main/arhive chat list
    
    Params:
        chat_list (:class:`ChatList`)
            Chat list in which to change the pinned state of the chat
        
        chat_id (:class:`int`)
            Chat identifier
        
        is_pinned (:class:`bool`)
            True, if the chat is pinned
        
    """

    ID: str = Field("toggleChatIsPinned", alias="@type")
    chat_list: ChatList
    chat_id: int
    is_pinned: bool

    @staticmethod
    def read(q: dict) -> ToggleChatIsPinned:
        return ToggleChatIsPinned.construct(**q)
