# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetSavedOrderInfo(BaseObject):
    """
    Returns saved order info, if any
    
    """

    ID: str = Field("getSavedOrderInfo", alias="@type")

    @staticmethod
    def read(q: dict) -> GetSavedOrderInfo:
        return GetSavedOrderInfo.construct(**q)
