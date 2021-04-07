# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import CallbackQueryPayload


class GetCallbackQueryAnswer(BaseObject):
    """
    Sends a callback query to a bot and returns an answer. Returns an error with code 502 if the bot fails to answer the query before the query timeout expires
    
    Params:
        chat_id (:class:`int`)
            Identifier of the chat with the message
        
        message_id (:class:`int`)
            Identifier of the message from which the query originated
        
        payload (:class:`CallbackQueryPayload`)
            Query payload
        
    """

    ID: str = Field("getCallbackQueryAnswer", alias="@type")
    chat_id: int
    message_id: int
    payload: CallbackQueryPayload

    @staticmethod
    def read(q: dict) -> GetCallbackQueryAnswer:
        return GetCallbackQueryAnswer.construct(**q)
