# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class Point(BaseObject):
    """
    A point on a Cartesian plane
    
    :param x: The point's first coordinate
    :type x: :class:`float`
    
    :param y: The point's second coordinate
    :type y: :class:`float`
    
    """

    ID: str = Field("point", alias="@type")
    x: float
    y: float

    @staticmethod
    def read(q: dict) -> Point:
        return Point.construct(**q)
