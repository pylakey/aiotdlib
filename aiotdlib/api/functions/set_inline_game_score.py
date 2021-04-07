# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SetInlineGameScore(BaseObject):
    """
    Updates the game score of the specified user in a game; for bots only
    
    Params:
        inline_message_id (:class:`str`)
            Inline message identifier
        
        edit_message (:class:`bool`)
            True, if the message should be edited
        
        user_id (:class:`int`)
            User identifier
        
        score (:class:`int`)
            The new score
        
        force (:class:`bool`)
            Pass true to update the score even if it decreases. If the score is 0, the user will be deleted from the high score table
        
    """

    ID: str = Field("setInlineGameScore", alias="@type")
    inline_message_id: str
    edit_message: bool
    user_id: int
    score: int
    force: bool

    @staticmethod
    def read(q: dict) -> SetInlineGameScore:
        return SetInlineGameScore.construct(**q)
