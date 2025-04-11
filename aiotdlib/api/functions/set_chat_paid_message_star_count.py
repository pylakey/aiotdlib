# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetChatPaidMessageStarCount(BaseObject):
    """
    Changes the amount of Telegram Stars that must be paid to send a message to a supergroup chat; requires can_restrict_members administrator right and supergroupFullInfo.can_enable_paid_messages

    :param chat_id: Identifier of the supergroup chat
    :type chat_id: :class:`Int53`
    :param paid_message_star_count: The new number of Telegram Stars that must be paid for each message that is sent to the supergroup chat unless the sender is an administrator of the chat; 0-getOption("paid_message_star_count_max"). The supergroup will receive getOption("paid_message_earnings_per_mille") Telegram Stars for each 1000 Telegram Stars paid for message sending
    :type paid_message_star_count: :class:`Int53`
    """

    ID: typing.Literal["setChatPaidMessageStarCount"] = Field(
        "setChatPaidMessageStarCount", validation_alias="@type", alias="@type"
    )
    chat_id: Int53
    paid_message_star_count: Int53
