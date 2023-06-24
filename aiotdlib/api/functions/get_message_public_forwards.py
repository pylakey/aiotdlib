# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetMessagePublicForwards(BaseObject):
    """
    Returns forwarded copies of a channel message to different public channels. For optimal performance, the number of returned messages is chosen by TDLib

    :param chat_id: Chat identifier of the message
    :type chat_id: :class:`Int53`
    :param message_id: Message identifier
    :type message_id: :class:`Int53`
    :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
    :type offset: :class:`String`
    :param limit: The maximum number of messages to be returned; must be positive and can't be greater than 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["getMessagePublicForwards"] = "getMessagePublicForwards"
    chat_id: Int53
    message_id: Int53
    offset: String
    limit: Int32
