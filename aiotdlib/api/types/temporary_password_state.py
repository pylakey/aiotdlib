# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class TemporaryPasswordState(BaseObject):
    """
    Returns information about the availability of a temporary password, which can be used for payments
    
    Params:
        has_password (:class:`bool`)
            True, if a temporary password is available
        
        valid_for (:class:`int`)
            Time left before the temporary password expires, in seconds
        
    """

    ID: str = Field("temporaryPasswordState", alias="@type")
    has_password: bool
    valid_for: int

    @staticmethod
    def read(q: dict) -> TemporaryPasswordState:
        return TemporaryPasswordState.construct(**q)
