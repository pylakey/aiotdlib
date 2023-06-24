# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetForumTopics(BaseObject):
    """
    Returns found forum topics in a forum chat. This is a temporary method for getting information about topic list from the server

    :param chat_id: Identifier of the forum chat
    :type chat_id: :class:`Int53`
    :param query: Query to search for in the forum topic's name
    :type query: :class:`String`
    :param offset_date: The date starting from which the results need to be fetched. Use 0 or any date in the future to get results from the last topic
    :type offset_date: :class:`Int32`
    :param offset_message_id: The message identifier of the last message in the last found topic, or 0 for the first request
    :type offset_message_id: :class:`Int53`
    :param offset_message_thread_id: The message thread identifier of the last found topic, or 0 for the first request
    :type offset_message_thread_id: :class:`Int53`
    :param limit: The maximum number of forum topics to be returned; up to 100. For optimal performance, the number of returned forum topics is chosen by TDLib and can be smaller than the specified limit
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["getForumTopics"] = "getForumTopics"
    chat_id: Int53
    query: String
    offset_date: Int32
    offset_message_id: Int53
    offset_message_thread_id: Int53
    limit: Int32
