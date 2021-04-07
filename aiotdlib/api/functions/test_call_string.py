# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class TestCallString(BaseObject):
    """
    Returns the received string; for testing only. This is an offline method. Can be called before authorization
    
    Params:
        x (:class:`str`)
            String to return
        
    """

    ID: str = Field("testCallString", alias="@type")
    x: str

    @staticmethod
    def read(q: dict) -> TestCallString:
        return TestCallString.construct(**q)
