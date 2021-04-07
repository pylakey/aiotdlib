# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CountryInfo(BaseObject):
    """
    Contains information about a country
    
    Params:
        country_code (:class:`str`)
            A two-letter ISO 3166-1 alpha-2 country code
        
        name (:class:`str`)
            Native name of the country
        
        english_name (:class:`str`)
            English name of the country
        
        is_hidden (:class:`bool`)
            True, if the country should be hidden from the list of all countries
        
        calling_codes (:obj:`list[str]`)
            List of country calling codes
        
    """

    ID: str = Field("countryInfo", alias="@type")
    country_code: str
    name: str
    english_name: str
    is_hidden: bool
    calling_codes: list[str]

    @staticmethod
    def read(q: dict) -> CountryInfo:
        return CountryInfo.construct(**q)
