# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .test_string import TestString
from ..base_object import BaseObject


class TestVectorStringObject(BaseObject):
    """
    A simple object containing a vector of objects that hold a string; for testing only
    
    :param value: Vector of objects
    :type value: :class:`list[TestString]`
    
    """

    ID: str = Field("testVectorStringObject", alias="@type")
    value: list[TestString]

    @staticmethod
    def read(q: dict) -> TestVectorStringObject:
        return TestVectorStringObject.construct(**q)
