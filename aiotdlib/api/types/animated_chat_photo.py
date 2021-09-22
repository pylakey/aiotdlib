# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .file import File
from ..base_object import BaseObject


class AnimatedChatPhoto(BaseObject):
    """
    Animated variant of a chat photo in MPEG4 format
    
    :param length: Animation width and height
    :type length: :class:`int`
    
    :param file: Information about the animation file
    :type file: :class:`File`
    
    :param main_frame_timestamp: Timestamp of the frame, used as a static chat photo
    :type main_frame_timestamp: :class:`float`
    
    """

    ID: str = Field("animatedChatPhoto", alias="@type")
    length: int
    file: File
    main_frame_timestamp: float

    @staticmethod
    def read(q: dict) -> AnimatedChatPhoto:
        return AnimatedChatPhoto.construct(**q)
