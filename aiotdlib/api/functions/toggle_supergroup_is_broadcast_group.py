# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ToggleSupergroupIsBroadcastGroup(BaseObject):
    """
    Upgrades supergroup to a broadcast group; requires owner privileges in the supergroup
    
    Params:
        supergroup_id (:class:`int`)
            Identifier of the supergroup
        
    """

    ID: str = Field("toggleSupergroupIsBroadcastGroup", alias="@type")
    supergroup_id: int

    @staticmethod
    def read(q: dict) -> ToggleSupergroupIsBroadcastGroup:
        return ToggleSupergroupIsBroadcastGroup.construct(**q)
