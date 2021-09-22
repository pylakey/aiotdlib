# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class BackgroundFill(BaseObject):
    """
    Describes a fill of a background
    
    """

    ID: str = Field("backgroundFill", alias="@type")


class BackgroundFillFreeformGradient(BackgroundFill):
    """
    Describes a freeform gradient fill of a background
    
    :param colors: A list of 3 or 4 colors of the freeform gradients in the RGB24 format
    :type colors: :class:`list[int]`
    
    """

    ID: str = Field("backgroundFillFreeformGradient", alias="@type")
    colors: list[int]

    @staticmethod
    def read(q: dict) -> BackgroundFillFreeformGradient:
        return BackgroundFillFreeformGradient.construct(**q)


class BackgroundFillGradient(BackgroundFill):
    """
    Describes a gradient fill of a background
    
    :param top_color: A top color of the background in the RGB24 format
    :type top_color: :class:`int`
    
    :param bottom_color: A bottom color of the background in the RGB24 format
    :type bottom_color: :class:`int`
    
    :param rotation_angle: Clockwise rotation angle of the gradient, in degrees; 0-359. Should be always divisible by 45
    :type rotation_angle: :class:`int`
    
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
    
    :param color: A color of the background in the RGB24 format
    :type color: :class:`int`
    
    """

    ID: str = Field("backgroundFillSolid", alias="@type")
    color: int

    @staticmethod
    def read(q: dict) -> BackgroundFillSolid:
        return BackgroundFillSolid.construct(**q)
