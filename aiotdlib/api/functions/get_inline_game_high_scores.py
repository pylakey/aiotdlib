# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetInlineGameHighScores(BaseObject):
    """
    Returns game high scores and some part of the high score table in the range of the specified user; for bots only
    
    :param inline_message_id: Inline message identifier
    :type inline_message_id: :class:`str`
    
    :param user_id: User identifier
    :type user_id: :class:`int`
    
    """

    ID: str = Field("getInlineGameHighScores", alias="@type")
    inline_message_id: str
    user_id: int

    @staticmethod
    def read(q: dict) -> GetInlineGameHighScores:
        return GetInlineGameHighScores.construct(**q)
