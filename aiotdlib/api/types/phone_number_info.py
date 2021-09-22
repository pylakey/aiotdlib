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
    
    :param country: Information about the country to which the phone number belongs; may be null, defaults to None
    :type country: :class:`CountryInfo`, optional
    
    :param country_calling_code: The part of the phone number denoting country calling code or its part
    :type country_calling_code: :class:`str`
    
    :param formatted_phone_number: The phone number without country calling code formatted accordingly to local rules. Expected digits are returned as '-', but even more digits might be entered by the user
    :type formatted_phone_number: :class:`str`
    
    """

    ID: str = Field("phoneNumberInfo", alias="@type")
    country: typing.Optional[CountryInfo] = None
    country_calling_code: str
    formatted_phone_number: str

    @staticmethod
    def read(q: dict) -> PhoneNumberInfo:
        return PhoneNumberInfo.construct(**q)
