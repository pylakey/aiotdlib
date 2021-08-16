# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SearchCallMessages(BaseObject):
    """
    Searches for call messages. Returns the results in reverse chronological order (i. e., in order of decreasing message_id). For optimal performance, the number of returned messages is chosen by TDLib
    
    Params:
        from_message_id (:class:`int`)
            Identifier of the message from which to search; use 0 to get results from the last message
        
        limit (:class:`int`)
            The maximum number of messages to be returned; up to 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
        
        only_missed (:class:`bool`)
            If true, returns only messages with missed calls
        
    """

    ID: str = Field("searchCallMessages", alias="@type")
    from_message_id: int
    limit: int
    only_missed: bool

    @staticmethod
    def read(q: dict) -> SearchCallMessages:
        return SearchCallMessages.construct(**q)
