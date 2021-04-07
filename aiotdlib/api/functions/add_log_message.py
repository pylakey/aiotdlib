# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class AddLogMessage(BaseObject):
    """
    Adds a message to TDLib internal log. Can be called synchronously
    
    Params:
        verbosity_level (:class:`int`)
            The minimum verbosity level needed for the message to be logged; 0-1023
        
        text (:class:`str`)
            Text of a message to log
        
    """

    ID: str = Field("addLogMessage", alias="@type")
    verbosity_level: int
    text: str

    @staticmethod
    def read(q: dict) -> AddLogMessage:
        return AddLogMessage.construct(**q)
