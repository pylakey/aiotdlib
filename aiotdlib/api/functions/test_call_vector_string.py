# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class TestCallVectorString(BaseObject):
    """
    Returns the received vector of strings; for testing only. This is an offline method. Can be called before authorization
    
    :param x: Vector of strings to return
    :type x: :class:`list[str]`
    
    """

    ID: str = Field("testCallVectorString", alias="@type")
    x: list[str]

    @staticmethod
    def read(q: dict) -> TestCallVectorString:
        return TestCallVectorString.construct(**q)
