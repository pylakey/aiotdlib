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
            Chat identifier
        
    """

    ID: str = Field("createVoiceChat", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> CreateVoiceChat:
        return CreateVoiceChat.construct(**q)
