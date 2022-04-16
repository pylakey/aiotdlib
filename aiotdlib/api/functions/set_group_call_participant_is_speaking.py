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
    
    :param group_call_id: Group call identifier
    :type group_call_id: :class:`int`
    
    :param audio_source: Group call participant's synchronization audio source identifier, or 0 for the current user
    :type audio_source: :class:`int`
    
    :param is_speaking: Pass true if the user is speaking
    :type is_speaking: :class:`bool`
    
    """

    ID: str = Field("setGroupCallParticipantIsSpeaking", alias="@type")
    group_call_id: int
    audio_source: int
    is_speaking: bool

    @staticmethod
    def read(q: dict) -> SetGroupCallParticipantIsSpeaking:
        return SetGroupCallParticipantIsSpeaking.construct(**q)
