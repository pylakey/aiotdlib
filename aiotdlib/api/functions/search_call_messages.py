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
    
    :param from_message_id: Identifier of the message from which to search; use 0 to get results from the last message
    :type from_message_id: :class:`int`
    
    :param limit: The maximum number of messages to be returned; up to 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
    :type limit: :class:`int`
    
    :param only_missed: Pass true to search only for messages with missed/declined calls
    :type only_missed: :class:`bool`
    
    """

    ID: str = Field("searchCallMessages", alias="@type")
    from_message_id: int
    limit: int
    only_missed: bool

    @staticmethod
    def read(q: dict) -> SearchCallMessages:
        return SearchCallMessages.construct(**q)
