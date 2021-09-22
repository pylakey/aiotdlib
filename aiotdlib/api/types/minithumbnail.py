# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class Minithumbnail(BaseObject):
    """
    Thumbnail image of a very poor quality and low resolution
    
    :param width: Thumbnail width, usually doesn't exceed 40
    :type width: :class:`int`
    
    :param height: Thumbnail height, usually doesn't exceed 40
    :type height: :class:`int`
    
    :param data: The thumbnail in JPEG format
    :type data: :class:`str`
    
    """

    ID: str = Field("minithumbnail", alias="@type")
    width: int
    height: int
    data: str

    @staticmethod
    def read(q: dict) -> Minithumbnail:
        return Minithumbnail.construct(**q)
