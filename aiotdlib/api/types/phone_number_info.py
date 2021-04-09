# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .country_info import CountryInfo
from ..base_object import BaseObject


class PhoneNumberInfo(BaseObject):
    """
    Contains information about a phone number
    
    Params:
        country (:class:`CountryInfo`)
            Information about the country to which the phone number belongs; may be null
        
        country_calling_code (:class:`str`)
            The part of the phone number denoting country calling code or its part
        
        formatted_phone_number (:class:`str`)
            The phone number without country calling code formatted accordingly to local rules
        
    """

    ID: str = Field("phoneNumberInfo", alias="@type")
    country: typing.Optional[CountryInfo] = None
    country_calling_code: str
    formatted_phone_number: str

    @staticmethod
    def read(q: dict) -> PhoneNumberInfo:
        return PhoneNumberInfo.construct(**q)
