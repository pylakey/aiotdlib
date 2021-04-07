# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class TestUseUpdate(BaseObject):
    """
    Does nothing and ensures that the Update object is used; for testing only. This is an offline method. Can be called before authorization
    
    """

    ID: str = Field("testUseUpdate", alias="@type")

    @staticmethod
    def read(q: dict) -> TestUseUpdate:
        return TestUseUpdate.construct(**q)
