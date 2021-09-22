# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class Address(BaseObject):
    """
    Describes an address
    
    :param country_code: A two-letter ISO 3166-1 alpha-2 country code
    :type country_code: :class:`str`
    
    :param state: State, if applicable
    :type state: :class:`str`
    
    :param city: City
    :type city: :class:`str`
    
    :param street_line1: First line of the address
    :type street_line1: :class:`str`
    
    :param street_line2: Second line of the address
    :type street_line2: :class:`str`
    
    :param postal_code: Address postal code
    :type postal_code: :class:`str`
    
    """

    ID: str = Field("address", alias="@type")
    country_code: str
    state: str
    city: str
    street_line1: str
    street_line2: str
    postal_code: str

    @staticmethod
    def read(q: dict) -> Address:
        return Address.construct(**q)
