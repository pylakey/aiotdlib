# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SetSupergroupUsername(BaseObject):
    """
    Changes the username of a supergroup or channel, requires owner privileges in the supergroup or channel
    
    :param supergroup_id: Identifier of the supergroup or channel
    :type supergroup_id: :class:`int`
    
    :param username: New value of the username. Use an empty string to remove the username
    :type username: :class:`str`
    
    """

    ID: str = Field("setSupergroupUsername", alias="@type")
    supergroup_id: int
    username: str

    @staticmethod
    def read(q: dict) -> SetSupergroupUsername:
        return SetSupergroupUsername.construct(**q)
