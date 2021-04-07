# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class TestSquareInt(BaseObject):
    """
    Returns the squared received number; for testing only. This is an offline method. Can be called before authorization
    
    Params:
        x (:class:`int`)
            Number to square
        
    """

    ID: str = Field("testSquareInt", alias="@type")
    x: int

    @staticmethod
    def read(q: dict) -> TestSquareInt:
        return TestSquareInt.construct(**q)
