# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetCallbackQueryMessage(BaseObject):
    """
    Returns information about a message with the callback button that originated a callback query; for bots only
    
    :param chat_id: Identifier of the chat the message belongs to
    :type chat_id: :class:`int`
    
    :param message_id: Message identifier
    :type message_id: :class:`int`
    
    :param callback_query_id: Identifier of the callback query
    :type callback_query_id: :class:`int`
    
    """

    ID: str = Field("getCallbackQueryMessage", alias="@type")
    chat_id: int
    message_id: int
    callback_query_id: int

    @staticmethod
    def read(q: dict) -> GetCallbackQueryMessage:
        return GetCallbackQueryMessage.construct(**q)
