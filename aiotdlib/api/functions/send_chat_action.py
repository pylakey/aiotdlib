# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import ChatAction


class SendChatAction(BaseObject):
    """
    Sends a notification about user activity in a chat
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        message_thread_id (:class:`int`)
            If not 0, a message thread identifier in which the action was performed
        
        action (:class:`ChatAction`)
            The action description
        
    """

    ID: str = Field("sendChatAction", alias="@type")
    chat_id: int
    message_thread_id: int
    action: ChatAction

    @staticmethod
    def read(q: dict) -> SendChatAction:
        return SendChatAction.construct(**q)
