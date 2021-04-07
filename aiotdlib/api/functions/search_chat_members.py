# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import ChatMembersFilter


class SearchChatMembers(BaseObject):
    """
    Searches for a specified query in the first name, last name and username of the members of a specified chat. Requires administrator rights in channels
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        query (:class:`str`)
            Query to search for
        
        limit (:class:`int`)
            The maximum number of users to be returned
        
        filter_ (:class:`ChatMembersFilter`)
            The type of users to return. By default, chatMembersFilterMembers
        
    """

    ID: str = Field("searchChatMembers", alias="@type")
    chat_id: int
    query: str
    limit: int
    filter_: ChatMembersFilter = Field(..., alias='filter')

    @staticmethod
    def read(q: dict) -> SearchChatMembers:
        return SearchChatMembers.construct(**q)
