# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetLogVerbosityLevel(BaseObject):
    """
    Returns current verbosity level of the internal logging of TDLib. Can be called synchronously
    
    """

    ID: str = Field("getLogVerbosityLevel", alias="@type")

    @staticmethod
    def read(q: dict) -> GetLogVerbosityLevel:
        return GetLogVerbosityLevel.construct(**q)
