# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SetUsername(BaseObject):
    """
    Changes the username of the current user
    
    :param username: The new value of the username. Use an empty string to remove the username
    :type username: :class:`str`
    
    """

    ID: str = Field("setUsername", alias="@type")
    username: str

    @staticmethod
    def read(q: dict) -> SetUsername:
        return SetUsername.construct(**q)
