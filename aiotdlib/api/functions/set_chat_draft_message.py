# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject
from ..types import DraftMessage


class SetChatDraftMessage(BaseObject):
    """
    Changes the draft message in a chat
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        message_thread_id (:class:`int`)
            If not 0, a message thread identifier in which the draft was changed
        
        draft_message (:class:`DraftMessage`)
            New draft message; may be null
        
    """

    ID: str = Field("setChatDraftMessage", alias="@type")
    chat_id: int
    message_thread_id: int
    draft_message: typing.Optional[DraftMessage] = None

    @staticmethod
    def read(q: dict) -> SetChatDraftMessage:
        return SetChatDraftMessage.construct(**q)
