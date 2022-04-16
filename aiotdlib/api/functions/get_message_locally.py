# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetMessageLocally(BaseObject):
    """
    Returns information about a message, if it is available without sending network request. This is an offline request
    
    :param chat_id: Identifier of the chat the message belongs to
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the message to get
    :type message_id: :class:`int`
    
    """

    ID: str = Field("getMessageLocally", alias="@type")
    chat_id: int
    message_id: int

    @staticmethod
    def read(q: dict) -> GetMessageLocally:
        return GetMessageLocally.construct(**q)
