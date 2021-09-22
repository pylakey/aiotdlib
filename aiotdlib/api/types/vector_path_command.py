# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

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
    
    :param start_control_point: The start control point of the curve
    :type start_control_point: :class:`Point`
    
    :param end_control_point: The end control point of the curve
    :type end_control_point: :class:`Point`
    
    :param end_point: The end point of the curve
    :type end_point: :class:`Point`
    
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
    
    :param end_point: The end point of the straight line
    :type end_point: :class:`Point`
    
    """

    ID: str = Field("vectorPathCommandLine", alias="@type")
    end_point: Point

    @staticmethod
    def read(q: dict) -> VectorPathCommandLine:
        return VectorPathCommandLine.construct(**q)
