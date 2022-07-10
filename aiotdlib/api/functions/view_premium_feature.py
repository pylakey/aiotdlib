# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import PremiumFeature


class ViewPremiumFeature(BaseObject):
    """
    Informs TDLib that the user viewed detailed information about a Premium feature on the Premium features screen
    
    :param feature: The viewed premium feature
    :type feature: :class:`PremiumFeature`
    
    """

    ID: str = Field("viewPremiumFeature", alias="@type")
    feature: PremiumFeature

    @staticmethod
    def read(q: dict) -> ViewPremiumFeature:
        return ViewPremiumFeature.construct(**q)
