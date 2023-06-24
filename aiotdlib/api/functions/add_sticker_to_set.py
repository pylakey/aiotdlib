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
    Adds a new sticker to a set; for bots only

    :param user_id: Sticker set owner
    :type user_id: :class:`Int53`
    :param name: Sticker set name
    :type name: :class:`String`
    :param sticker: Sticker to add to the set
    :type sticker: :class:`InputSticker`
    """

    ID: typing.Literal["addStickerToSet"] = "addStickerToSet"
    user_id: Int53
    name: String
    sticker: InputSticker
