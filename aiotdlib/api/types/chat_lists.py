# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .chat_list import ChatList
from ..base_object import BaseObject


class ChatLists(BaseObject):
    """
    Contains a list of chat lists
    
    Params:
        chat_lists (:obj:`list[ChatList]`)
            List of chat lists
        
    """

    ID: str = Field("chatLists", alias="@type")
    chat_lists: list[ChatList]

    @staticmethod
    def read(q: dict) -> ChatLists:
        return ChatLists.construct(**q)
