# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SendEmailAddressVerificationCode(BaseObject):
    """
    Sends a code to verify an email address to be added to a user's Telegram Passport
    
    Params:
        email_address (:class:`str`)
            Email address
        
    """

    ID: str = Field("sendEmailAddressVerificationCode", alias="@type")
    email_address: str

    @staticmethod
    def read(q: dict) -> SendEmailAddressVerificationCode:
        return SendEmailAddressVerificationCode.construct(**q)
