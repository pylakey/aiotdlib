# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SetGameScore(BaseObject):
    """
    Updates the game score of the specified user in the game; for bots only
    
    Params:
        chat_id (:class:`int`)
            The chat to which the message with the game belongs
        
        message_id (:class:`int`)
            Identifier of the message
        
        edit_message (:class:`bool`)
            True, if the message should be edited
        
        user_id (:class:`int`)
            User identifier
        
        score (:class:`int`)
            The new score
        
        force (:class:`bool`)
            Pass true to update the score even if it decreases. If the score is 0, the user will be deleted from the high score table
        
    """

    ID: str = Field("setGameScore", alias="@type")
    chat_id: int
    message_id: int
    edit_message: bool
    user_id: int
    score: int
    force: bool

    @staticmethod
    def read(q: dict) -> SetGameScore:
        return SetGameScore.construct(**q)
