# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ResendPhoneNumberConfirmationCode(BaseObject):
    """
    Resends phone number confirmation code
    
    """

    ID: str = Field("resendPhoneNumberConfirmationCode", alias="@type")

    @staticmethod
    def read(q: dict) -> ResendPhoneNumberConfirmationCode:
        return ResendPhoneNumberConfirmationCode.construct(**q)
