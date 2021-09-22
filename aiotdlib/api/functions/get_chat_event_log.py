# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import ChatEventLogFilters
from ..base_object import BaseObject


class GetChatEventLog(BaseObject):
    """
    Returns a list of service actions taken by chat members and administrators in the last 48 hours. Available only for supergroups and channels. Requires administrator rights. Returns results in reverse chronological order (i. e., in order of decreasing event_id)
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param query: Search query by which to filter events
    :type query: :class:`str`
    
    :param from_event_id: Identifier of an event from which to return results. Use 0 to get results from the latest events
    :type from_event_id: :class:`int`
    
    :param limit: The maximum number of events to return; up to 100
    :type limit: :class:`int`
    
    :param filters: The types of events to return. By default, all types will be returned
    :type filters: :class:`ChatEventLogFilters`
    
    :param user_ids: User identifiers by which to filter events. By default, events relating to all users will be returned
    :type user_ids: :class:`list[int]`
    
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
