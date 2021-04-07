# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class LogTags(BaseObject):
    """
    Contains a list of available TDLib internal log tags
    
    Params:
        tags (:obj:`list[str]`)
            List of log tags
        
    """

    ID: str = Field("logTags", alias="@type")
    tags: list[str]

    @staticmethod
    def read(q: dict) -> LogTags:
        return LogTags.construct(**q)
