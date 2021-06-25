# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import MessageSender


class SetVoiceChatDefaultParticipant(BaseObject):
    """
    Changes default participant identifier, which can be used to join voice chats in a chat
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        default_participant_id (:class:`MessageSender`)
            Default group call participant identifier to join the voice chats
        
    """

    ID: str = Field("setVoiceChatDefaultParticipant", alias="@type")
    chat_id: int
    default_participant_id: MessageSender

    @staticmethod
    def read(q: dict) -> SetVoiceChatDefaultParticipant:
        return SetVoiceChatDefaultParticipant.construct(**q)
