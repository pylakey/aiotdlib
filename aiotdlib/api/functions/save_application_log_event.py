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
    JsonValue,
)


class SaveApplicationLogEvent(BaseObject):
    """
    Saves application log event on the server. Can be called before authorization

    :param type_: Event type
    :type type_: :class:`String`
    :param chat_id: Optional chat identifier, associated with the event
    :type chat_id: :class:`Int53`
    :param data: The log event data
    :type data: :class:`JsonValue`
    """

    ID: typing.Literal["saveApplicationLogEvent"] = "saveApplicationLogEvent"
    type_: String = Field(..., alias="type")
    chat_id: Int53
    data: JsonValue
