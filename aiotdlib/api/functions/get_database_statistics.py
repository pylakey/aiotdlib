# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetDatabaseStatistics(BaseObject):
    """
    Returns database statistics
    
    """

    ID: str = Field("getDatabaseStatistics", alias="@type")

    @staticmethod
    def read(q: dict) -> GetDatabaseStatistics:
        return GetDatabaseStatistics.construct(**q)
