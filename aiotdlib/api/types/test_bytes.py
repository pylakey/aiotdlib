# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class TestBytes(BaseObject):
    """
    A simple object containing a sequence of bytes; for testing only
    
    :param value: Bytes
    :type value: :class:`str`
    
    """

    ID: str = Field("testBytes", alias="@type")
    value: str

    @staticmethod
    def read(q: dict) -> TestBytes:
        return TestBytes.construct(**q)
