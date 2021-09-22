# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetChat(BaseObject):
    """
    Returns information about a chat by its identifier, this is an offline request if the current user is not a bot
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    """

    ID: str = Field("getChat", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> GetChat:
        return GetChat.construct(**q)
