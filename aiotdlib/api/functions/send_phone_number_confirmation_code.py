# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import PhoneNumberAuthenticationSettings


class SendPhoneNumberConfirmationCode(BaseObject):
    """
    Sends phone number confirmation code to handle links of the type internalLinkTypePhoneNumberConfirmation
    
    Params:
        hash_ (:class:`str`)
            Hash value from the link
        
        phone_number (:class:`str`)
            Phone number value from the link
        
        settings (:class:`PhoneNumberAuthenticationSettings`)
            Settings for the authentication of the user's phone number
        
    """

    ID: str = Field("sendPhoneNumberConfirmationCode", alias="@type")
    hash_: str = Field(..., alias='hash')
    phone_number: str
    settings: PhoneNumberAuthenticationSettings

    @staticmethod
    def read(q: dict) -> SendPhoneNumberConfirmationCode:
        return SendPhoneNumberConfirmationCode.construct(**q)
