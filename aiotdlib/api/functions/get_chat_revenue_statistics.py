# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetChatRevenueStatistics(BaseObject):
    """
    Returns detailed revenue statistics about a chat. Currently, this method can be used only for channels if supergroupFullInfo.can_get_revenue_statistics == true or bots if userFullInfo.bot_info.can_get_revenue_statistics == true

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param is_dark: Pass true if a dark theme is used by the application
    :type is_dark: :class:`Bool`
    """

    ID: typing.Literal["getChatRevenueStatistics"] = Field(
        "getChatRevenueStatistics", validation_alias="@type", alias="@type"
    )
    chat_id: Int53
    is_dark: Bool = False
