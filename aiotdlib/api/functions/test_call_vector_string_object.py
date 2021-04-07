# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import TestString


class TestCallVectorStringObject(BaseObject):
    """
    Returns the received vector of objects containing a string; for testing only. This is an offline method. Can be called before authorization
    
    Params:
        x (:obj:`list[TestString]`)
            Vector of objects to return
        
    """

    ID: str = Field("testCallVectorStringObject", alias="@type")
    x: list[TestString]

    @staticmethod
    def read(q: dict) -> TestCallVectorStringObject:
        return TestCallVectorStringObject.construct(**q)
