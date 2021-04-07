# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SetPollAnswer(BaseObject):
    """
    Changes the user answer to a poll. A poll in quiz mode can be answered only once
    
    Params:
        chat_id (:class:`int`)
            Identifier of the chat to which the poll belongs
        
        message_id (:class:`int`)
            Identifier of the message containing the poll
        
        option_ids (:obj:`list[int]`)
            0-based identifiers of answer options, chosen by the user. User can choose more than 1 answer option only is the poll allows multiple answers
        
    """

    ID: str = Field("setPollAnswer", alias="@type")
    chat_id: int
    message_id: int
    option_ids: list[int]

    @staticmethod
    def read(q: dict) -> SetPollAnswer:
        return SetPollAnswer.construct(**q)
