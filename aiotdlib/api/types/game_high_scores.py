# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .game_high_score import GameHighScore
from ..base_object import BaseObject


class GameHighScores(BaseObject):
    """
    Contains a list of game high scores
    
    :param scores: A list of game high scores
    :type scores: :class:`list[GameHighScore]`
    
    """

    ID: str = Field("gameHighScores", alias="@type")
    scores: list[GameHighScore]

    @staticmethod
    def read(q: dict) -> GameHighScores:
        return GameHighScores.construct(**q)
