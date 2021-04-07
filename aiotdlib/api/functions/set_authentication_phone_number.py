# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import PhoneNumberAuthenticationSettings


class SetAuthenticationPhoneNumber(BaseObject):
    """
    Sets the phone number of the user and sends an authentication code to the user. Works only when the current authorization state is authorizationStateWaitPhoneNumber, or if there is no pending authentication query and the current authorization state is authorizationStateWaitCode, authorizationStateWaitRegistration, or authorizationStateWaitPassword
    
    Params:
        phone_number (:class:`str`)
            The phone number of the user, in international format
        
        settings (:class:`PhoneNumberAuthenticationSettings`)
            Settings for the authentication of the user's phone number
        
    """

    ID: str = Field("setAuthenticationPhoneNumber", alias="@type")
    phone_number: str
    settings: PhoneNumberAuthenticationSettings

    @staticmethod
    def read(q: dict) -> SetAuthenticationPhoneNumber:
        return SetAuthenticationPhoneNumber.construct(**q)
