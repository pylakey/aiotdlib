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
    MessageSender,
)


class ReportMessageReactions(BaseObject):
    """
    Reports reactions set on a message to the Telegram moderators. Reactions on a message can be reported only if message.can_report_reactions

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_id: Message identifier
    :type message_id: :class:`Int53`
    :param sender_id: Identifier of the sender, which added the reaction
    :type sender_id: :class:`MessageSender`
    """

    ID: typing.Literal["reportMessageReactions"] = "reportMessageReactions"
    chat_id: Int53
    message_id: Int53
    sender_id: MessageSender
