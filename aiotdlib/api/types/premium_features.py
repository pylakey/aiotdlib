# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .internal_link_type import InternalLinkType
from .premium_feature import PremiumFeature
from .premium_limit import PremiumLimit
from ..base_object import BaseObject


class PremiumFeatures(BaseObject):
    """
    Contains information about features, available to Premium users
    
    :param features: The list of available features
    :type features: :class:`list[PremiumFeature]`
    
    :param limits: The list of limits, increased for Premium users
    :type limits: :class:`list[PremiumLimit]`
    
    :param payment_link: An internal link to be opened to pay for Telegram Premium if store payment isn't possible; may be null if direct payment isn't available, defaults to None
    :type payment_link: :class:`InternalLinkType`, optional
    
    """

    ID: str = Field("premiumFeatures", alias="@type")
    features: list[PremiumFeature]
    limits: list[PremiumLimit]
    payment_link: typing.Optional[InternalLinkType] = None

    @staticmethod
    def read(q: dict) -> PremiumFeatures:
        return PremiumFeatures.construct(**q)
