# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetGameHighScores(BaseObject):
    """
    Returns the high scores for a game and some part of the high score table in the range of the specified user; for bots only
    
    Params:
        chat_id (:class:`int`)
            The chat that contains the message with the game
        
        message_id (:class:`int`)
            Identifier of the message
        
        user_id (:class:`int`)
            User identifier
        
    """

    ID: str = Field("getGameHighScores", alias="@type")
    chat_id: int
    message_id: int
    user_id: int

    @staticmethod
    def read(q: dict) -> GetGameHighScores:
        return GetGameHighScores.construct(**q)
