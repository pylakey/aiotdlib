# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetRecoveryEmailAddress(BaseObject):
    """
    Returns a 2-step verification recovery email address that was previously set up. This method can be used to verify a password provided by the user
    
    Params:
        password (:class:`str`)
            The password for the current user
        
    """

    ID: str = Field("getRecoveryEmailAddress", alias="@type")
    password: str

    @staticmethod
    def read(q: dict) -> GetRecoveryEmailAddress:
        return GetRecoveryEmailAddress.construct(**q)
