# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class TestInt(BaseObject):
    """
    A simple object containing a number; for testing only
    
    Params:
        value (:class:`int`)
            Number
        
    """

    ID: str = Field("testInt", alias="@type")
    value: int

    @staticmethod
    def read(q: dict) -> TestInt:
        return TestInt.construct(**q)
