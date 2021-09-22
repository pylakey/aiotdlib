# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import InputSticker
from ..base_object import BaseObject


class CreateNewStickerSet(BaseObject):
    """
    Creates a new sticker set. Returns the newly created sticker set
    
    :param user_id: Sticker set owner; ignored for regular users
    :type user_id: :class:`int`
    
    :param title: Sticker set title; 1-64 characters
    :type title: :class:`str`
    
    :param name: Sticker set name. Can contain only English letters, digits and underscores. Must end with *"_by_<bot username>"* (*<bot_username>* is case insensitive) for bots; 1-64 characters
    :type name: :class:`str`
    
    :param is_masks: True, if stickers are masks. Animated stickers can't be masks
    :type is_masks: :class:`bool`
    
    :param stickers: List of stickers to be added to the set; must be non-empty. All stickers must be of the same type. For animated stickers, uploadStickerFile must be used before the sticker is shown
    :type stickers: :class:`list[InputSticker]`
    
    :param source: Source of the sticker set; may be empty if unknown
    :type source: :class:`str`
    
    """

    ID: str = Field("createNewStickerSet", alias="@type")
    user_id: int
    title: str = Field(..., min_length=1, max_length=64)
    name: str = Field(..., min_length=1, max_length=64)
    is_masks: bool
    stickers: list[InputSticker]
    source: str

    @staticmethod
    def read(q: dict) -> CreateNewStickerSet:
        return CreateNewStickerSet.construct(**q)
