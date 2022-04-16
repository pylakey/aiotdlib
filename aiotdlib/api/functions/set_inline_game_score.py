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
    
    :param inline_message_id: Inline message identifier
    :type inline_message_id: :class:`str`
    
    :param edit_message: Pass true to edit the game message to include the current scoreboard
    :type edit_message: :class:`bool`
    
    :param user_id: User identifier
    :type user_id: :class:`int`
    
    :param score: The new score
    :type score: :class:`int`
    
    :param force: Pass true to update the score even if it decreases. If the score is 0, the user will be deleted from the high score table
    :type force: :class:`bool`
    
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
