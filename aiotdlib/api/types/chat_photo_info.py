# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .file import File
from ..base_object import BaseObject


class ChatPhotoInfo(BaseObject):
    """
    Contains basic information about the photo of a chat
    
    Params:
        small (:class:`File`)
            A small (160x160) chat photo variant in JPEG format. The file can be downloaded only before the photo is changed
        
        big (:class:`File`)
            A big (640x640) chat photo variant in JPEG format. The file can be downloaded only before the photo is changed
        
        has_animation (:class:`bool`)
            True, if the photo has animated variant
        
    """

    ID: str = Field("chatPhotoInfo", alias="@type")
    small: File
    big: File
    has_animation: bool

    @staticmethod
    def read(q: dict) -> ChatPhotoInfo:
        return ChatPhotoInfo.construct(**q)
