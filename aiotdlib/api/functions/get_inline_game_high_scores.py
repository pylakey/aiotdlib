# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetInlineGameHighScores(BaseObject):
    """
    Returns game high scores and some part of the high score table in the range of the specified user; for bots only
    
    Params:
        inline_message_id (:class:`str`)
            Inline message identifier
        
        user_id (:class:`int`)
            User identifier
        
    """

    ID: str = Field("getInlineGameHighScores", alias="@type")
    inline_message_id: str
    user_id: int

    @staticmethod
    def read(q: dict) -> GetInlineGameHighScores:
        return GetInlineGameHighScores.construct(**q)
