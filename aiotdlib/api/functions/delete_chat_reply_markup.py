# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class DeleteChatReplyMarkup(BaseObject):
    """
    Deletes the default reply markup from a chat. Must be called after a one-time keyboard or a ForceReply reply markup has been used. UpdateChatReplyMarkup will be sent if the reply markup will be changed
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param message_id: The message identifier of the used keyboard
    :type message_id: :class:`int`
    
    """

    ID: str = Field("deleteChatReplyMarkup", alias="@type")
    chat_id: int
    message_id: int

    @staticmethod
    def read(q: dict) -> DeleteChatReplyMarkup:
        return DeleteChatReplyMarkup.construct(**q)
