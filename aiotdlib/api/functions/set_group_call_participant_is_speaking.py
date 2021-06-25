# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SetGroupCallParticipantIsSpeaking(BaseObject):
    """
    Informs TDLib that speaking state of a participant of an active group has changed
    
    Params:
        group_call_id (:class:`int`)
            Group call identifier
        
        audio_source (:class:`int`)
            Group call participant's synchronization audio source identifier, or 0 for the current user
        
        is_speaking (:class:`bool`)
            True, if the user is speaking
        
    """

    ID: str = Field("setGroupCallParticipantIsSpeaking", alias="@type")
    group_call_id: int
    audio_source: int
    is_speaking: bool

    @staticmethod
    def read(q: dict) -> SetGroupCallParticipantIsSpeaking:
        return SetGroupCallParticipantIsSpeaking.construct(**q)
