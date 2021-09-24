# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import ChatList


class AddChatToList(BaseObject):
    """
    Adds a chat to a chat list. A chat can't be simultaneously in Main and Archive chat lists, so it is automatically removed from another one if needed
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param chat_list: The chat list. Use getChatListsToAddChat to get suitable chat lists
    :type chat_list: :class:`ChatList`
    
    """

    ID: str = Field("addChatToList", alias="@type")
    chat_id: int
    chat_list: ChatList

    @staticmethod
    def read(q: dict) -> AddChatToList:
        return AddChatToList.construct(**q)
