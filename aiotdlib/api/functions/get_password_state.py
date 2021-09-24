# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetPasswordState(BaseObject):
    """
    Returns the current state of 2-step verification
    
    """

    ID: str = Field("getPasswordState", alias="@type")

    @staticmethod
    def read(q: dict) -> GetPasswordState:
        return GetPasswordState.construct(**q)
