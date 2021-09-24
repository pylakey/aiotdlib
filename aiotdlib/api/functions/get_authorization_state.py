# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetAuthorizationState(BaseObject):
    """
    Returns the current authorization state; this is an offline request. For informational purposes only. Use updateAuthorizationState instead to maintain the current authorization state. Can be called before initialization
    
    """

    ID: str = Field("getAuthorizationState", alias="@type")

    @staticmethod
    def read(q: dict) -> GetAuthorizationState:
        return GetAuthorizationState.construct(**q)
