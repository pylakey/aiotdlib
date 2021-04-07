# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .background import Background
from ..base_object import BaseObject


class Backgrounds(BaseObject):
    """
    Contains a list of backgrounds
    
    Params:
        backgrounds (:obj:`list[Background]`)
            A list of backgrounds
        
    """

    ID: str = Field("backgrounds", alias="@type")
    backgrounds: list[Background]

    @staticmethod
    def read(q: dict) -> Backgrounds:
        return Backgrounds.construct(**q)
