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
    StickerType,
)


class CreateNewStickerSet(BaseObject):
    """
    Creates a new sticker set. Returns the newly created sticker set

    :param user_id: Sticker set owner; ignored for regular users
    :type user_id: :class:`Int53`
    :param title: Sticker set title; 1-64 characters
    :type title: :class:`String`
    :param sticker_type: Type of the stickers in the set
    :type sticker_type: :class:`StickerType`
    :param stickers: List of stickers to be added to the set; 1-200 stickers for custom emoji sticker sets, and 1-120 stickers otherwise. For TGS stickers, uploadStickerFile must be used before the sticker is shown
    :type stickers: :class:`Vector[InputSticker]`
    :param needs_repainting: Pass true if stickers in the sticker set must be repainted; for custom emoji sticker sets only
    :type needs_repainting: :class:`Bool`
    :param source: Source of the sticker set; may be empty if unknown
    :type source: :class:`String`
    :param name: Sticker set name. Can contain only English letters, digits and underscores. Must end with *"_by_<bot username>"* (*<bot_username>* is case insensitive) for bots; 0-64 characters. If empty, then the name returned by getSuggestedStickerSetName will be used automatically, defaults to None
    :type name: :class:`String`, optional
    """

    ID: typing.Literal["createNewStickerSet"] = Field("createNewStickerSet", validation_alias="@type", alias="@type")
    user_id: Int53
    title: String = Field(..., min_length=1, max_length=64)
    sticker_type: StickerType
    stickers: Vector[InputSticker]
    needs_repainting: Bool = False
    source: String = ""
    name: typing.Optional[String] = Field("", max_length=64)
