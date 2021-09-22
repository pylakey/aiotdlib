# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetPollVoters(BaseObject):
    """
    Returns users voted for the specified option in a non-anonymous polls. For optimal performance, the number of returned users is chosen by TDLib
    
    :param chat_id: Identifier of the chat to which the poll belongs
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the message containing the poll
    :type message_id: :class:`int`
    
    :param option_id: 0-based identifier of the answer option
    :type option_id: :class:`int`
    
    :param offset: Number of users to skip in the result; must be non-negative
    :type offset: :class:`int`
    
    :param limit: The maximum number of users to be returned; must be positive and can't be greater than 50. For optimal performance, the number of returned users is chosen by TDLib and can be smaller than the specified limit, even if the end of the voter list has not been reached
    :type limit: :class:`int`
    
    """

    ID: str = Field("getPollVoters", alias="@type")
    chat_id: int
    message_id: int
    option_id: int
    offset: int
    limit: int

    @staticmethod
    def read(q: dict) -> GetPollVoters:
        return GetPollVoters.construct(**q)
