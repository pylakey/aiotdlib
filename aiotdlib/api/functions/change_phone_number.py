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


class ChangePhoneNumber(BaseObject):
    """
    Changes the phone number of the user and sends an authentication code to the user's new phone number. On success, returns information about the sent code
    
    :param phone_number: The new phone number of the user in international format
    :type phone_number: :class:`str`
    
    :param settings: Settings for the authentication of the user's phone number
    :type settings: :class:`PhoneNumberAuthenticationSettings`
    
    """

    ID: str = Field("changePhoneNumber", alias="@type")
    phone_number: str
    settings: PhoneNumberAuthenticationSettings

    @staticmethod
    def read(q: dict) -> ChangePhoneNumber:
        return ChangePhoneNumber.construct(**q)
