# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .file import File
from .minithumbnail import Minithumbnail
from ..base_object import BaseObject


class ProfilePhoto(BaseObject):
    """
    Describes a user profile photo
    
    Params:
        id (:class:`int`)
            Photo identifier; 0 for an empty photo. Can be used to find a photo in a list of user profile photos
        
        small (:class:`File`)
            A small (160x160) user profile photo. The file can be downloaded only before the photo is changed
        
        big (:class:`File`)
            A big (640x640) user profile photo. The file can be downloaded only before the photo is changed
        
        minithumbnail (:class:`Minithumbnail`)
            User profile photo minithumbnail; may be null
        
        has_animation (:class:`bool`)
            True, if the photo has animated variant
        
    """

    ID: str = Field("profilePhoto", alias="@type")
    id: int
    small: File
    big: File
    minithumbnail: typing.Optional[Minithumbnail] = None
    has_animation: bool

    @staticmethod
    def read(q: dict) -> ProfilePhoto:
        return ProfilePhoto.construct(**q)
