# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SetUsername(BaseObject):
    """
    Changes the username of the current user
    
    Params:
        username (:class:`str`)
            The new value of the username. Use an empty string to remove the username
        
    """

    ID: str = Field("setUsername", alias="@type")
    username: str

    @staticmethod
    def read(q: dict) -> SetUsername:
        return SetUsername.construct(**q)
