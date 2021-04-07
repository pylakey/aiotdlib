# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SearchPublicChat(BaseObject):
    """
    Searches a public chat by its username. Currently only private chats, supergroups and channels can be public. Returns the chat if found; otherwise an error is returned
    
    Params:
        username (:class:`str`)
            Username to be resolved
        
    """

    ID: str = Field("searchPublicChat", alias="@type")
    username: str

    @staticmethod
    def read(q: dict) -> SearchPublicChat:
        return SearchPublicChat.construct(**q)
