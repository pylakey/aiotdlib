# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SearchContacts(BaseObject):
    """
    Searches for the specified query in the first names, last names and usernames of the known user contacts
    
    Params:
        query (:class:`str`)
            Query to search for; may be empty to return all contacts
        
        limit (:class:`int`)
            The maximum number of users to be returned
        
    """

    ID: str = Field("searchContacts", alias="@type")
    query: str
    limit: int

    @staticmethod
    def read(q: dict) -> SearchContacts:
        return SearchContacts.construct(**q)
