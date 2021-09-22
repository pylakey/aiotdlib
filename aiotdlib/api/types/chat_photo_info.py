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


class ChatPhotoInfo(BaseObject):
    """
    Contains basic information about the photo of a chat
    
    :param small: A small (160x160) chat photo variant in JPEG format. The file can be downloaded only before the photo is changed
    :type small: :class:`File`
    
    :param big: A big (640x640) chat photo variant in JPEG format. The file can be downloaded only before the photo is changed
    :type big: :class:`File`
    
    :param minithumbnail: Chat photo minithumbnail; may be null, defaults to None
    :type minithumbnail: :class:`Minithumbnail`, optional
    
    :param has_animation: True, if the photo has animated variant
    :type has_animation: :class:`bool`
    
    """

    ID: str = Field("chatPhotoInfo", alias="@type")
    small: File
    big: File
    minithumbnail: typing.Optional[Minithumbnail] = None
    has_animation: bool

    @staticmethod
    def read(q: dict) -> ChatPhotoInfo:
        return ChatPhotoInfo.construct(**q)
