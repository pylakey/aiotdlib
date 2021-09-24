# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ResendPhoneNumberVerificationCode(BaseObject):
    """
    Re-sends the code to verify a phone number to be added to a user's Telegram Passport
    
    """

    ID: str = Field("resendPhoneNumberVerificationCode", alias="@type")

    @staticmethod
    def read(q: dict) -> ResendPhoneNumberVerificationCode:
        return ResendPhoneNumberVerificationCode.construct(**q)
