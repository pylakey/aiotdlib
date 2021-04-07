# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetBasicGroup(BaseObject):
    """
    Returns information about a basic group by its identifier. This is an offline request if the current user is not a bot
    
    Params:
        basic_group_id (:class:`int`)
            Basic group identifier
        
    """

    ID: str = Field("getBasicGroup", alias="@type")
    basic_group_id: int

    @staticmethod
    def read(q: dict) -> GetBasicGroup:
        return GetBasicGroup.construct(**q)
