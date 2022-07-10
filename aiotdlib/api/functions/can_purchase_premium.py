# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CanPurchasePremium(BaseObject):
    """
    Checks whether Telegram Premium purchase is possible. Must be called before in-store Premium purchase
    
    """

    ID: str = Field("canPurchasePremium", alias="@type")

    @staticmethod
    def read(q: dict) -> CanPurchasePremium:
        return CanPurchasePremium.construct(**q)
