# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SendCallSignalingData(BaseObject):
    """
    Sends call signaling data
    
    Params:
        call_id (:class:`int`)
            Call identifier
        
        data (:class:`str`)
            The data
        
    """

    ID: str = Field("sendCallSignalingData", alias="@type")
    call_id: int
    data: str

    @staticmethod
    def read(q: dict) -> SendCallSignalingData:
        return SendCallSignalingData.construct(**q)
