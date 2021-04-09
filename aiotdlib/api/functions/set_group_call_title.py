# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SetGroupCallTitle(BaseObject):
    """
    Sets group call title. Requires groupCall.can_be_managed group call flag
    
    Params:
        group_call_id (:class:`int`)
            Group call identifier
        
        title (:class:`str`)
            New group call title; 1-64 characters
        
    """

    ID: str = Field("setGroupCallTitle", alias="@type")
    group_call_id: int
    title: str = Field(..., min_length=1, max_length=64)

    @staticmethod
    def read(q: dict) -> SetGroupCallTitle:
        return SetGroupCallTitle.construct(**q)
