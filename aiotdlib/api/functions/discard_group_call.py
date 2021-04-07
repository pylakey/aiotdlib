# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class DiscardGroupCall(BaseObject):
    """
    Discards a group call. Requires groupCall.can_be_managed
    
    Params:
        group_call_id (:class:`int`)
            Group call identifier
        
    """

    ID: str = Field("discardGroupCall", alias="@type")
    group_call_id: int

    @staticmethod
    def read(q: dict) -> DiscardGroupCall:
        return DiscardGroupCall.construct(**q)
