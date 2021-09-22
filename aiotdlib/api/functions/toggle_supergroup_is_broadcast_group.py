# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ToggleSupergroupIsBroadcastGroup(BaseObject):
    """
    Upgrades supergroup to a broadcast group; requires owner privileges in the supergroup
    
    :param supergroup_id: Identifier of the supergroup
    :type supergroup_id: :class:`int`
    
    """

    ID: str = Field("toggleSupergroupIsBroadcastGroup", alias="@type")
    supergroup_id: int

    @staticmethod
    def read(q: dict) -> ToggleSupergroupIsBroadcastGroup:
        return ToggleSupergroupIsBroadcastGroup.construct(**q)
