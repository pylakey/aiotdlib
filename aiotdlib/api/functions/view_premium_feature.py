# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    PremiumFeature,
)


class ViewPremiumFeature(BaseObject):
    """
    Informs TDLib that the user viewed detailed information about a Premium feature on the Premium features screen

    :param feature: The viewed premium feature
    :type feature: :class:`PremiumFeature`
    """

    ID: typing.Literal["viewPremiumFeature"] = "viewPremiumFeature"
    feature: PremiumFeature
