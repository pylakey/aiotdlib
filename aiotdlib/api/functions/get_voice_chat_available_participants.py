# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetVoiceChatAvailableParticipants(BaseObject):
    """
    Returns list of participant identifiers, which can be used to join voice chats in a chat
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    """

    ID: str = Field("getVoiceChatAvailableParticipants", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> GetVoiceChatAvailableParticipants:
        return GetVoiceChatAvailableParticipants.construct(**q)
