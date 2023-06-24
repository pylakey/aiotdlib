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


class StopPoll(BaseObject):
    """
    Stops a poll. A poll in a message can be stopped when the message has can_be_edited flag set

    :param chat_id: Identifier of the chat to which the poll belongs
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message containing the poll
    :type message_id: :class:`Int53`
    :param reply_markup: The new message reply markup; pass null if none; for bots only, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    """

    ID: typing.Literal["stopPoll"] = "stopPoll"
    chat_id: Int53
    message_id: Int53
    reply_markup: typing.Optional[ReplyMarkup] = None
