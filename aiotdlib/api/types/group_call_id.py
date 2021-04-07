# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GroupCallId(BaseObject):
    """
    Contains the group call identifier
    
    Params:
        id (:class:`int`)
            Group call identifier
        
    """

    ID: str = Field("groupCallId", alias="@type")
    id: int

    @staticmethod
    def read(q: dict) -> GroupCallId:
        return GroupCallId.construct(**q)
