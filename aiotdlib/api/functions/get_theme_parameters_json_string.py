# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import ThemeParameters


class GetThemeParametersJsonString(BaseObject):
    """
    Converts a themeParameters object to corresponding JSON-serialized string. Can be called synchronously
    
    :param theme: Theme parameters to convert to JSON
    :type theme: :class:`ThemeParameters`
    
    """

    ID: str = Field("getThemeParametersJsonString", alias="@type")
    theme: ThemeParameters

    @staticmethod
    def read(q: dict) -> GetThemeParametersJsonString:
        return GetThemeParametersJsonString.construct(**q)
