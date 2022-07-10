# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ReplaceVideoChatRtmpUrl(BaseObject):
    """
    Replaces the current RTMP URL for streaming to the chat; requires creator privileges
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    """

    ID: str = Field("replaceVideoChatRtmpUrl", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> ReplaceVideoChatRtmpUrl:
        return ReplaceVideoChatRtmpUrl.construct(**q)
