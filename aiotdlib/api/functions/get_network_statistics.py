# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetNetworkStatistics(BaseObject):
    """
    Returns network data usage statistics. Can be called before authorization

    :param only_current: Pass true to get statistics only for the current library launch
    :type only_current: :class:`Bool`
    """

    ID: typing.Literal["getNetworkStatistics"] = "getNetworkStatistics"
    only_current: Bool = False
