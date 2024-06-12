# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetChatBoostLink(BaseObject):
    """
    Returns an HTTPS link to boost the specified supergroup or channel chat

    :param chat_id: Identifier of the chat
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getChatBoostLink"] = Field("getChatBoostLink", validation_alias="@type", alias="@type")
    chat_id: Int53
