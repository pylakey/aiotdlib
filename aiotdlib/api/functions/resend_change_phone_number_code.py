# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ResendChangePhoneNumberCode(BaseObject):
    """
    Re-sends the authentication code sent to confirm a new phone number for the user. Works only if the previously received authenticationCodeInfo next_code_type was not null
    
    """

    ID: str = Field("resendChangePhoneNumberCode", alias="@type")

    @staticmethod
    def read(q: dict) -> ResendChangePhoneNumberCode:
        return ResendChangePhoneNumberCode.construct(**q)
