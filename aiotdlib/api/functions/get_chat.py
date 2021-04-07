# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetChat(BaseObject):
    """
    Returns information about a chat by its identifier, this is an offline request if the current user is not a bot
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
    """

    ID: str = Field("getChat", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> GetChat:
        return GetChat.construct(**q)
