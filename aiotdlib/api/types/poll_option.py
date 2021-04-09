# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class PollOption(BaseObject):
    """
    Describes one answer option of a poll
    
    Params:
        text (:class:`str`)
            Option text; 1-100 characters
        
        voter_count (:class:`int`)
            Number of voters for this option, available only for closed or voted polls
        
        vote_percentage (:class:`int`)
            The percentage of votes for this option; 0-100
        
        is_chosen (:class:`bool`)
            True, if the option was chosen by the user
        
        is_being_chosen (:class:`bool`)
            True, if the option is being chosen by a pending setPollAnswer request
        
    """

    ID: str = Field("pollOption", alias="@type")
    text: str = Field(..., min_length=1, max_length=100)
    voter_count: int
    vote_percentage: int
    is_chosen: bool
    is_being_chosen: bool

    @staticmethod
    def read(q: dict) -> PollOption:
        return PollOption.construct(**q)
