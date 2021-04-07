# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import JsonValue


class SaveApplicationLogEvent(BaseObject):
    """
    Saves application log event on the server. Can be called before authorization
    
    Params:
        type_ (:class:`str`)
            Event type
        
        chat_id (:class:`int`)
            Optional chat identifier, associated with the event
        
        data (:class:`JsonValue`)
            The log event data
        
    """

    ID: str = Field("saveApplicationLogEvent", alias="@type")
    type_: str = Field(..., alias='type')
    chat_id: int
    data: JsonValue

    @staticmethod
    def read(q: dict) -> SaveApplicationLogEvent:
        return SaveApplicationLogEvent.construct(**q)
