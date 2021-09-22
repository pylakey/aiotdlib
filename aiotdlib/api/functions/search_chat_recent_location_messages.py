# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SearchChatRecentLocationMessages(BaseObject):
    """
    Returns information about the recent locations of chat members that were sent to the chat. Returns up to 1 location message per user
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param limit: The maximum number of messages to be returned
    :type limit: :class:`int`
    
    """

    ID: str = Field("searchChatRecentLocationMessages", alias="@type")
    chat_id: int
    limit: int

    @staticmethod
    def read(q: dict) -> SearchChatRecentLocationMessages:
        return SearchChatRecentLocationMessages.construct(**q)
