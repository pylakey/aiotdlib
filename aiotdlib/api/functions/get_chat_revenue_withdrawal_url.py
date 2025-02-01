# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetChatRevenueWithdrawalUrl(BaseObject):
    """
    Returns a URL for chat revenue withdrawal; requires owner privileges in the channel chat or the bot. Currently, this method can be used only if getOption("can_withdraw_chat_revenue") for channels with supergroupFullInfo.can_get_revenue_statistics == true or bots with userFullInfo.bot_info.can_get_revenue_statistics == true

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param password: The 2-step verification password of the current user
    :type password: :class:`String`
    """

    ID: typing.Literal["getChatRevenueWithdrawalUrl"] = Field(
        "getChatRevenueWithdrawalUrl", validation_alias="@type", alias="@type"
    )
    chat_id: Int53
    password: String
