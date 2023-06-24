# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class TestGetDifference(BaseObject):
    """
    Forces an updates.getDifference call to the Telegram servers; for testing only
    """

    ID: typing.Literal["testGetDifference"] = "testGetDifference"
