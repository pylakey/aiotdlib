# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SearchPublicChat(BaseObject):
    """
    Searches a public chat by its username. Currently only private chats, supergroups and channels can be public. Returns the chat if found; otherwise an error is returned
    
    :param username: Username to be resolved
    :type username: :class:`str`
    
    """

    ID: str = Field("searchPublicChat", alias="@type")
    username: str

    @staticmethod
    def read(q: dict) -> SearchPublicChat:
        return SearchPublicChat.construct(**q)
