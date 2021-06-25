# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

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
    
    Params:
        fill (:class:`BackgroundFill`)
            Description of the background fill
        
    """

    ID: str = Field("backgroundTypeFill", alias="@type")
    fill: BackgroundFill

    @staticmethod
    def read(q: dict) -> BackgroundTypeFill:
        return BackgroundTypeFill.construct(**q)


class BackgroundTypePattern(BackgroundType):
    """
    A PNG or TGV (gzipped subset of SVG with MIME type "application/x-tgwallpattern") pattern to be combined with the background fill chosen by the user
    
    Params:
        fill (:class:`BackgroundFill`)
            Description of the background fill
        
        intensity (:class:`int`)
            Intensity of the pattern when it is shown above the filled background; -100-100. If negative, the pattern color and the filled background colors needs to be inverted
        
        is_moving (:class:`bool`)
            True, if the background needs to be slightly moved when device is tilted
        
    """

    ID: str = Field("backgroundTypePattern", alias="@type")
    fill: BackgroundFill
    intensity: int
    is_moving: bool

    @staticmethod
    def read(q: dict) -> BackgroundTypePattern:
        return BackgroundTypePattern.construct(**q)


class BackgroundTypeWallpaper(BackgroundType):
    """
    A wallpaper in JPEG format
    
    Params:
        is_blurred (:class:`bool`)
            True, if the wallpaper must be downscaled to fit in 450x450 square and then box-blurred with radius 12
        
        is_moving (:class:`bool`)
            True, if the background needs to be slightly moved when device is tilted
        
    """

    ID: str = Field("backgroundTypeWallpaper", alias="@type")
    is_blurred: bool
    is_moving: bool

    @staticmethod
    def read(q: dict) -> BackgroundTypeWallpaper:
        return BackgroundTypeWallpaper.construct(**q)
