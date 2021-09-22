# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import ChatAction
from ..base_object import BaseObject


class SendChatAction(BaseObject):
    """
    Sends a notification about user activity in a chat
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param message_thread_id: If not 0, a message thread identifier in which the action was performed
    :type message_thread_id: :class:`int`
    
    :param action: The action description
    :type action: :class:`ChatAction`
    
    """

    ID: str = Field("sendChatAction", alias="@type")
    chat_id: int
    message_thread_id: int
    action: ChatAction

    @staticmethod
    def read(q: dict) -> SendChatAction:
        return SendChatAction.construct(**q)
