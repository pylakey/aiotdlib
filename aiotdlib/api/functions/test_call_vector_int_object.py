# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import TestInt
from ..base_object import BaseObject


class TestCallVectorIntObject(BaseObject):
    """
    Returns the received vector of objects containing a number; for testing only. This is an offline method. Can be called before authorization
    
    :param x: Vector of objects to return
    :type x: :class:`list[TestInt]`
    
    """

    ID: str = Field("testCallVectorIntObject", alias="@type")
    x: list[TestInt]

    @staticmethod
    def read(q: dict) -> TestCallVectorIntObject:
        return TestCallVectorIntObject.construct(**q)
