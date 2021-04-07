# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SetLogTagVerbosityLevel(BaseObject):
    """
    Sets the verbosity level for a specified TDLib internal log tag. Can be called synchronously
    
    Params:
        tag (:class:`str`)
            Logging tag to change verbosity level
        
        new_verbosity_level (:class:`int`)
            New verbosity level; 1-1024
        
    """

    ID: str = Field("setLogTagVerbosityLevel", alias="@type")
    tag: str
    new_verbosity_level: int

    @staticmethod
    def read(q: dict) -> SetLogTagVerbosityLevel:
        return SetLogTagVerbosityLevel.construct(**q)
