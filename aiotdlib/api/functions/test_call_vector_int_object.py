# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import TestInt


class TestCallVectorIntObject(BaseObject):
    """
    Returns the received vector of objects containing a number; for testing only. This is an offline method. Can be called before authorization
    
    Params:
        x (:obj:`list[TestInt]`)
            Vector of objects to return
        
    """

    ID: str = Field("testCallVectorIntObject", alias="@type")
    x: list[TestInt]

    @staticmethod
    def read(q: dict) -> TestCallVectorIntObject:
        return TestCallVectorIntObject.construct(**q)
