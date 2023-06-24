# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetAlarm(BaseObject):
    """
    Succeeds after a specified amount of time has passed. Can be called before initialization

    :param seconds: Number of seconds before the function returns
    :type seconds: :class:`Double`
    """

    ID: typing.Literal["setAlarm"] = "setAlarm"
    seconds: Double
