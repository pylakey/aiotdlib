# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ClickPremiumSubscriptionButton(BaseObject):
    """
    Informs TDLib that the user clicked Premium subscription button on the Premium features screen
    
    """

    ID: str = Field("clickPremiumSubscriptionButton", alias="@type")

    @staticmethod
    def read(q: dict) -> ClickPremiumSubscriptionButton:
        return ClickPremiumSubscriptionButton.construct(**q)
