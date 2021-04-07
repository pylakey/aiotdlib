# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .point import Point
from ..base_object import BaseObject


class VectorPathCommand(BaseObject):
    """
    Represents a vector path command
    
    """

    ID: str = Field("vectorPathCommand", alias="@type")


class VectorPathCommandCubicBezierCurve(VectorPathCommand):
    """
    A cubic Bézier curve to a given point
    
    Params:
        start_control_point (:class:`Point`)
            The start control point of the curve
        
        end_control_point (:class:`Point`)
            The end control point of the curve
        
        end_point (:class:`Point`)
            The end point of the curve
        
    """

    ID: str = Field("vectorPathCommandCubicBezierCurve", alias="@type")
    start_control_point: Point
    end_control_point: Point
    end_point: Point

    @staticmethod
    def read(q: dict) -> VectorPathCommandCubicBezierCurve:
        return VectorPathCommandCubicBezierCurve.construct(**q)


class VectorPathCommandLine(VectorPathCommand):
    """
    A straight line to a given point
    
    Params:
        end_point (:class:`Point`)
            The end point of the straight line
        
    """

    ID: str = Field("vectorPathCommandLine", alias="@type")
    end_point: Point

    @staticmethod
    def read(q: dict) -> VectorPathCommandLine:
        return VectorPathCommandLine.construct(**q)
