# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetCurrentState(BaseObject):
    """
    Returns all updates needed to restore current TDLib state, i.e. all actual UpdateAuthorizationState/UpdateUser/UpdateNewChat and others. This is especially useful if TDLib is run in a separate process. Can be called before initialization
    
    """

    ID: str = Field("getCurrentState", alias="@type")

    @staticmethod
    def read(q: dict) -> GetCurrentState:
        return GetCurrentState.construct(**q)
