# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .mask_point import MaskPoint
from ..base_object import BaseObject


class MaskPosition(BaseObject):
    """
    Position on a photo where a mask should be placed
    
    Params:
        point (:class:`MaskPoint`)
            Part of the face, relative to which the mask should be placed
        
        x_shift (:class:`float`)
            Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. (For example, -1.0 will place the mask just to the left of the default mask position)
        
        y_shift (:class:`float`)
            Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. (For example, 1.0 will place the mask just below the default mask position)
        
        scale (:class:`float`)
            Mask scaling coefficient. (For example, 2.0 means a doubled size)
        
    """

    ID: str = Field("maskPosition", alias="@type")
    point: MaskPoint
    x_shift: float
    y_shift: float
    scale: float

    @staticmethod
    def read(q: dict) -> MaskPosition:
        return MaskPosition.construct(**q)
