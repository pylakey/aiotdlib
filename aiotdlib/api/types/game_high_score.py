# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GameHighScore(BaseObject):
    """
    Contains one row of the game high score table
    
    :param position: Position in the high score table
    :type position: :class:`int`
    
    :param user_id: User identifier
    :type user_id: :class:`int`
    
    :param score: User score
    :type score: :class:`int`
    
    """

    ID: str = Field("gameHighScore", alias="@type")
    position: int
    user_id: int
    score: int

    @staticmethod
    def read(q: dict) -> GameHighScore:
        return GameHighScore.construct(**q)
