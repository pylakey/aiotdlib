# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SetSupergroupUsername(BaseObject):
    """
    Changes the username of a supergroup or channel, requires owner privileges in the supergroup or channel
    
    Params:
        supergroup_id (:class:`int`)
            Identifier of the supergroup or channel
        
        username (:class:`str`)
            New value of the username. Use an empty string to remove the username
        
    """

    ID: str = Field("setSupergroupUsername", alias="@type")
    supergroup_id: int
    username: str

    @staticmethod
    def read(q: dict) -> SetSupergroupUsername:
        return SetSupergroupUsername.construct(**q)
