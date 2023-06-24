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
    TestInt,
)


class TestCallVectorIntObject(BaseObject):
    """
    Returns the received vector of objects containing a number; for testing only. This is an offline method. Can be called before authorization

    :param x: Vector of objects to return
    :type x: :class:`Vector[TestInt]`
    """

    ID: typing.Literal["testCallVectorIntObject"] = "testCallVectorIntObject"
    x: Vector[TestInt]
