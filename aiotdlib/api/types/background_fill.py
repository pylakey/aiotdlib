# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class BackgroundFill(BaseObject):
    """
    Describes a fill of a background
    
    """

    ID: str = Field("backgroundFill", alias="@type")


class BackgroundFillGradient(BackgroundFill):
    """
    Describes a gradient fill of a background
    
    Params:
        top_color (:class:`int`)
            A top color of the background in the RGB24 format
        
        bottom_color (:class:`int`)
            A bottom color of the background in the RGB24 format
        
        rotation_angle (:class:`int`)
            Clockwise rotation angle of the gradient, in degrees; 0-359. Should be always divisible by 45
        
    """

    ID: str = Field("backgroundFillGradient", alias="@type")
    top_color: int
    bottom_color: int
    rotation_angle: int

    @staticmethod
    def read(q: dict) -> BackgroundFillGradient:
        return BackgroundFillGradient.construct(**q)


class BackgroundFillSolid(BackgroundFill):
    """
    Describes a solid fill of a background
    
    Params:
        color (:class:`int`)
            A color of the background in the RGB24 format
        
    """

    ID: str = Field("backgroundFillSolid", alias="@type")
    color: int

    @staticmethod
    def read(q: dict) -> BackgroundFillSolid:
        return BackgroundFillSolid.construct(**q)
