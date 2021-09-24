# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetTemporaryPasswordState(BaseObject):
    """
    Returns information about the current temporary password
    
    """

    ID: str = Field("getTemporaryPasswordState", alias="@type")

    @staticmethod
    def read(q: dict) -> GetTemporaryPasswordState:
        return GetTemporaryPasswordState.construct(**q)
