# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetAttachedStickerSets(BaseObject):
    """
    Returns a list of sticker sets attached to a file, including regular, mask, and emoji sticker sets. Currently, only animations, photos, and videos can have attached sticker sets

    :param file_id: File identifier
    :type file_id: :class:`Int32`
    """

    ID: typing.Literal["getAttachedStickerSets"] = "getAttachedStickerSets"
    file_id: Int32
