# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ResendRecoveryEmailAddressCode(BaseObject):
    """
    Resends the 2-step verification recovery email address verification code
    
    """

    ID: str = Field("resendRecoveryEmailAddressCode", alias="@type")

    @staticmethod
    def read(q: dict) -> ResendRecoveryEmailAddressCode:
        return ResendRecoveryEmailAddressCode.construct(**q)
