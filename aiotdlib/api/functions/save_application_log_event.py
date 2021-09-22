# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import JsonValue
from ..base_object import BaseObject


class SaveApplicationLogEvent(BaseObject):
    """
    Saves application log event on the server. Can be called before authorization
    
    :param type_: Event type
    :type type_: :class:`str`
    
    :param chat_id: Optional chat identifier, associated with the event
    :type chat_id: :class:`int`
    
    :param data: The log event data
    :type data: :class:`JsonValue`
    
    """

    ID: str = Field("saveApplicationLogEvent", alias="@type")
    type_: str = Field(..., alias='type')
    chat_id: int
    data: JsonValue

    @staticmethod
    def read(q: dict) -> SaveApplicationLogEvent:
        return SaveApplicationLogEvent.construct(**q)
