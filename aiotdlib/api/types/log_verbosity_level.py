# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class LogVerbosityLevel(BaseObject):
    """
    Contains a TDLib internal log verbosity level
    
    :param verbosity_level: Log verbosity level
    :type verbosity_level: :class:`int`
    
    """

    ID: str = Field("logVerbosityLevel", alias="@type")
    verbosity_level: int

    @staticmethod
    def read(q: dict) -> LogVerbosityLevel:
        return LogVerbosityLevel.construct(**q)
