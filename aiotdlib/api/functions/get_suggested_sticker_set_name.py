# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetSuggestedStickerSetName(BaseObject):
    """
    Returns a suggested name for a new sticker set with a given title

    :param title: Sticker set title; 1-64 characters
    :type title: :class:`String`
    """

    ID: typing.Literal["getSuggestedStickerSetName"] = "getSuggestedStickerSetName"
    title: String = Field(..., min_length=1, max_length=64)
