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
    
    :param total_count: Approximate total number of users found
    :type total_count: :class:`int`
    
    :param user_ids: A list of user identifiers
    :type user_ids: :class:`list[int]`
    
    """

    ID: str = Field("users", alias="@type")
    total_count: int
    user_ids: list[int]

    @staticmethod
    def read(q: dict) -> Users:
        return Users.construct(**q)
