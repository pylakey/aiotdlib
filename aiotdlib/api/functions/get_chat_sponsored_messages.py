# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetChatSponsoredMessages(BaseObject):
    """
    Returns sponsored messages to be shown in a chat; for channel chats only
    
    Params:
        chat_id (:class:`int`)
            Identifier of the chat
        
    """

    ID: str = Field("getChatSponsoredMessages", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> GetChatSponsoredMessages:
        return GetChatSponsoredMessages.construct(**q)
