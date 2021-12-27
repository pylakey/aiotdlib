# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import MessageSender


class SetVideoChatDefaultParticipant(BaseObject):
    """
    Changes default participant identifier, on whose behalf a video chat in the chat will be joined
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param default_participant_id: Default group call participant identifier to join the video chats
    :type default_participant_id: :class:`MessageSender`
    
    """

    ID: str = Field("setVideoChatDefaultParticipant", alias="@type")
    chat_id: int
    default_participant_id: MessageSender

    @staticmethod
    def read(q: dict) -> SetVideoChatDefaultParticipant:
        return SetVideoChatDefaultParticipant.construct(**q)
