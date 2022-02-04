# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetMessageAddedReactions(BaseObject):
    """
    Returns reactions added for a message, along with their sender
    
    :param chat_id: Identifier of the chat to which the message belongs
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the message
    :type message_id: :class:`int`
    
    :param reaction: If non-empty, only added reactions with the specified text representation will be returned
    :type reaction: :class:`str`
    
    :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
    :type offset: :class:`str`
    
    :param limit: The maximum number of reactions to be returned; must be positive and can't be greater than 100
    :type limit: :class:`int`
    
    """

    ID: str = Field("getMessageAddedReactions", alias="@type")
    chat_id: int
    message_id: int
    reaction: str
    offset: str
    limit: int

    @staticmethod
    def read(q: dict) -> GetMessageAddedReactions:
        return GetMessageAddedReactions.construct(**q)
