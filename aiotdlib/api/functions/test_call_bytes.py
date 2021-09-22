# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class TestCallBytes(BaseObject):
    """
    Returns the received bytes; for testing only. This is an offline method. Can be called before authorization
    
    :param x: Bytes to return
    :type x: :class:`str`
    
    """

    ID: str = Field("testCallBytes", alias="@type")
    x: str

    @staticmethod
    def read(q: dict) -> TestCallBytes:
        return TestCallBytes.construct(**q)
