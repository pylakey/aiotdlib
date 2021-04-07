# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class DeleteSavedOrderInfo(BaseObject):
    """
    Deletes saved order info
    
    """

    ID: str = Field("deleteSavedOrderInfo", alias="@type")

    @staticmethod
    def read(q: dict) -> DeleteSavedOrderInfo:
        return DeleteSavedOrderInfo.construct(**q)
