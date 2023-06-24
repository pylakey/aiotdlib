# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetChatSlowModeDelay(BaseObject):
    """
    Changes the slow mode delay of a chat. Available only for supergroups; requires can_restrict_members rights

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param slow_mode_delay: New slow mode delay for the chat, in seconds; must be one of 0, 10, 30, 60, 300, 900, 3600
    :type slow_mode_delay: :class:`Int32`
    """

    ID: typing.Literal["setChatSlowModeDelay"] = "setChatSlowModeDelay"
    chat_id: Int53
    slow_mode_delay: Int32
