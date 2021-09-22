# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class TestString(BaseObject):
    """
    A simple object containing a string; for testing only
    
    :param value: String
    :type value: :class:`str`
    
    """

    ID: str = Field("testString", alias="@type")
    value: str

    @staticmethod
    def read(q: dict) -> TestString:
        return TestString.construct(**q)
