# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetUserFullInfo(BaseObject):
    """
    Returns full information about a user by their identifier
    
    Params:
        user_id (:class:`int`)
            User identifier
        
    """

    ID: str = Field("getUserFullInfo", alias="@type")
    user_id: int

    @staticmethod
    def read(q: dict) -> GetUserFullInfo:
        return GetUserFullInfo.construct(**q)
