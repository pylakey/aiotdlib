# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetPollVoters(BaseObject):
    """
    Returns users voted for the specified option in a non-anonymous polls. For the optimal performance the number of returned users is chosen by the library
    
    Params:
        chat_id (:class:`int`)
            Identifier of the chat to which the poll belongs
        
        message_id (:class:`int`)
            Identifier of the message containing the poll
        
        option_id (:class:`int`)
            0-based identifier of the answer option
        
        offset (:class:`int`)
            Number of users to skip in the result; must be non-negative
        
        limit (:class:`int`)
            The maximum number of users to be returned; must be positive and can't be greater than 50. Fewer users may be returned than specified by the limit, even if the end of the voter list has not been reached
        
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
