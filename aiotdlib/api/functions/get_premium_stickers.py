# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetPremiumStickers(BaseObject):
    """
    Returns examples of premium stickers for demonstration purposes
    
    """

    ID: str = Field("getPremiumStickers", alias="@type")

    @staticmethod
    def read(q: dict) -> GetPremiumStickers:
        return GetPremiumStickers.construct(**q)
