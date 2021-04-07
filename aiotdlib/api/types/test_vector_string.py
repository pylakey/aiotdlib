# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class TestVectorString(BaseObject):
    """
    A simple object containing a vector of strings; for testing only
    
    Params:
        value (:obj:`list[str]`)
            Vector of strings
        
    """

    ID: str = Field("testVectorString", alias="@type")
    value: list[str]

    @staticmethod
    def read(q: dict) -> TestVectorString:
        return TestVectorString.construct(**q)
