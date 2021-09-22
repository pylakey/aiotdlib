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


class Countries(BaseObject):
    """
    Contains information about countries
    
    :param countries: The list of countries
    :type countries: :class:`list[CountryInfo]`
    
    """

    ID: str = Field("countries", alias="@type")
    countries: list[CountryInfo]

    @staticmethod
    def read(q: dict) -> Countries:
        return Countries.construct(**q)
