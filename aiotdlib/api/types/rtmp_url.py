# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class RtmpUrl(BaseObject):
    """
    Represents an RTMP url
    
    :param url: The URL
    :type url: :class:`str`
    
    :param stream_key: Stream key
    :type stream_key: :class:`str`
    
    """

    ID: str = Field("rtmpUrl", alias="@type")
    url: str
    stream_key: str

    @staticmethod
    def read(q: dict) -> RtmpUrl:
        return RtmpUrl.construct(**q)
