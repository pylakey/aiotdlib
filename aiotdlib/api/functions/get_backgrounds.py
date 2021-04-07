# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetBackgrounds(BaseObject):
    """
    Returns backgrounds installed by the user
    
    Params:
        for_dark_theme (:class:`bool`)
            True, if the backgrounds must be ordered for dark theme
        
    """

    ID: str = Field("getBackgrounds", alias="@type")
    for_dark_theme: bool

    @staticmethod
    def read(q: dict) -> GetBackgrounds:
        return GetBackgrounds.construct(**q)
