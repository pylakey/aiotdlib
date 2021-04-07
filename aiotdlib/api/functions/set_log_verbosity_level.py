# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SetLogVerbosityLevel(BaseObject):
    """
    Sets the verbosity level of the internal logging of TDLib. Can be called synchronously
    
    Params:
        new_verbosity_level (:class:`int`)
            New value of the verbosity level for logging. Value 0 corresponds to fatal errors, value 1 corresponds to errors, value 2 corresponds to warnings and debug warnings, value 3 corresponds to informational, value 4 corresponds to debug, value 5 corresponds to verbose debug, value greater than 5 and up to 1023 can be used to enable even more logging
        
    """

    ID: str = Field("setLogVerbosityLevel", alias="@type")
    new_verbosity_level: int

    @staticmethod
    def read(q: dict) -> SetLogVerbosityLevel:
        return SetLogVerbosityLevel.construct(**q)
