# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import ChatEventLogFilters


class GetChatEventLog(BaseObject):
    """
    Returns a list of service actions taken by chat members and administrators in the last 48 hours. Available only for supergroups and channels. Requires administrator rights. Returns results in reverse chronological order (i. e., in order of decreasing event_id)
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        query (:class:`str`)
            Search query by which to filter events
        
        from_event_id (:class:`int`)
            Identifier of an event from which to return results. Use 0 to get results from the latest events
        
        limit (:class:`int`)
            The maximum number of events to return; up to 100
        
        filters (:class:`ChatEventLogFilters`)
            The types of events to return. By default, all types will be returned
        
        user_ids (:obj:`list[int]`)
            User identifiers by which to filter events. By default, events relating to all users will be returned
        
    """

    ID: str = Field("getChatEventLog", alias="@type")
    chat_id: int
    query: str
    from_event_id: int
    limit: int
    filters: ChatEventLogFilters
    user_ids: list[int]

    @staticmethod
    def read(q: dict) -> GetChatEventLog:
        return GetChatEventLog.construct(**q)
