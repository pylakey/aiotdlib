# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetStickerSet(BaseObject):
    """
    Returns information about a sticker set by its identifier

    :param set_id: Identifier of the sticker set
    :type set_id: :class:`Int64`
    """

    ID: typing.Literal["getStickerSet"] = "getStickerSet"
    set_id: Int64
