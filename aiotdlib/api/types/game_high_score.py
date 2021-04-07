# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GameHighScore(BaseObject):
    """
    Contains one row of the game high score table
    
    Params:
        position (:class:`int`)
            Position in the high score table
        
        user_id (:class:`int`)
            User identifier
        
        score (:class:`int`)
            User score
        
    """

    ID: str = Field("gameHighScore", alias="@type")
    position: int
    user_id: int
    score: int

    @staticmethod
    def read(q: dict) -> GameHighScore:
        return GameHighScore.construct(**q)
