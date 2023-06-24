# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    ChatEventLogFilters,
)


class GetChatEventLog(BaseObject):
    """
    Returns a list of service actions taken by chat members and administrators in the last 48 hours. Available only for supergroups and channels. Requires administrator rights. Returns results in reverse chronological order (i.e., in order of decreasing event_id)

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param query: Search query by which to filter events
    :type query: :class:`String`
    :param from_event_id: Identifier of an event from which to return results. Use 0 to get results from the latest events
    :type from_event_id: :class:`Int64`
    :param limit: The maximum number of events to return; up to 100
    :type limit: :class:`Int32`
    :param user_ids: User identifiers by which to filter events. By default, events relating to all users will be returned
    :type user_ids: :class:`Vector[Int53]`
    :param filters: The types of events to return; pass null to get chat events of all types, defaults to None
    :type filters: :class:`ChatEventLogFilters`, optional
    """

    ID: typing.Literal["getChatEventLog"] = "getChatEventLog"
    chat_id: Int53
    query: String
    from_event_id: Int64
    limit: Int32
    user_ids: Vector[Int53]
    filters: typing.Optional[ChatEventLogFilters] = None
