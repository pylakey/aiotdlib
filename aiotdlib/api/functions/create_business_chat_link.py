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
    InputBusinessChatLink,
)


class CreateBusinessChatLink(BaseObject):
    """
    Creates a business chat link for the current account. Requires Telegram Business subscription. There can be up to getOption("business_chat_link_count_max") links created. Returns the created link

    :param link_info: Information about the link to create
    :type link_info: :class:`InputBusinessChatLink`
    """

    ID: typing.Literal["createBusinessChatLink"] = Field(
        "createBusinessChatLink", validation_alias="@type", alias="@type"
    )
    link_info: InputBusinessChatLink
