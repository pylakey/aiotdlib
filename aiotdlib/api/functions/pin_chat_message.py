# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class PinChatMessage(BaseObject):
    """
    Pins a message in a chat; requires can_pin_messages rights or can_edit_messages rights in the channel
    
    Params:
        chat_id (:class:`int`)
            Identifier of the chat
        
        message_id (:class:`int`)
            Identifier of the new pinned message
        
        disable_notification (:class:`bool`)
            True, if there should be no notification about the pinned message. Notifications are always disabled in channels and private chats
        
        only_for_self (:class:`bool`)
            True, if the message needs to be pinned for one side only; private chats only
        
    """

    ID: str = Field("pinChatMessage", alias="@type")
    chat_id: int
    message_id: int
    disable_notification: bool
    only_for_self: bool

    @staticmethod
    def read(q: dict) -> PinChatMessage:
        return PinChatMessage.construct(**q)
