# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetMessage(BaseObject):
    """
    Returns information about a message. Returns a 404 error if the message doesn't exist

    :param chat_id: Identifier of the chat the message belongs to
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message to get
    :type message_id: :class:`Int53`
    """

    ID: typing.Literal["getMessage"] = Field("getMessage", validation_alias="@type", alias="@type")
    chat_id: Int53
    message_id: Int53
