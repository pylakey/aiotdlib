# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class LogOut(BaseObject):
    """
    Closes the TDLib instance after a proper logout. Requires an available network connection. All local data will be destroyed. After the logout completes, updateAuthorizationState with authorizationStateClosed will be sent
    
    """

    ID: str = Field("logOut", alias="@type")

    @staticmethod
    def read(q: dict) -> LogOut:
        return LogOut.construct(**q)
