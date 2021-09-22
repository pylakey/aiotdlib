# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .mask_point import MaskPoint
from ..base_object import BaseObject


class MaskPosition(BaseObject):
    """
    Position on a photo where a mask should be placed
    
    :param point: Part of the face, relative to which the mask should be placed
    :type point: :class:`MaskPoint`
    
    :param x_shift: Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. (For example, -1.0 will place the mask just to the left of the default mask position)
    :type x_shift: :class:`float`
    
    :param y_shift: Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. (For example, 1.0 will place the mask just below the default mask position)
    :type y_shift: :class:`float`
    
    :param scale: Mask scaling coefficient. (For example, 2.0 means a doubled size)
    :type scale: :class:`float`
    
    """

    ID: str = Field("maskPosition", alias="@type")
    point: MaskPoint
    x_shift: float
    y_shift: float
    scale: float

    @staticmethod
    def read(q: dict) -> MaskPosition:
        return MaskPosition.construct(**q)
