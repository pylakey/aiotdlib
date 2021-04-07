# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class UnpinChatMessage(BaseObject):
    """
    Removes a pinned message from a chat; requires can_pin_messages rights in the group or can_edit_messages rights in the channel
    
    Params:
        chat_id (:class:`int`)
            Identifier of the chat
        
        message_id (:class:`int`)
            Identifier of the removed pinned message
        
    """

    ID: str = Field("unpinChatMessage", alias="@type")
    chat_id: int
    message_id: int

    @staticmethod
    def read(q: dict) -> UnpinChatMessage:
        return UnpinChatMessage.construct(**q)
