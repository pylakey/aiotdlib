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
    
    :param for_dark_theme: Pass true to order returned backgrounds for a dark theme
    :type for_dark_theme: :class:`bool`
    
    """

    ID: str = Field("getBackgrounds", alias="@type")
    for_dark_theme: bool

    @staticmethod
    def read(q: dict) -> GetBackgrounds:
        return GetBackgrounds.construct(**q)
