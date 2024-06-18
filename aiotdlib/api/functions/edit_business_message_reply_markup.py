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
    ReplyMarkup,
)


class EditBusinessMessageReplyMarkup(BaseObject):
    """
    Edits the reply markup of a message sent on behalf of a business account; for bots only

    :param business_connection_id: Unique identifier of business connection on behalf of which the message was sent
    :type business_connection_id: :class:`String`
    :param chat_id: The chat the message belongs to
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    :param reply_markup: The new message reply markup; pass null if none, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    """

    ID: typing.Literal["editBusinessMessageReplyMarkup"] = Field(
        "editBusinessMessageReplyMarkup", validation_alias="@type", alias="@type"
    )
    business_connection_id: String
    chat_id: Int53
    message_id: Int53
    reply_markup: typing.Optional[ReplyMarkup] = None
