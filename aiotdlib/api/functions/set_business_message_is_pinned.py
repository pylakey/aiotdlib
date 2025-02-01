# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetBusinessMessageIsPinned(BaseObject):
    """
    Pins or unpins a message sent on behalf of a business account; for bots only

    :param business_connection_id: Unique identifier of business connection on behalf of which the message was sent
    :type business_connection_id: :class:`String`
    :param chat_id: The chat the message belongs to
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    :param is_pinned: Pass true to pin the message, pass false to unpin it
    :type is_pinned: :class:`Bool`
    """

    ID: typing.Literal["setBusinessMessageIsPinned"] = Field(
        "setBusinessMessageIsPinned", validation_alias="@type", alias="@type"
    )
    business_connection_id: String
    chat_id: Int53
    message_id: Int53
    is_pinned: Bool = False
