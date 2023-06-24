# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetPremiumState(BaseObject):
    """
    Returns state of Telegram Premium subscription and promotion videos for Premium features
    """

    ID: typing.Literal["getPremiumState"] = "getPremiumState"
