# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .chat_list import ChatList
from .chat_source import ChatSource
from ..base_object import BaseObject


class ChatPosition(BaseObject):
    """
    Describes a position of a chat in a chat list
    
    :param list: The chat list
    :type list: :class:`ChatList`
    
    :param order: A parameter used to determine order of the chat in the chat list. Chats must be sorted by the pair (order, chat.id) in descending order
    :type order: :class:`int`
    
    :param is_pinned: True, if the chat is pinned in the chat list
    :type is_pinned: :class:`bool`
    
    :param source: Source of the chat in the chat list; may be null, defaults to None
    :type source: :class:`ChatSource`, optional
    
    """

    ID: str = Field("chatPosition", alias="@type")
    list: ChatList
    order: int
    is_pinned: bool
    source: typing.Optional[ChatSource] = None

    @staticmethod
    def read(q: dict) -> ChatPosition:
        return ChatPosition.construct(**q)
