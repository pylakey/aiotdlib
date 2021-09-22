# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import DraftMessage
from ..base_object import BaseObject


class SetChatDraftMessage(BaseObject):
    """
    Changes the draft message in a chat
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param message_thread_id: If not 0, a message thread identifier in which the draft was changed
    :type message_thread_id: :class:`int`
    
    :param draft_message: New draft message; may be null, defaults to None
    :type draft_message: :class:`DraftMessage`, optional
    
    """

    ID: str = Field("setChatDraftMessage", alias="@type")
    chat_id: int
    message_thread_id: int
    draft_message: typing.Optional[DraftMessage] = None

    @staticmethod
    def read(q: dict) -> SetChatDraftMessage:
        return SetChatDraftMessage.construct(**q)
