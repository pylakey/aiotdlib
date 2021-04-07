# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class Address(BaseObject):
    """
    Describes an address
    
    Params:
        country_code (:class:`str`)
            A two-letter ISO 3166-1 alpha-2 country code
        
        state (:class:`str`)
            State, if applicable
        
        city (:class:`str`)
            City
        
        street_line1 (:class:`str`)
            First line of the address
        
        street_line2 (:class:`str`)
            Second line of the address
        
        postal_code (:class:`str`)
            Address postal code
        
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
