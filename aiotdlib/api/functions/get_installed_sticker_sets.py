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
    StickerType,
)


class GetInstalledStickerSets(BaseObject):
    """
    Returns a list of installed sticker sets

    :param sticker_type: Type of the sticker sets to return
    :type sticker_type: :class:`StickerType`
    """

    ID: typing.Literal["getInstalledStickerSets"] = "getInstalledStickerSets"
    sticker_type: StickerType
