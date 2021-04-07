# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import PhoneNumberAuthenticationSettings


class SendPhoneNumberVerificationCode(BaseObject):
    """
    Sends a code to verify a phone number to be added to a user's Telegram Passport
    
    Params:
        phone_number (:class:`str`)
            The phone number of the user, in international format
        
        settings (:class:`PhoneNumberAuthenticationSettings`)
            Settings for the authentication of the user's phone number
        
    """

    ID: str = Field("sendPhoneNumberVerificationCode", alias="@type")
    phone_number: str
    settings: PhoneNumberAuthenticationSettings

    @staticmethod
    def read(q: dict) -> SendPhoneNumberVerificationCode:
        return SendPhoneNumberVerificationCode.construct(**q)
