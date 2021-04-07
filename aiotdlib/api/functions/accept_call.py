# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import CallProtocol


class AcceptCall(BaseObject):
    """
    Accepts an incoming call
    
    Params:
        call_id (:class:`int`)
            Call identifier
        
        protocol (:class:`CallProtocol`)
            Description of the call protocols supported by the application
        
    """

    ID: str = Field("acceptCall", alias="@type")
    call_id: int
    protocol: CallProtocol

    @staticmethod
    def read(q: dict) -> AcceptCall:
        return AcceptCall.construct(**q)
