# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class Users(BaseObject):
    """
    Represents a list of users
    
    Params:
        total_count (:class:`int`)
            Approximate total count of users found
        
        user_ids (:obj:`list[int]`)
            A list of user identifiers
        
    """

    ID: str = Field("users", alias="@type")
    total_count: int
    user_ids: list[int]

    @staticmethod
    def read(q: dict) -> Users:
        return Users.construct(**q)
