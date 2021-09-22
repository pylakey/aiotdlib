# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class LogTags(BaseObject):
    """
    Contains a list of available TDLib internal log tags
    
    :param tags: List of log tags
    :type tags: :class:`list[str]`
    
    """

    ID: str = Field("logTags", alias="@type")
    tags: list[str]

    @staticmethod
    def read(q: dict) -> LogTags:
        return LogTags.construct(**q)
