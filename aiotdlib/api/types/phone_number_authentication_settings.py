# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class PhoneNumberAuthenticationSettings(BaseObject):
    """
    Contains settings for the authentication of the user's phone number
    
    :param allow_flash_call: Pass true if the authentication code may be sent via flash call to the specified phone number
    :type allow_flash_call: :class:`bool`
    
    :param is_current_phone_number: Pass true if the authenticated phone number is used on the current device
    :type is_current_phone_number: :class:`bool`
    
    :param allow_sms_retriever_api: For official applications only. True, if the application can use Android SMS Retriever API (requires Google Play Services >= 10.2) to automatically receive the authentication code from the SMS. See https://developers.google.com/identity/sms-retriever/ for more details
    :type allow_sms_retriever_api: :class:`bool`
    
    """

    ID: str = Field("phoneNumberAuthenticationSettings", alias="@type")
    allow_flash_call: bool
    is_current_phone_number: bool
    allow_sms_retriever_api: bool

    @staticmethod
    def read(q: dict) -> PhoneNumberAuthenticationSettings:
        return PhoneNumberAuthenticationSettings.construct(**q)
