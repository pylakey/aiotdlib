# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetChat(BaseObject):
    """
    Returns information about a chat by its identifier. This is an offline method if the current user is not a bot

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getChat"] = Field("getChat", validation_alias="@type", alias="@type")
    chat_id: Int53
