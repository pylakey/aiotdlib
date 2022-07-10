# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .animation import Animation
from .premium_feature import PremiumFeature
from ..base_object import BaseObject


class PremiumFeaturePromotionAnimation(BaseObject):
    """
    Describes a promotion animation for a Premium feature
    
    :param feature: Premium feature
    :type feature: :class:`PremiumFeature`
    
    :param animation: Promotion animation for the feature
    :type animation: :class:`Animation`
    
    """

    ID: str = Field("premiumFeaturePromotionAnimation", alias="@type")
    feature: PremiumFeature
    animation: Animation

    @staticmethod
    def read(q: dict) -> PremiumFeaturePromotionAnimation:
        return PremiumFeaturePromotionAnimation.construct(**q)
