# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class Point(BaseObject):
    """
    A point on a Cartesian plane
    
    Params:
        x (:class:`float`)
            The point's first coordinate
        
        y (:class:`float`)
            The point's second coordinate
        
    """

    ID: str = Field("point", alias="@type")
    x: float
    y: float

    @staticmethod
    def read(q: dict) -> Point:
        return Point.construct(**q)
