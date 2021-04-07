# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .file import File
from ..base_object import BaseObject


class AnimatedChatPhoto(BaseObject):
    """
    Animated variant of a chat photo in MPEG4 format
    
    Params:
        length (:class:`int`)
            Animation width and height
        
        file (:class:`File`)
            Information about the animation file
        
        main_frame_timestamp (:class:`float`)
            Timestamp of the frame, used as a static chat photo
        
    """

    ID: str = Field("animatedChatPhoto", alias="@type")
    length: int
    file: File
    main_frame_timestamp: float

    @staticmethod
    def read(q: dict) -> AnimatedChatPhoto:
        return AnimatedChatPhoto.construct(**q)
