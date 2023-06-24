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
    PublicChatType,
)


class CheckCreatedPublicChatsLimit(BaseObject):
    """
    Checks whether the maximum number of owned public chats has been reached. Returns corresponding error if the limit was reached. The limit can be increased with Telegram Premium

    :param type_: Type of the public chats, for which to check the limit
    :type type_: :class:`PublicChatType`
    """

    ID: typing.Literal["checkCreatedPublicChatsLimit"] = "checkCreatedPublicChatsLimit"
    type_: PublicChatType = Field(..., alias="type")
