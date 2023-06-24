# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class TestCallVectorInt(BaseObject):
    """
    Returns the received vector of numbers; for testing only. This is an offline method. Can be called before authorization

    :param x: Vector of numbers to return
    :type x: :class:`Vector[Int32]`
    """

    ID: typing.Literal["testCallVectorInt"] = "testCallVectorInt"
    x: Vector[Int32]
