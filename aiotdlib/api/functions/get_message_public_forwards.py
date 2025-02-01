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
    Returns forwarded copies of a channel message to different public channels and public reposts as a story. Can be used only if messageProperties.can_get_statistics == true. For optimal performance, the number of returned messages and stories is chosen by TDLib

    :param chat_id: Chat identifier of the message
    :type chat_id: :class:`Int53`
    :param message_id: Message identifier
    :type message_id: :class:`Int53`
    :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
    :type offset: :class:`String`
    :param limit: The maximum number of messages and stories to be returned; must be positive and can't be greater than 100. For optimal performance, the number of returned objects is chosen by TDLib and can be smaller than the specified limit
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["getMessagePublicForwards"] = Field(
        "getMessagePublicForwards", validation_alias="@type", alias="@type"
    )
    chat_id: Int53
    message_id: Int53
    offset: String
    limit: Int32
