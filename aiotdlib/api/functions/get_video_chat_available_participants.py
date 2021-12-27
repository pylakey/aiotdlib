# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetVideoChatAvailableParticipants(BaseObject):
    """
    Returns list of participant identifiers, on whose behalf a video chat in the chat can be joined
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    """

    ID: str = Field("getVideoChatAvailableParticipants", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> GetVideoChatAvailableParticipants:
        return GetVideoChatAvailableParticipants.construct(**q)
