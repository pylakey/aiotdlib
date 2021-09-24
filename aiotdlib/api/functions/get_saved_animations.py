# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetSavedAnimations(BaseObject):
    """
    Returns saved animations
    
    """

    ID: str = Field("getSavedAnimations", alias="@type")

    @staticmethod
    def read(q: dict) -> GetSavedAnimations:
        return GetSavedAnimations.construct(**q)
