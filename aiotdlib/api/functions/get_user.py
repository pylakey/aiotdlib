# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetUser(BaseObject):
    """
    Returns information about a user by their identifier. This is an offline request if the current user is not a bot
    
    :param user_id: User identifier
    :type user_id: :class:`int`
    
    """

    ID: str = Field("getUser", alias="@type")
    user_id: int

    @staticmethod
    def read(q: dict) -> GetUser:
        return GetUser.construct(**q)
