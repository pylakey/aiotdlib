# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .background_fill import BackgroundFill
from ..base_object import BaseObject


class BackgroundType(BaseObject):
    """
    Describes the type of a background
    
    """

    ID: str = Field("backgroundType", alias="@type")


class BackgroundTypeFill(BackgroundType):
    """
    A filled background
    
    :param fill: Description of the background fill
    :type fill: :class:`BackgroundFill`
    
    """

    ID: str = Field("backgroundTypeFill", alias="@type")
    fill: BackgroundFill

    @staticmethod
    def read(q: dict) -> BackgroundTypeFill:
        return BackgroundTypeFill.construct(**q)


class BackgroundTypePattern(BackgroundType):
    """
    A PNG or TGV (gzipped subset of SVG with MIME type "application/x-tgwallpattern") pattern to be combined with the background fill chosen by the user
    
    :param fill: Description of the background fill
    :type fill: :class:`BackgroundFill`
    
    :param intensity: Intensity of the pattern when it is shown above the filled background; 0-100.
    :type intensity: :class:`int`
    
    :param is_inverted: True, if the background fill must be applied only to the pattern itself. All other pixels are black in this case. For dark themes only
    :type is_inverted: :class:`bool`
    
    :param is_moving: True, if the background needs to be slightly moved when device is tilted
    :type is_moving: :class:`bool`
    
    """

    ID: str = Field("backgroundTypePattern", alias="@type")
    fill: BackgroundFill
    intensity: int
    is_inverted: bool
    is_moving: bool

    @staticmethod
    def read(q: dict) -> BackgroundTypePattern:
        return BackgroundTypePattern.construct(**q)


class BackgroundTypeWallpaper(BackgroundType):
    """
    A wallpaper in JPEG format
    
    :param is_blurred: True, if the wallpaper must be downscaled to fit in 450x450 square and then box-blurred with radius 12
    :type is_blurred: :class:`bool`
    
    :param is_moving: True, if the background needs to be slightly moved when device is tilted
    :type is_moving: :class:`bool`
    
    """

    ID: str = Field("backgroundTypeWallpaper", alias="@type")
    is_blurred: bool
    is_moving: bool

    @staticmethod
    def read(q: dict) -> BackgroundTypeWallpaper:
        return BackgroundTypeWallpaper.construct(**q)
