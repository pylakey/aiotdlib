# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import CallbackQueryPayload
from ..base_object import BaseObject


class GetCallbackQueryAnswer(BaseObject):
    """
    Sends a callback query to a bot and returns an answer. Returns an error with code 502 if the bot fails to answer the query before the query timeout expires
    
    :param chat_id: Identifier of the chat with the message
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the message from which the query originated
    :type message_id: :class:`int`
    
    :param payload: Query payload
    :type payload: :class:`CallbackQueryPayload`
    
    """

    ID: str = Field("getCallbackQueryAnswer", alias="@type")
    chat_id: int
    message_id: int
    payload: CallbackQueryPayload

    @staticmethod
    def read(q: dict) -> GetCallbackQueryAnswer:
        return GetCallbackQueryAnswer.construct(**q)
