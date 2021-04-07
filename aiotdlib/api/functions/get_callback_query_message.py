# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetCallbackQueryMessage(BaseObject):
    """
    Returns information about a message with the callback button that originated a callback query; for bots only
    
    Params:
        chat_id (:class:`int`)
            Identifier of the chat the message belongs to
        
        message_id (:class:`int`)
            Message identifier
        
        callback_query_id (:class:`int`)
            Identifier of the callback query
        
    """

    ID: str = Field("getCallbackQueryMessage", alias="@type")
    chat_id: int
    message_id: int
    callback_query_id: int

    @staticmethod
    def read(q: dict) -> GetCallbackQueryMessage:
        return GetCallbackQueryMessage.construct(**q)
