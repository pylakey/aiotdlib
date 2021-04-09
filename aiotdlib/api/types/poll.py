# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .poll_option import PollOption
from .poll_type import PollType
from ..base_object import BaseObject


class Poll(BaseObject):
    """
    Describes a poll
    
    Params:
        id (:class:`int`)
            Unique poll identifier
        
        question (:class:`str`)
            Poll question; 1-300 characters
        
        options (:obj:`list[PollOption]`)
            List of poll answer options
        
        total_voter_count (:class:`int`)
            Total number of voters, participating in the poll
        
        recent_voter_user_ids (:obj:`list[int]`)
            User identifiers of recent voters, if the poll is non-anonymous
        
        is_anonymous (:class:`bool`)
            True, if the poll is anonymous
        
        type_ (:class:`PollType`)
            Type of the poll
        
        open_period (:class:`int`)
            Amount of time the poll will be active after creation, in seconds
        
        close_date (:class:`int`)
            Point in time (Unix timestamp) when the poll will be automatically closed
        
        is_closed (:class:`bool`)
            True, if the poll is closed
        
    """

    ID: str = Field("poll", alias="@type")
    id: int
    question: str = Field(..., min_length=1, max_length=300)
    options: list[PollOption]
    total_voter_count: int
    recent_voter_user_ids: list[int]
    is_anonymous: bool
    type_: PollType = Field(..., alias='type')
    open_period: int
    close_date: int
    is_closed: bool

    @staticmethod
    def read(q: dict) -> Poll:
        return Poll.construct(**q)
