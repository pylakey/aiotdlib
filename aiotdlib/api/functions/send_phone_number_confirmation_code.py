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


class SendPhoneNumberConfirmationCode(BaseObject):
    """
    Sends phone number confirmation code to handle links of the type internalLinkTypePhoneNumberConfirmation
    
    :param hash_: Hash value from the link
    :type hash_: :class:`str`
    
    :param phone_number: Phone number value from the link
    :type phone_number: :class:`str`
    
    :param settings: Settings for the authentication of the user's phone number
    :type settings: :class:`PhoneNumberAuthenticationSettings`
    
    """

    ID: str = Field("sendPhoneNumberConfirmationCode", alias="@type")
    hash_: str = Field(..., alias='hash')
    phone_number: str
    settings: PhoneNumberAuthenticationSettings

    @staticmethod
    def read(q: dict) -> SendPhoneNumberConfirmationCode:
        return SendPhoneNumberConfirmationCode.construct(**q)
