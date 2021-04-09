# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .input_file import InputFile
from .mask_position import MaskPosition
from ..base_object import BaseObject


class InputSticker(BaseObject):
    """
    Describes a sticker that needs to be added to a sticker set
    
    """

    ID: str = Field("inputSticker", alias="@type")


class InputStickerAnimated(InputSticker):
    """
    An animated sticker in TGS format
    
    Params:
        sticker (:class:`InputFile`)
            File with the animated sticker. Only local or uploaded within a week files are supported. See https://core.telegram.org/animated_stickers#technical-requirements for technical requirements
        
        emojis (:class:`str`)
            Emojis corresponding to the sticker
        
    """

    ID: str = Field("inputStickerAnimated", alias="@type")
    sticker: InputFile
    emojis: str

    @staticmethod
    def read(q: dict) -> InputStickerAnimated:
        return InputStickerAnimated.construct(**q)


class InputStickerStatic(InputSticker):
    """
    A static sticker in PNG format, which will be converted to WEBP server-side
    
    Params:
        sticker (:class:`InputFile`)
            PNG image with the sticker; must be up to 512 KB in size and fit in a 512x512 square
        
        emojis (:class:`str`)
            Emojis corresponding to the sticker
        
        mask_position (:class:`MaskPosition`)
            For masks, position where the mask should be placed; may be null
        
    """

    ID: str = Field("inputStickerStatic", alias="@type")
    sticker: InputFile
    emojis: str
    mask_position: typing.Optional[MaskPosition] = None

    @staticmethod
    def read(q: dict) -> InputStickerStatic:
        return InputStickerStatic.construct(**q)
