# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class TestBytes(BaseObject):
    """
    A simple object containing a sequence of bytes; for testing only
    
    Params:
        value (:class:`str`)
            Bytes
        
    """

    ID: str = Field("testBytes", alias="@type")
    value: str

    @staticmethod
    def read(q: dict) -> TestBytes:
        return TestBytes.construct(**q)
