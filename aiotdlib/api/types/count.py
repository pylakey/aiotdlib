# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class Count(BaseObject):
    """
    Contains a counter
    
    :param count: Count
    :type count: :class:`int`
    
    """

    ID: str = Field("count", alias="@type")
    count: int

    @staticmethod
    def read(q: dict) -> Count:
        return Count.construct(**q)
