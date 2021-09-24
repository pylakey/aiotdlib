# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CancelPasswordReset(BaseObject):
    """
    Cancels reset of 2-step verification password. The method can be called if passwordState.pending_reset_date > 0
    
    """

    ID: str = Field("cancelPasswordReset", alias="@type")

    @staticmethod
    def read(q: dict) -> CancelPasswordReset:
        return CancelPasswordReset.construct(**q)
