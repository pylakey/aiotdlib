# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class TestCallEmpty(BaseObject):
    """
    Does nothing; for testing only. This is an offline method. Can be called before authorization
    """

    ID: typing.Literal["testCallEmpty"] = "testCallEmpty"
