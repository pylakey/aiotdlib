# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SetLogTagVerbosityLevel(BaseObject):
    """
    Sets the verbosity level for a specified TDLib internal log tag. Can be called synchronously
    
    :param tag: Logging tag to change verbosity level
    :type tag: :class:`str`
    
    :param new_verbosity_level: New verbosity level; 1-1024
    :type new_verbosity_level: :class:`int`
    
    """

    ID: str = Field("setLogTagVerbosityLevel", alias="@type")
    tag: str
    new_verbosity_level: int

    @staticmethod
    def read(q: dict) -> SetLogTagVerbosityLevel:
        return SetLogTagVerbosityLevel.construct(**q)
