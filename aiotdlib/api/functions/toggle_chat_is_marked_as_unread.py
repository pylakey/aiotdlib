# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ToggleChatIsMarkedAsUnread(BaseObject):
    """
    Changes the marked as unread state of a chat
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        is_marked_as_unread (:class:`bool`)
            New value of is_marked_as_unread
        
    """

    ID: str = Field("toggleChatIsMarkedAsUnread", alias="@type")
    chat_id: int
    is_marked_as_unread: bool

    @staticmethod
    def read(q: dict) -> ToggleChatIsMarkedAsUnread:
        return ToggleChatIsMarkedAsUnread.construct(**q)
