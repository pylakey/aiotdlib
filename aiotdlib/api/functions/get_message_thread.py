# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetMessageThread(BaseObject):
    """
    Returns information about a message thread. Can be used only if message.can_get_message_thread == true
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the message
    :type message_id: :class:`int`
    
    """

    ID: str = Field("getMessageThread", alias="@type")
    chat_id: int
    message_id: int

    @staticmethod
    def read(q: dict) -> GetMessageThread:
        return GetMessageThread.construct(**q)
