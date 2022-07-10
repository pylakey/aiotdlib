# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .premium_limit_type import PremiumLimitType
from ..base_object import BaseObject


class PremiumLimit(BaseObject):
    """
    Contains information about a limit, increased for Premium users
    
    :param type_: The type of the limit
    :type type_: :class:`PremiumLimitType`
    
    :param default_value: Default value of the limit
    :type default_value: :class:`int`
    
    :param premium_value: Value of the limit for Premium users
    :type premium_value: :class:`int`
    
    """

    ID: str = Field("premiumLimit", alias="@type")
    type_: PremiumLimitType = Field(..., alias='type')
    default_value: int
    premium_value: int

    @staticmethod
    def read(q: dict) -> PremiumLimit:
        return PremiumLimit.construct(**q)
