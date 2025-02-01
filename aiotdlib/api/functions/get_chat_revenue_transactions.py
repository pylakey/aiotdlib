# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetChatRevenueTransactions(BaseObject):
    """
    Returns the list of revenue transactions for a chat. Currently, this method can be used only for channels if supergroupFullInfo.can_get_revenue_statistics == true or bots if userFullInfo.bot_info.can_get_revenue_statistics == true

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param offset: Number of transactions to skip
    :type offset: :class:`Int32`
    :param limit: The maximum number of transactions to be returned; up to 200
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["getChatRevenueTransactions"] = Field(
        "getChatRevenueTransactions", validation_alias="@type", alias="@type"
    )
    chat_id: Int53
    offset: Int32
    limit: Int32
