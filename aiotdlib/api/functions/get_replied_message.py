# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetRepliedMessage(BaseObject):
    """
    Returns information about a non-bundled message that is replied by a given message. Also, returns the pinned message, the game message, the invoice message, the message with a previously set same background, the giveaway message, and the topic creation message for messages of the types messagePinMessage, messageGameScore, messagePaymentSuccessful, messageChatSetBackground, messageGiveawayCompleted and topic messages without non-bundled replied message respectively. Returns a 404 error if the message doesn't exist

    :param chat_id: Identifier of the chat the message belongs to
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the reply message
    :type message_id: :class:`Int53`
    """

    ID: typing.Literal["getRepliedMessage"] = Field("getRepliedMessage", validation_alias="@type", alias="@type")
    chat_id: Int53
    message_id: Int53
