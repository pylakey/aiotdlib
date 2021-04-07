# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetLogStream(BaseObject):
    """
    Returns information about currently used log stream for internal logging of TDLib. Can be called synchronously
    
    """

    ID: str = Field("getLogStream", alias="@type")

    @staticmethod
    def read(q: dict) -> GetLogStream:
        return GetLogStream.construct(**q)
