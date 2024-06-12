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
    InputFile,
    InputSticker,
)


class ReplaceStickerInSet(BaseObject):
    """
    Replaces existing sticker in a set. The function is equivalent to removeStickerFromSet, then addStickerToSet, then setStickerPositionInSet

    :param user_id: Sticker set owner; ignored for regular users
    :type user_id: :class:`Int53`
    :param name: Sticker set name. The sticker set must be owned by the current user
    :type name: :class:`String`
    :param old_sticker: Sticker to remove from the set
    :type old_sticker: :class:`InputFile`
    :param new_sticker: Sticker to add to the set
    :type new_sticker: :class:`InputSticker`
    """

    ID: typing.Literal["replaceStickerInSet"] = Field("replaceStickerInSet", validation_alias="@type", alias="@type")
    user_id: Int53
    name: String
    old_sticker: InputFile
    new_sticker: InputSticker
