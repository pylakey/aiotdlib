# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetLogTagVerbosityLevel(BaseObject):
    """
    Returns current verbosity level for a specified TDLib internal log tag. Can be called synchronously
    
    :param tag: Logging tag to change verbosity level
    :type tag: :class:`str`
    
    """

    ID: str = Field("getLogTagVerbosityLevel", alias="@type")
    tag: str

    @staticmethod
    def read(q: dict) -> GetLogTagVerbosityLevel:
        return GetLogTagVerbosityLevel.construct(**q)
