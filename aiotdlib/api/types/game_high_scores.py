# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .game_high_score import GameHighScore
from ..base_object import BaseObject


class GameHighScores(BaseObject):
    """
    Contains a list of game high scores
    
    Params:
        scores (:obj:`list[GameHighScore]`)
            A list of game high scores
        
    """

    ID: str = Field("gameHighScores", alias="@type")
    scores: list[GameHighScore]

    @staticmethod
    def read(q: dict) -> GameHighScores:
        return GameHighScores.construct(**q)
