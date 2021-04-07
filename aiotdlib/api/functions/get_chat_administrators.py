# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetChatAdministrators(BaseObject):
    """
    Returns a list of administrators of the chat with their custom titles
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
    """

    ID: str = Field("getChatAdministrators", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> GetChatAdministrators:
        return GetChatAdministrators.construct(**q)
