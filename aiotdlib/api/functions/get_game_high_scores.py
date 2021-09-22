# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetGameHighScores(BaseObject):
    """
    Returns the high scores for a game and some part of the high score table in the range of the specified user; for bots only
    
    :param chat_id: The chat that contains the message with the game
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the message
    :type message_id: :class:`int`
    
    :param user_id: User identifier
    :type user_id: :class:`int`
    
    """

    ID: str = Field("getGameHighScores", alias="@type")
    chat_id: int
    message_id: int
    user_id: int

    @staticmethod
    def read(q: dict) -> GetGameHighScores:
        return GetGameHighScores.construct(**q)
