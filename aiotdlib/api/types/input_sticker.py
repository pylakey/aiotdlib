# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .input_file import InputFile
from .sticker_type import StickerType
from ..base_object import BaseObject


class InputSticker(BaseObject):
    """
    A sticker to be added to a sticker set
    
    :param sticker: File with the sticker; must fit in a 512x512 square. For WEBP stickers and masks the file must be in PNG format, which will be converted to WEBP server-side. Otherwise, the file must be local or uploaded within a week. See https://core.telegram.org/animated_stickers#technical-requirements for technical requirements
    :type sticker: :class:`InputFile`
    
    :param emojis: Emojis corresponding to the sticker
    :type emojis: :class:`str`
    
    :param type_: Sticker type
    :type type_: :class:`StickerType`
    
    """

    ID: str = Field("inputSticker", alias="@type")
    sticker: InputFile
    emojis: str
    type_: StickerType = Field(..., alias='type')

    @staticmethod
    def read(q: dict) -> InputSticker:
        return InputSticker.construct(**q)
