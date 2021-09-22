# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import PhoneNumberAuthenticationSettings
from ..base_object import BaseObject


class SetAuthenticationPhoneNumber(BaseObject):
    """
    Sets the phone number of the user and sends an authentication code to the user. Works only when the current authorization state is authorizationStateWaitPhoneNumber, or if there is no pending authentication query and the current authorization state is authorizationStateWaitCode, authorizationStateWaitRegistration, or authorizationStateWaitPassword
    
    :param phone_number: The phone number of the user, in international format
    :type phone_number: :class:`str`
    
    :param settings: Settings for the authentication of the user's phone number
    :type settings: :class:`PhoneNumberAuthenticationSettings`
    
    """

    ID: str = Field("setAuthenticationPhoneNumber", alias="@type")
    phone_number: str
    settings: PhoneNumberAuthenticationSettings

    @staticmethod
    def read(q: dict) -> SetAuthenticationPhoneNumber:
        return SetAuthenticationPhoneNumber.construct(**q)
