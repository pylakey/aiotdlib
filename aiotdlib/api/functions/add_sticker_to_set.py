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
)


class AddStickerToSet(BaseObject):
    """
    Adds a new sticker to a set

    :param user_id: Sticker set owner; ignored for regular users
    :type user_id: :class:`Int53`
    :param name: Sticker set name. The sticker set must be owned by the current user, and contain less than 200 stickers for custom emoji sticker sets and less than 120 otherwise
    :type name: :class:`String`
    :param sticker: Sticker to add to the set
    :type sticker: :class:`InputSticker`
    """

    ID: typing.Literal["addStickerToSet"] = Field("addStickerToSet", validation_alias="@type", alias="@type")
    user_id: Int53
    name: String
    sticker: InputSticker
