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
    CallbackQueryPayload,
)


class GetCallbackQueryAnswer(BaseObject):
    """
    Sends a callback query to a bot and returns an answer. Returns an error with code 502 if the bot fails to answer the query before the query timeout expires

    :param chat_id: Identifier of the chat with the message
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message from which the query originated. The message must not be scheduled
    :type message_id: :class:`Int53`
    :param payload: Query payload
    :type payload: :class:`CallbackQueryPayload`
    """

    ID: typing.Literal["getCallbackQueryAnswer"] = Field(
        "getCallbackQueryAnswer", validation_alias="@type", alias="@type"
    )
    chat_id: Int53
    message_id: Int53
    payload: CallbackQueryPayload
