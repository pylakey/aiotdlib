# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ResendEmailAddressVerificationCode(BaseObject):
    """
    Re-sends the code to verify an email address to be added to a user's Telegram Passport
    
    """

    ID: str = Field("resendEmailAddressVerificationCode", alias="@type")

    @staticmethod
    def read(q: dict) -> ResendEmailAddressVerificationCode:
        return ResendEmailAddressVerificationCode.construct(**q)
