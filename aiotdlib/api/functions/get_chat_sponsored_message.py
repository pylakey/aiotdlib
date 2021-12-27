# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetChatSponsoredMessage(BaseObject):
    """
    Returns sponsored message to be shown in a chat; for channel chats only. Returns a 404 error if there is no sponsored message in the chat
    
    :param chat_id: Identifier of the chat
    :type chat_id: :class:`int`
    
    """

    ID: str = Field("getChatSponsoredMessage", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> GetChatSponsoredMessage:
        return GetChatSponsoredMessage.construct(**q)
