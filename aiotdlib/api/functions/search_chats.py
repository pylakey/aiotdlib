# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SearchChats(BaseObject):
    """
    Searches for the specified query in the title and username of already known chats, this is an offline request. Returns chats in the order seen in the main chat list
    
    Params:
        query (:class:`str`)
            Query to search for. If the query is empty, returns up to 20 recently found chats
        
        limit (:class:`int`)
            The maximum number of chats to be returned
        
    """

    ID: str = Field("searchChats", alias="@type")
    query: str
    limit: int

    @staticmethod
    def read(q: dict) -> SearchChats:
        return SearchChats.construct(**q)
