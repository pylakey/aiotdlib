# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .poll_option import PollOption
from .poll_type import PollType
from ..base_object import BaseObject


class Poll(BaseObject):
    """
    Describes a poll
    
    :param id: Unique poll identifier
    :type id: :class:`int`
    
    :param question: Poll question; 1-300 characters
    :type question: :class:`str`
    
    :param options: List of poll answer options
    :type options: :class:`list[PollOption]`
    
    :param total_voter_count: Total number of voters, participating in the poll
    :type total_voter_count: :class:`int`
    
    :param recent_voter_user_ids: User identifiers of recent voters, if the poll is non-anonymous
    :type recent_voter_user_ids: :class:`list[int]`
    
    :param is_anonymous: True, if the poll is anonymous
    :type is_anonymous: :class:`bool`
    
    :param type_: Type of the poll
    :type type_: :class:`PollType`
    
    :param open_period: Amount of time the poll will be active after creation, in seconds
    :type open_period: :class:`int`
    
    :param close_date: Point in time (Unix timestamp) when the poll will be automatically closed
    :type close_date: :class:`int`
    
    :param is_closed: True, if the poll is closed
    :type is_closed: :class:`bool`
    
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
