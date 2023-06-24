# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ResetNetworkStatistics(BaseObject):
    """
    Resets all network data usage statistics to zero. Can be called before authorization
    """

    ID: typing.Literal["resetNetworkStatistics"] = "resetNetworkStatistics"
