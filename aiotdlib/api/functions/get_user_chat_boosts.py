# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetUserChatBoosts(BaseObject):
    """
    Returns the list of boosts applied to a chat by a given user; requires administrator rights in the chat; for bots only

    :param chat_id: Identifier of the chat
    :type chat_id: :class:`Int53`
    :param user_id: Identifier of the user
    :type user_id: :class:`Int53`
    """

    ID: typing.Literal["getUserChatBoosts"] = Field("getUserChatBoosts", validation_alias="@type", alias="@type")
    chat_id: Int53
    user_id: Int53
