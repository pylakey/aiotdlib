# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class DatabaseStatistics(BaseObject):
    """
    Contains database statistics
    
    :param statistics: Database statistics in an unspecified human-readable format
    :type statistics: :class:`str`
    
    """

    ID: str = Field("databaseStatistics", alias="@type")
    statistics: str

    @staticmethod
    def read(q: dict) -> DatabaseStatistics:
        return DatabaseStatistics.construct(**q)
