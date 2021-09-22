# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ViewMessages(BaseObject):
    """
    Informs TDLib that messages are being viewed by the user. Many useful activities depend on whether the messages are currently being viewed or not (e.g., marking messages as read, incrementing a view counter, updating a view counter, removing deleted messages in supergroups and channels)
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param message_thread_id: If not 0, a message thread identifier in which the messages are being viewed
    :type message_thread_id: :class:`int`
    
    :param message_ids: The identifiers of the messages being viewed
    :type message_ids: :class:`list[int]`
    
    :param force_read: True, if messages in closed chats should be marked as read by the request
    :type force_read: :class:`bool`
    
    """

    ID: str = Field("viewMessages", alias="@type")
    chat_id: int
    message_thread_id: int
    message_ids: list[int]
    force_read: bool

    @staticmethod
    def read(q: dict) -> ViewMessages:
        return ViewMessages.construct(**q)
