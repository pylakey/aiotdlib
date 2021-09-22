# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .test_int import TestInt
from ..base_object import BaseObject


class TestVectorIntObject(BaseObject):
    """
    A simple object containing a vector of objects that hold a number; for testing only
    
    :param value: Vector of objects
    :type value: :class:`list[TestInt]`
    
    """

    ID: str = Field("testVectorIntObject", alias="@type")
    value: list[TestInt]

    @staticmethod
    def read(q: dict) -> TestVectorIntObject:
        return TestVectorIntObject.construct(**q)
