# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import CallProblem


class SendCallRating(BaseObject):
    """
    Sends a call rating
    
    Params:
        call_id (:class:`int`)
            Call identifier
        
        rating (:class:`int`)
            Call rating; 1-5
        
        comment (:class:`str`)
            An optional user comment if the rating is less than 5
        
        problems (:obj:`list[CallProblem]`)
            List of the exact types of problems with the call, specified by the user
        
    """

    ID: str = Field("sendCallRating", alias="@type")
    call_id: int
    rating: int
    comment: str
    problems: list[CallProblem]

    @staticmethod
    def read(q: dict) -> SendCallRating:
        return SendCallRating.construct(**q)
