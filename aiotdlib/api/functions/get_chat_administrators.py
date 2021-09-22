# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetChatAdministrators(BaseObject):
    """
    Returns a list of administrators of the chat with their custom titles
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    """

    ID: str = Field("getChatAdministrators", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> GetChatAdministrators:
        return GetChatAdministrators.construct(**q)
