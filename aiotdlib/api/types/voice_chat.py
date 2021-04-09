# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .message_sender import MessageSender
from ..base_object import BaseObject


class VoiceChat(BaseObject):
    """
    Describes a voice chat
    
    Params:
        group_call_id (:class:`int`)
            Group call identifier of an active voice chat; 0 if none. Full informationa about the voice chat can be received through the method getGroupCall
        
        has_participants (:class:`bool`)
            True, if the voice chat has participants
        
        default_participant_alias (:class:`MessageSender`)
            Default group call participant identifier to join the voice chat; may be null
        
    """

    ID: str = Field("voiceChat", alias="@type")
    group_call_id: int
    has_participants: bool
    default_participant_alias: typing.Optional[MessageSender] = None

    @staticmethod
    def read(q: dict) -> VoiceChat:
        return VoiceChat.construct(**q)
