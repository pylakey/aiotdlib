# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class DiscardCall(BaseObject):
    """
    Discards a call
    
    Params:
        call_id (:class:`int`)
            Call identifier
        
        is_disconnected (:class:`bool`)
            True, if the user was disconnected
        
        duration (:class:`int`)
            The call duration, in seconds
        
        is_video (:class:`bool`)
            True, if the call was a video call
        
        connection_id (:class:`int`)
            Identifier of the connection used during the call
        
    """

    ID: str = Field("discardCall", alias="@type")
    call_id: int
    is_disconnected: bool
    duration: int
    is_video: bool
    connection_id: int

    @staticmethod
    def read(q: dict) -> DiscardCall:
        return DiscardCall.construct(**q)
