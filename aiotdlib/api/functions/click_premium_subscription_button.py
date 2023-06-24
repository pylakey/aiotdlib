# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ClickPremiumSubscriptionButton(BaseObject):
    """
    Informs TDLib that the user clicked Premium subscription button on the Premium features screen
    """

    ID: typing.Literal["clickPremiumSubscriptionButton"] = "clickPremiumSubscriptionButton"
