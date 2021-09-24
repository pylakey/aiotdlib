# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class TestNetwork(BaseObject):
    """
    Sends a simple network request to the Telegram servers; for testing only. Can be called before authorization
    
    """

    ID: str = Field("testNetwork", alias="@type")

    @staticmethod
    def read(q: dict) -> TestNetwork:
        return TestNetwork.construct(**q)
