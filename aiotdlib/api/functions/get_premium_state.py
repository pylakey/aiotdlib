# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetPremiumState(BaseObject):
    """
    Returns state of Telegram Premium subscription and promotion videos for Premium features
    
    """

    ID: str = Field("getPremiumState", alias="@type")

    @staticmethod
    def read(q: dict) -> GetPremiumState:
        return GetPremiumState.construct(**q)
