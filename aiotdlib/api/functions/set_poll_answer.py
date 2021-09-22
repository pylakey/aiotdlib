# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SetPollAnswer(BaseObject):
    """
    Changes the user answer to a poll. A poll in quiz mode can be answered only once
    
    :param chat_id: Identifier of the chat to which the poll belongs
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the message containing the poll
    :type message_id: :class:`int`
    
    :param option_ids: 0-based identifiers of answer options, chosen by the user. User can choose more than 1 answer option only is the poll allows multiple answers
    :type option_ids: :class:`list[int]`
    
    """

    ID: str = Field("setPollAnswer", alias="@type")
    chat_id: int
    message_id: int
    option_ids: list[int]

    @staticmethod
    def read(q: dict) -> SetPollAnswer:
        return SetPollAnswer.construct(**q)
