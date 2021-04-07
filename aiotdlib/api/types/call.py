# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .call_state import CallState
from ..base_object import BaseObject


class Call(BaseObject):
    """
    Describes a call
    
    Params:
        id (:class:`int`)
            Call identifier, not persistent
        
        user_id (:class:`int`)
            Peer user identifier
        
        is_outgoing (:class:`bool`)
            True, if the call is outgoing
        
        is_video (:class:`bool`)
            True, if the call is a video call
        
        state (:class:`CallState`)
            Call state
        
    """

    ID: str = Field("call", alias="@type")
    id: int
    user_id: int
    is_outgoing: bool
    is_video: bool
    state: CallState

    @staticmethod
    def read(q: dict) -> Call:
        return Call.construct(**q)
