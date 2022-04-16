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
    
    :param chat_id: Identifier of the chat
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the new pinned message
    :type message_id: :class:`int`
    
    :param disable_notification: Pass true to disable notification about the pinned message. Notifications are always disabled in channels and private chats
    :type disable_notification: :class:`bool`
    
    :param only_for_self: Pass true to pin the message only for self; private chats only
    :type only_for_self: :class:`bool`
    
    """

    ID: str = Field("pinChatMessage", alias="@type")
    chat_id: int
    message_id: int
    disable_notification: bool
    only_for_self: bool

    @staticmethod
    def read(q: dict) -> PinChatMessage:
        return PinChatMessage.construct(**q)
