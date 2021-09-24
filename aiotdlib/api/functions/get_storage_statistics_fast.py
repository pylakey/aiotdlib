# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetStorageStatisticsFast(BaseObject):
    """
    Quickly returns approximate storage usage statistics. Can be called before authorization
    
    """

    ID: str = Field("getStorageStatisticsFast", alias="@type")

    @staticmethod
    def read(q: dict) -> GetStorageStatisticsFast:
        return GetStorageStatisticsFast.construct(**q)
