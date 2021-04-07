# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetCountries(BaseObject):
    """
    Returns information about existing countries. Can be called before authorization
    
    """

    ID: str = Field("getCountries", alias="@type")

    @staticmethod
    def read(q: dict) -> GetCountries:
        return GetCountries.construct(**q)
