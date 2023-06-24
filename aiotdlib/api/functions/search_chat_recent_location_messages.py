# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SearchChatRecentLocationMessages(BaseObject):
    """
    Returns information about the recent locations of chat members that were sent to the chat. Returns up to 1 location message per user

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param limit: The maximum number of messages to be returned
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["searchChatRecentLocationMessages"] = "searchChatRecentLocationMessages"
    chat_id: Int53
    limit: Int32
