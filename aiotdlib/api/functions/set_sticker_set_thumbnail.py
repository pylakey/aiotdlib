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
    StickerFormat,
)


class SetStickerSetThumbnail(BaseObject):
    """
    Sets a sticker set thumbnail

    :param user_id: Sticker set owner; ignored for regular users
    :type user_id: :class:`Int53`
    :param name: Sticker set name. The sticker set must be owned by the current user
    :type name: :class:`String`
    :param thumbnail: Thumbnail to set; pass null to remove the sticker set thumbnail, defaults to None
    :type thumbnail: :class:`InputFile`, optional
    :param format: Format of the thumbnail; pass null if thumbnail is removed, defaults to None
    :type format: :class:`StickerFormat`, optional
    """

    ID: typing.Literal["setStickerSetThumbnail"] = Field(
        "setStickerSetThumbnail", validation_alias="@type", alias="@type"
    )
    user_id: Int53
    name: String
    thumbnail: typing.Optional[InputFile] = None
    format: typing.Optional[StickerFormat] = None
