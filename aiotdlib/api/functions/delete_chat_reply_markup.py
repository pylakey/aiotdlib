# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class DeleteChatReplyMarkup(BaseObject):
    """
    Deletes the default reply markup from a chat. Must be called after a one-time keyboard or a ForceReply reply markup has been used. UpdateChatReplyMarkup will be sent if the reply markup will be changed
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        message_id (:class:`int`)
            The message identifier of the used keyboard
        
    """

    ID: str = Field("deleteChatReplyMarkup", alias="@type")
    chat_id: int
    message_id: int

    @staticmethod
    def read(q: dict) -> DeleteChatReplyMarkup:
        return DeleteChatReplyMarkup.construct(**q)
