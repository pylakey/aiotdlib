# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetMessageReadDate(BaseObject):
    """
    Returns read date of a recent outgoing message in a private chat. The method can be called if messageProperties.can_get_read_date == true

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    """

    ID: typing.Literal["getMessageReadDate"] = Field("getMessageReadDate", validation_alias="@type", alias="@type")
    chat_id: Int53
    message_id: Int53
