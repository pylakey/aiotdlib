# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class StartGroupCallScreenSharing(BaseObject):
    """
    Starts screen sharing in a joined group call. Returns join response payload for tgcalls
    
    Params:
        group_call_id (:class:`int`)
            Group call identifier
        
        audio_source_id (:class:`int`)
            Screen sharing audio channel synchronization source identifier; received from tgcalls
        
        payload (:class:`str`)
            Group call join payload; received from tgcalls
        
    """

    ID: str = Field("startGroupCallScreenSharing", alias="@type")
    group_call_id: int
    audio_source_id: int
    payload: str

    @staticmethod
    def read(q: dict) -> StartGroupCallScreenSharing:
        return StartGroupCallScreenSharing.construct(**q)
