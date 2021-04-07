# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetSupportUser(BaseObject):
    """
    Returns a user that can be contacted to get support
    
    """

    ID: str = Field("getSupportUser", alias="@type")

    @staticmethod
    def read(q: dict) -> GetSupportUser:
        return GetSupportUser.construct(**q)
