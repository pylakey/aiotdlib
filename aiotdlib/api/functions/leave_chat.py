# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class LeaveChat(BaseObject):
    """
    Removes the current user from chat members. Private and secret chats can't be left using this method

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["leaveChat"] = "leaveChat"
    chat_id: Int53
