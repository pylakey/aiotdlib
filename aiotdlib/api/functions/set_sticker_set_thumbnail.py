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
)


class SetStickerSetThumbnail(BaseObject):
    """
    Sets a sticker set thumbnail; for bots only

    :param user_id: Sticker set owner
    :type user_id: :class:`Int53`
    :param name: Sticker set name
    :type name: :class:`String`
    :param thumbnail: Thumbnail to set in PNG, TGS, or WEBM format; pass null to remove the sticker set thumbnail. Thumbnail format must match the format of stickers in the set, defaults to None
    :type thumbnail: :class:`InputFile`, optional
    """

    ID: typing.Literal["setStickerSetThumbnail"] = "setStickerSetThumbnail"
    user_id: Int53
    name: String
    thumbnail: typing.Optional[InputFile] = None
