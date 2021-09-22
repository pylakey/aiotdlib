# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class CountryInfo(BaseObject):
    """
    Contains information about a country
    
    :param country_code: A two-letter ISO 3166-1 alpha-2 country code
    :type country_code: :class:`str`
    
    :param name: Native name of the country
    :type name: :class:`str`
    
    :param english_name: English name of the country
    :type english_name: :class:`str`
    
    :param is_hidden: True, if the country should be hidden from the list of all countries
    :type is_hidden: :class:`bool`
    
    :param calling_codes: List of country calling codes
    :type calling_codes: :class:`list[str]`
    
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
