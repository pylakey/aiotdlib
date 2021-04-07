# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class TestCallEmpty(BaseObject):
    """
    Does nothing; for testing only. This is an offline method. Can be called before authorization
    
    """

    ID: str = Field("testCallEmpty", alias="@type")

    @staticmethod
    def read(q: dict) -> TestCallEmpty:
        return TestCallEmpty.construct(**q)
