# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetCountryCode(BaseObject):
    """
    Uses the current IP address to find the current country. Returns two-letter ISO 3166-1 alpha-2 country code. Can be called before authorization
    
    """

    ID: str = Field("getCountryCode", alias="@type")

    @staticmethod
    def read(q: dict) -> GetCountryCode:
        return GetCountryCode.construct(**q)
