# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class LogVerbosityLevel(BaseObject):
    """
    Contains a TDLib internal log verbosity level
    
    Params:
        verbosity_level (:class:`int`)
            Log verbosity level
        
    """

    ID: str = Field("logVerbosityLevel", alias="@type")
    verbosity_level: int

    @staticmethod
    def read(q: dict) -> LogVerbosityLevel:
        return LogVerbosityLevel.construct(**q)
