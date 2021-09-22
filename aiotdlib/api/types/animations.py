# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .animation import Animation
from ..base_object import BaseObject


class Animations(BaseObject):
    """
    Represents a list of animations
    
    :param animations: List of animations
    :type animations: :class:`list[Animation]`
    
    """

    ID: str = Field("animations", alias="@type")
    animations: list[Animation]

    @staticmethod
    def read(q: dict) -> Animations:
        return Animations.construct(**q)
