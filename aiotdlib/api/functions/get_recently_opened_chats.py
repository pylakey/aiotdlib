# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetRecentlyOpenedChats(BaseObject):
    """
    Returns recently opened chats. This is an offline method. Returns chats in the order of last opening

    :param limit: The maximum number of chats to be returned
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["getRecentlyOpenedChats"] = Field(
        "getRecentlyOpenedChats", validation_alias="@type", alias="@type"
    )
    limit: Int32
