# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class Minithumbnail(BaseObject):
    """
    Thumbnail image of a very poor quality and low resolution
    
    Params:
        width (:class:`int`)
            Thumbnail width, usually doesn't exceed 40
        
        height (:class:`int`)
            Thumbnail height, usually doesn't exceed 40
        
        data (:class:`str`)
            The thumbnail in JPEG format
        
    """

    ID: str = Field("minithumbnail", alias="@type")
    width: int
    height: int
    data: str

    @staticmethod
    def read(q: dict) -> Minithumbnail:
        return Minithumbnail.construct(**q)
