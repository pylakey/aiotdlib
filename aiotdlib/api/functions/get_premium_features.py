# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import PremiumSource


class GetPremiumFeatures(BaseObject):
    """
    Returns information about features, available to Premium users
    
    :param source: Source of the request; pass null if the method is called from some non-standard source
    :type source: :class:`PremiumSource`
    
    """

    ID: str = Field("getPremiumFeatures", alias="@type")
    source: PremiumSource

    @staticmethod
    def read(q: dict) -> GetPremiumFeatures:
        return GetPremiumFeatures.construct(**q)
