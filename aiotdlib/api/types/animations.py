# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .animation import Animation
from ..base_object import BaseObject


class Animations(BaseObject):
    """
    Represents a list of animations
    
    Params:
        animations (:obj:`list[Animation]`)
            List of animations
        
    """

    ID: str = Field("animations", alias="@type")
    animations: list[Animation]

    @staticmethod
    def read(q: dict) -> Animations:
        return Animations.construct(**q)
