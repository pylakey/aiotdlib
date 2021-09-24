# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class MaskPoint(BaseObject):
    """
    Part of the face, relative to which a mask should be placed
    
    """

    ID: str = Field("maskPoint", alias="@type")


class MaskPointChin(MaskPoint):
    """
    A mask should be placed relatively to the chin
    
    """

    ID: str = Field("maskPointChin", alias="@type")

    @staticmethod
    def read(q: dict) -> MaskPointChin:
        return MaskPointChin.construct(**q)


class MaskPointEyes(MaskPoint):
    """
    A mask should be placed relatively to the eyes
    
    """

    ID: str = Field("maskPointEyes", alias="@type")

    @staticmethod
    def read(q: dict) -> MaskPointEyes:
        return MaskPointEyes.construct(**q)


class MaskPointForehead(MaskPoint):
    """
    A mask should be placed relatively to the forehead
    
    """

    ID: str = Field("maskPointForehead", alias="@type")

    @staticmethod
    def read(q: dict) -> MaskPointForehead:
        return MaskPointForehead.construct(**q)


class MaskPointMouth(MaskPoint):
    """
    A mask should be placed relatively to the mouth
    
    """

    ID: str = Field("maskPointMouth", alias="@type")

    @staticmethod
    def read(q: dict) -> MaskPointMouth:
        return MaskPointMouth.construct(**q)
