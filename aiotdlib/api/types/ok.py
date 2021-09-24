# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class Ok(BaseObject):
    """
    An object of this type is returned on a successful function call for certain functions
    
    """

    ID: str = Field("ok", alias="@type")

    @staticmethod
    def read(q: dict) -> Ok:
        return Ok.construct(**q)
