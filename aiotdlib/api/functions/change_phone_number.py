# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import PhoneNumberAuthenticationSettings


class ChangePhoneNumber(BaseObject):
    """
    Changes the phone number of the user and sends an authentication code to the user's new phone number. On success, returns information about the sent code
    
    Params:
        phone_number (:class:`str`)
            The new phone number of the user in international format
        
        settings (:class:`PhoneNumberAuthenticationSettings`)
            Settings for the authentication of the user's phone number
        
    """

    ID: str = Field("changePhoneNumber", alias="@type")
    phone_number: str
    settings: PhoneNumberAuthenticationSettings

    @staticmethod
    def read(q: dict) -> ChangePhoneNumber:
        return ChangePhoneNumber.construct(**q)
