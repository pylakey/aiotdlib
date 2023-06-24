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


class GetStickerEmojis(BaseObject):
    """
    Returns emoji corresponding to a sticker. The list is only for informational purposes, because a sticker is always sent with a fixed emoji from the corresponding Sticker object

    :param sticker: Sticker file identifier
    :type sticker: :class:`InputFile`
    """

    ID: typing.Literal["getStickerEmojis"] = "getStickerEmojis"
    sticker: InputFile
