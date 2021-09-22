# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SearchContacts(BaseObject):
    """
    Searches for the specified query in the first names, last names and usernames of the known user contacts
    
    :param query: Query to search for; may be empty to return all contacts
    :type query: :class:`str`
    
    :param limit: The maximum number of users to be returned
    :type limit: :class:`int`
    
    """

    ID: str = Field("searchContacts", alias="@type")
    query: str
    limit: int

    @staticmethod
    def read(q: dict) -> SearchContacts:
        return SearchContacts.construct(**q)
