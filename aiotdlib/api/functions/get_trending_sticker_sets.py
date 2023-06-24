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


class GetTrendingStickerSets(BaseObject):
    """
    Returns a list of trending sticker sets. For optimal performance, the number of returned sticker sets is chosen by TDLib

    :param sticker_type: Type of the sticker sets to return
    :type sticker_type: :class:`StickerType`
    :param offset: The offset from which to return the sticker sets; must be non-negative
    :type offset: :class:`Int32`
    :param limit: The maximum number of sticker sets to be returned; up to 100. For optimal performance, the number of returned sticker sets is chosen by TDLib and can be smaller than the specified limit, even if the end of the list has not been reached
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["getTrendingStickerSets"] = "getTrendingStickerSets"
    sticker_type: StickerType
    offset: Int32
    limit: Int32
