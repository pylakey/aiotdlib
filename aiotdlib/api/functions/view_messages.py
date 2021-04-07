# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ViewMessages(BaseObject):
    """
    Informs TDLib that messages are being viewed by the user. Many useful activities depend on whether the messages are currently being viewed or not (e.g., marking messages as read, incrementing a view counter, updating a view counter, removing deleted messages in supergroups and channels)
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        message_thread_id (:class:`int`)
            If not 0, a message thread identifier in which the messages are being viewed
        
        message_ids (:obj:`list[int]`)
            The identifiers of the messages being viewed
        
        force_read (:class:`bool`)
            True, if messages in closed chats should be marked as read by the request
        
    """

    ID: str = Field("viewMessages", alias="@type")
    chat_id: int
    message_thread_id: int
    message_ids: list[int]
    force_read: bool

    @staticmethod
    def read(q: dict) -> ViewMessages:
        return ViewMessages.construct(**q)
