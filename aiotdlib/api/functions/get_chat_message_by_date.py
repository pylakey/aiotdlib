# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetChatMessageByDate(BaseObject):
    """
    Returns the last message sent in a chat no later than the specified date

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param date: Point in time (Unix timestamp) relative to which to search for messages
    :type date: :class:`Int32`
    """

    ID: typing.Literal["getChatMessageByDate"] = "getChatMessageByDate"
    chat_id: Int53
    date: Int32
