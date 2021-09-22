# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import ChatMembersFilter
from ..base_object import BaseObject


class SearchChatMembers(BaseObject):
    """
    Searches for a specified query in the first name, last name and username of the members of a specified chat. Requires administrator rights in channels
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param query: Query to search for
    :type query: :class:`str`
    
    :param limit: The maximum number of users to be returned
    :type limit: :class:`int`
    
    :param filter_: The type of users to return. By default, chatMembersFilterMembers
    :type filter_: :class:`ChatMembersFilter`
    
    """

    ID: str = Field("searchChatMembers", alias="@type")
    chat_id: int
    query: str
    limit: int
    filter_: ChatMembersFilter = Field(..., alias='filter')

    @staticmethod
    def read(q: dict) -> SearchChatMembers:
        return SearchChatMembers.construct(**q)
