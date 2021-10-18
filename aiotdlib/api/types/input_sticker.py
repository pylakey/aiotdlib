# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

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
    
    :param sticker: File with the animated sticker. Only local or uploaded within a week files are supported. See https://core.telegram.org/animated_stickers#technical-requirements for technical requirements
    :type sticker: :class:`InputFile`
    
    :param emojis: Emojis corresponding to the sticker
    :type emojis: :class:`str`
    
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
    
    :param sticker: PNG image with the sticker; must be up to 512 KB in size and fit in a 512x512 square
    :type sticker: :class:`InputFile`
    
    :param emojis: Emojis corresponding to the sticker
    :type emojis: :class:`str`
    
    :param mask_position: For masks, position where the mask is placed; pass null if unspecified
    :type mask_position: :class:`MaskPosition`
    
    """

    ID: str = Field("inputStickerStatic", alias="@type")
    sticker: InputFile
    emojis: str
    mask_position: MaskPosition

    @staticmethod
    def read(q: dict) -> InputStickerStatic:
        return InputStickerStatic.construct(**q)
