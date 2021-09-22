# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ReadAllChatMentions(BaseObject):
    """
    Marks all mentions in a chat as read
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    """

    ID: str = Field("readAllChatMentions", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> ReadAllChatMentions:
        return ReadAllChatMentions.construct(**q)
