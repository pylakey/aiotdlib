# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    InputSticker,
    StickerFormat,
    StickerType,
)


class CreateNewStickerSet(BaseObject):
    """
    Creates a new sticker set. Returns the newly created sticker set

    :param user_id: Sticker set owner; ignored for regular users
    :type user_id: :class:`Int53`
    :param title: Sticker set title; 1-64 characters
    :type title: :class:`String`
    :param name: Sticker set name. Can contain only English letters, digits and underscores. Must end with *"_by_<bot username>"* (*<bot_username>* is case insensitive) for bots; 1-64 characters
    :type name: :class:`String`
    :param sticker_format: Format of the stickers in the set
    :type sticker_format: :class:`StickerFormat`
    :param sticker_type: Type of the stickers in the set
    :type sticker_type: :class:`StickerType`
    :param stickers: List of stickers to be added to the set; must be non-empty. All stickers must have the same format. For TGS stickers, uploadStickerFile must be used before the sticker is shown
    :type stickers: :class:`Vector[InputSticker]`
    :param needs_repainting: Pass true if stickers in the sticker set must be repainted; for custom emoji sticker sets only
    :type needs_repainting: :class:`Bool`
    :param source: Source of the sticker set; may be empty if unknown
    :type source: :class:`String`
    """

    ID: typing.Literal["createNewStickerSet"] = "createNewStickerSet"
    user_id: Int53
    title: String = Field(..., min_length=1, max_length=64)
    name: String = Field(..., min_length=1, max_length=64)
    sticker_format: StickerFormat
    sticker_type: StickerType
    stickers: Vector[InputSticker]
    needs_repainting: Bool = False
    source: String = ""
