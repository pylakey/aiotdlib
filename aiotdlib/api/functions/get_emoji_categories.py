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
    EmojiCategoryType,
)


class GetEmojiCategories(BaseObject):
    """
    Returns available emojis categories

    :param type_: Type of emoji categories to return; pass null to get default emoji categories, defaults to None
    :type type_: :class:`EmojiCategoryType`, optional
    """

    ID: typing.Literal["getEmojiCategories"] = "getEmojiCategories"
    type_: typing.Optional[EmojiCategoryType] = Field(None, alias="type")
