# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetMe(BaseObject):
    """
    Returns the current user
    
    """

    ID: str = Field("getMe", alias="@type")

    @staticmethod
    def read(q: dict) -> GetMe:
        return GetMe.construct(**q)
