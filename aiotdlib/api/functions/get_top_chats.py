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
    TopChatCategory,
)


class GetTopChats(BaseObject):
    """
    Returns a list of frequently used chats

    :param category: Category of chats to be returned
    :type category: :class:`TopChatCategory`
    :param limit: The maximum number of chats to be returned; up to 30
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["getTopChats"] = "getTopChats"
    category: TopChatCategory
    limit: Int32
