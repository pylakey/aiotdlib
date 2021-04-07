# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ResetBackgrounds(BaseObject):
    """
    Resets list of installed backgrounds to its default value
    
    """

    ID: str = Field("resetBackgrounds", alias="@type")

    @staticmethod
    def read(q: dict) -> ResetBackgrounds:
        return ResetBackgrounds.construct(**q)
