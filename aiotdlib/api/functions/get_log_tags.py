# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetLogTags(BaseObject):
    """
    Returns list of available TDLib internal log tags, for example, ["actor", "binlog", "connections", "notifications", "proxy"]. Can be called synchronously
    
    """

    ID: str = Field("getLogTags", alias="@type")

    @staticmethod
    def read(q: dict) -> GetLogTags:
        return GetLogTags.construct(**q)
