# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class TestUseUpdate(BaseObject):
    """
    Does nothing and ensures that the Update object is used; for testing only. This is an offline method. Can be called before authorization
    """

    ID: typing.Literal["testUseUpdate"] = "testUseUpdate"
