# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .premium_feature import PremiumFeature
from .premium_limit_type import PremiumLimitType
from ..base_object import BaseObject


class PremiumSource(BaseObject):
    """
    Describes a source from which the Premium features screen is opened
    
    """

    ID: str = Field("premiumSource", alias="@type")


class PremiumSourceFeature(PremiumSource):
    """
    A user tried to use a Premium feature
    
    :param feature: The used feature
    :type feature: :class:`PremiumFeature`
    
    """

    ID: str = Field("premiumSourceFeature", alias="@type")
    feature: PremiumFeature

    @staticmethod
    def read(q: dict) -> PremiumSourceFeature:
        return PremiumSourceFeature.construct(**q)


class PremiumSourceLimitExceeded(PremiumSource):
    """
    A limit was exceeded
    
    :param limit_type: Type of the exceeded limit
    :type limit_type: :class:`PremiumLimitType`
    
    """

    ID: str = Field("premiumSourceLimitExceeded", alias="@type")
    limit_type: PremiumLimitType

    @staticmethod
    def read(q: dict) -> PremiumSourceLimitExceeded:
        return PremiumSourceLimitExceeded.construct(**q)


class PremiumSourceLink(PremiumSource):
    """
    A user opened an internal link of the type internalLinkTypePremiumFeatures
    
    :param referrer: The referrer from the link
    :type referrer: :class:`str`
    
    """

    ID: str = Field("premiumSourceLink", alias="@type")
    referrer: str

    @staticmethod
    def read(q: dict) -> PremiumSourceLink:
        return PremiumSourceLink.construct(**q)


class PremiumSourceSettings(PremiumSource):
    """
    A user opened the Premium features screen from settings
    
    """

    ID: str = Field("premiumSourceSettings", alias="@type")

    @staticmethod
    def read(q: dict) -> PremiumSourceSettings:
        return PremiumSourceSettings.construct(**q)
