# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .file import File
from .sticker import Sticker
from ..base_object import BaseObject


class AnimatedEmoji(BaseObject):
    """
    Describes an animated representation of an emoji
    
    :param sticker: Animated sticker for the emoji
    :type sticker: :class:`Sticker`
    
    :param fitzpatrick_type: Emoji modifier fitzpatrick type; 0-6; 0 if none
    :type fitzpatrick_type: :class:`int`
    
    :param sound: File containing the sound to be played when the animated emoji is clicked; may be null. The sound is encoded with the Opus codec, and stored inside an OGG container, defaults to None
    :type sound: :class:`File`, optional
    
    """

    ID: str = Field("animatedEmoji", alias="@type")
    sticker: Sticker
    fitzpatrick_type: int
    sound: typing.Optional[File] = None

    @staticmethod
    def read(q: dict) -> AnimatedEmoji:
        return AnimatedEmoji.construct(**q)
