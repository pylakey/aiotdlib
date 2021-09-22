# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import MessageSender
from ..base_object import BaseObject


class SetVoiceChatDefaultParticipant(BaseObject):
    """
    Changes default participant identifier, which can be used to join voice chats in a chat
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param default_participant_id: Default group call participant identifier to join the voice chats
    :type default_participant_id: :class:`MessageSender`
    
    """

    ID: str = Field("setVoiceChatDefaultParticipant", alias="@type")
    chat_id: int
    default_participant_id: MessageSender

    @staticmethod
    def read(q: dict) -> SetVoiceChatDefaultParticipant:
        return SetVoiceChatDefaultParticipant.construct(**q)
