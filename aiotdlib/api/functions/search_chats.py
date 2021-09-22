# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SearchChats(BaseObject):
    """
    Searches for the specified query in the title and username of already known chats, this is an offline request. Returns chats in the order seen in the main chat list
    
    :param query: Query to search for. If the query is empty, returns up to 50 recently found chats
    :type query: :class:`str`
    
    :param limit: The maximum number of chats to be returned
    :type limit: :class:`int`
    
    """

    ID: str = Field("searchChats", alias="@type")
    query: str
    limit: int

    @staticmethod
    def read(q: dict) -> SearchChats:
        return SearchChats.construct(**q)
