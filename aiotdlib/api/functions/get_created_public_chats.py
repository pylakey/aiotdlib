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


class GetCreatedPublicChats(BaseObject):
    """
    Returns a list of public chats of the specified type, owned by the user

    :param type_: Type of the public chats to return
    :type type_: :class:`PublicChatType`
    """

    ID: typing.Literal["getCreatedPublicChats"] = "getCreatedPublicChats"
    type_: PublicChatType = Field(..., alias="type")
