# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class TestNetwork(BaseObject):
    """
    Sends a simple network request to the Telegram servers; for testing only. Can be called before authorization
    """

    ID: typing.Literal["testNetwork"] = "testNetwork"
