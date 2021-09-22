# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class CustomRequestResult(BaseObject):
    """
    Contains the result of a custom request
    
    :param result: A JSON-serialized result
    :type result: :class:`str`
    
    """

    ID: str = Field("customRequestResult", alias="@type")
    result: str

    @staticmethod
    def read(q: dict) -> CustomRequestResult:
        return CustomRequestResult.construct(**q)
