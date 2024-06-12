# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class DeleteStickerSet(BaseObject):
    """
    Completely deletes a sticker set

    :param name: Sticker set name. The sticker set must be owned by the current user
    :type name: :class:`String`
    """

    ID: typing.Literal["deleteStickerSet"] = Field("deleteStickerSet", validation_alias="@type", alias="@type")
    name: String
