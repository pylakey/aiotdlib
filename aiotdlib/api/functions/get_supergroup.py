# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetSupergroup(BaseObject):
    """
    Returns information about a supergroup or a channel by its identifier. This is an offline request if the current user is not a bot
    
    Params:
        supergroup_id (:class:`int`)
            Supergroup or channel identifier
        
    """

    ID: str = Field("getSupergroup", alias="@type")
    supergroup_id: int

    @staticmethod
    def read(q: dict) -> GetSupergroup:
        return GetSupergroup.construct(**q)
