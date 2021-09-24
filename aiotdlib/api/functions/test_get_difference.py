# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class TestGetDifference(BaseObject):
    """
    Forces an updates.getDifference call to the Telegram servers; for testing only
    
    """

    ID: str = Field("testGetDifference", alias="@type")

    @staticmethod
    def read(q: dict) -> TestGetDifference:
        return TestGetDifference.construct(**q)
