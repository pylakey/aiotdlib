# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetMessageProperties(BaseObject):
    """
    Returns properties of a message. This is an offline method

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    """

    ID: typing.Literal["getMessageProperties"] = Field("getMessageProperties", validation_alias="@type", alias="@type")
    chat_id: Int53
    message_id: Int53
