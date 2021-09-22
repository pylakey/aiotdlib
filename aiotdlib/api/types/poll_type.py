# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .formatted_text import FormattedText
from ..base_object import BaseObject


class PollType(BaseObject):
    """
    Describes the type of a poll
    
    """

    ID: str = Field("pollType", alias="@type")


class PollTypeQuiz(PollType):
    """
    A poll in quiz mode, which has exactly one correct answer option and can be answered only once
    
    :param correct_option_id: 0-based identifier of the correct answer option; -1 for a yet unanswered poll
    :type correct_option_id: :class:`int`
    
    :param explanation: Text that is shown when the user chooses an incorrect answer or taps on the lamp icon; 0-200 characters with at most 2 line feeds; empty for a yet unanswered poll, defaults to None
    :type explanation: :class:`FormattedText`, optional
    
    """

    ID: str = Field("pollTypeQuiz", alias="@type")
    correct_option_id: int
    explanation: typing.Optional[FormattedText] = None

    @staticmethod
    def read(q: dict) -> PollTypeQuiz:
        return PollTypeQuiz.construct(**q)


class PollTypeRegular(PollType):
    """
    A regular poll
    
    :param allow_multiple_answers: True, if multiple answer options can be chosen simultaneously
    :type allow_multiple_answers: :class:`bool`
    
    """

    ID: str = Field("pollTypeRegular", alias="@type")
    allow_multiple_answers: bool

    @staticmethod
    def read(q: dict) -> PollTypeRegular:
        return PollTypeRegular.construct(**q)
