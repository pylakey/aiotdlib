# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SearchStickerSet(BaseObject):
    """
    Searches for a sticker set by its name

    :param name: Name of the sticker set
    :type name: :class:`String`
    """

    ID: typing.Literal["searchStickerSet"] = "searchStickerSet"
    name: String
