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
    Deleted a sticker set; for bots only

    :param name: Sticker set name
    :type name: :class:`String`
    """

    ID: typing.Literal["deleteStickerSet"] = "deleteStickerSet"
    name: String
