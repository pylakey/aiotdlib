# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class PollOption(BaseObject):
    """
    Describes one answer option of a poll
    
    :param text: Option text; 1-100 characters
    :type text: :class:`str`
    
    :param voter_count: Number of voters for this option, available only for closed or voted polls
    :type voter_count: :class:`int`
    
    :param vote_percentage: The percentage of votes for this option; 0-100
    :type vote_percentage: :class:`int`
    
    :param is_chosen: True, if the option was chosen by the user
    :type is_chosen: :class:`bool`
    
    :param is_being_chosen: True, if the option is being chosen by a pending setPollAnswer request
    :type is_being_chosen: :class:`bool`
    
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
