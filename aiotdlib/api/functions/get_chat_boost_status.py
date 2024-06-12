# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetChatBoostStatus(BaseObject):
    """
    Returns the current boost status for a supergroup or a channel chat

    :param chat_id: Identifier of the chat
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getChatBoostStatus"] = Field("getChatBoostStatus", validation_alias="@type", alias="@type")
    chat_id: Int53
