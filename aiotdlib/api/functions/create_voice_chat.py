# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CreateVoiceChat(BaseObject):
    """
    Creates a voice chat (a group call bound to a chat). Available only for basic groups, supergroups and channels; requires can_manage_voice_chats rights
    
    Params:
        chat_id (:class:`int`)
            Chat identifier, in which the voice chat will be created
        
        title (:class:`str`)
            Group call title; if empty, chat title will be used
        
        start_date (:class:`int`)
            Point in time (Unix timestamp) when the group call is supposed to be started by an administrator; 0 to start the voice chat immediately. The date must be at least 10 seconds and at most 8 days in the future
        
    """

    ID: str = Field("createVoiceChat", alias="@type")
    chat_id: int
    title: str
    start_date: int

    @staticmethod
    def read(q: dict) -> CreateVoiceChat:
        return CreateVoiceChat.construct(**q)
