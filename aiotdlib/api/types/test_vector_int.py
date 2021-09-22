# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class TestVectorInt(BaseObject):
    """
    A simple object containing a vector of numbers; for testing only
    
    :param value: Vector of numbers
    :type value: :class:`list[int]`
    
    """

    ID: str = Field("testVectorInt", alias="@type")
    value: list[int]

    @staticmethod
    def read(q: dict) -> TestVectorInt:
        return TestVectorInt.construct(**q)
