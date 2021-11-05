# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ColorReplacement(BaseObject):
    """
    Describes a color replacement for animated emoji
    
    :param old_color: Original animated emoji color in the RGB24 format
    :type old_color: :class:`int`
    
    :param new_color: Replacement animated emoji color in the RGB24 format
    :type new_color: :class:`int`
    
    """

    ID: str = Field("colorReplacement", alias="@type")
    old_color: int
    new_color: int

    @staticmethod
    def read(q: dict) -> ColorReplacement:
        return ColorReplacement.construct(**q)
