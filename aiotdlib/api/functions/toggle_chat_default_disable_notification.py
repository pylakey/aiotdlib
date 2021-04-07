# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ToggleChatDefaultDisableNotification(BaseObject):
    """
    Changes the value of the default disable_notification parameter, used when a message is sent to a chat
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        default_disable_notification (:class:`bool`)
            New value of default_disable_notification
        
    """

    ID: str = Field("toggleChatDefaultDisableNotification", alias="@type")
    chat_id: int
    default_disable_notification: bool

    @staticmethod
    def read(q: dict) -> ToggleChatDefaultDisableNotification:
        return ToggleChatDefaultDisableNotification.construct(**q)
