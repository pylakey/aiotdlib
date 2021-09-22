# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ToggleChatIsMarkedAsUnread(BaseObject):
    """
    Changes the marked as unread state of a chat
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param is_marked_as_unread: New value of is_marked_as_unread
    :type is_marked_as_unread: :class:`bool`
    
    """

    ID: str = Field("toggleChatIsMarkedAsUnread", alias="@type")
    chat_id: int
    is_marked_as_unread: bool

    @staticmethod
    def read(q: dict) -> ToggleChatIsMarkedAsUnread:
        return ToggleChatIsMarkedAsUnread.construct(**q)
