# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ToggleChatDefaultDisableNotification(BaseObject):
    """
    Changes the value of the default disable_notification parameter, used when a message is sent to a chat
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param default_disable_notification: New value of default_disable_notification
    :type default_disable_notification: :class:`bool`
    
    """

    ID: str = Field("toggleChatDefaultDisableNotification", alias="@type")
    chat_id: int
    default_disable_notification: bool

    @staticmethod
    def read(q: dict) -> ToggleChatDefaultDisableNotification:
        return ToggleChatDefaultDisableNotification.construct(**q)
