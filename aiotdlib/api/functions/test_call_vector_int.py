# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class TestCallVectorInt(BaseObject):
    """
    Returns the received vector of numbers; for testing only. This is an offline method. Can be called before authorization
    
    Params:
        x (:obj:`list[int]`)
            Vector of numbers to return
        
    """

    ID: str = Field("testCallVectorInt", alias="@type")
    x: list[int]

    @staticmethod
    def read(q: dict) -> TestCallVectorInt:
        return TestCallVectorInt.construct(**q)
