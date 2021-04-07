# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SearchPublicChats(BaseObject):
    """
    Searches public chats by looking for specified query in their username and title. Currently only private chats, supergroups and channels can be public. Returns a meaningful number of results. Returns nothing if the length of the searched username prefix is less than 5. Excludes private chats with contacts and chats from the chat list from the results
    
    Params:
        query (:class:`str`)
            Query to search for
        
    """

    ID: str = Field("searchPublicChats", alias="@type")
    query: str

    @staticmethod
    def read(q: dict) -> SearchPublicChats:
        return SearchPublicChats.construct(**q)
