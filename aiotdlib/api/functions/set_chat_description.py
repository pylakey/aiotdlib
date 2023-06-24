# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetChatDescription(BaseObject):
    """
    Changes information about a chat. Available for basic groups, supergroups, and channels. Requires can_change_info administrator right

    :param chat_id: Identifier of the chat
    :type chat_id: :class:`Int53`
    :param description: New chat description; 0-255 characters
    :type description: :class:`String`
    """

    ID: typing.Literal["setChatDescription"] = "setChatDescription"
    chat_id: Int53
    description: String = Field("", max_length=255)
