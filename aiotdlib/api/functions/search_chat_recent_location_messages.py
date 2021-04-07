# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SearchChatRecentLocationMessages(BaseObject):
    """
    Returns information about the recent locations of chat members that were sent to the chat. Returns up to 1 location message per user
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        limit (:class:`int`)
            The maximum number of messages to be returned
        
    """

    ID: str = Field("searchChatRecentLocationMessages", alias="@type")
    chat_id: int
    limit: int

    @staticmethod
    def read(q: dict) -> SearchChatRecentLocationMessages:
        return SearchChatRecentLocationMessages.construct(**q)
