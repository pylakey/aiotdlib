# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import CallProblem
from ..base_object import BaseObject


class SendCallRating(BaseObject):
    """
    Sends a call rating
    
    :param call_id: Call identifier
    :type call_id: :class:`int`
    
    :param rating: Call rating; 1-5
    :type rating: :class:`int`
    
    :param comment: An optional user comment if the rating is less than 5
    :type comment: :class:`str`
    
    :param problems: List of the exact types of problems with the call, specified by the user
    :type problems: :class:`list[CallProblem]`
    
    """

    ID: str = Field("sendCallRating", alias="@type")
    call_id: int
    rating: int
    comment: str
    problems: list[CallProblem]

    @staticmethod
    def read(q: dict) -> SendCallRating:
        return SendCallRating.construct(**q)
