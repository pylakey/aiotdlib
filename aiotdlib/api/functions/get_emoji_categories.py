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
    Returns available emoji categories

    :param type_: Type of emoji categories to return; pass null to get default emoji categories, defaults to None
    :type type_: :class:`EmojiCategoryType`, optional
    """

    ID: typing.Literal["getEmojiCategories"] = Field("getEmojiCategories", validation_alias="@type", alias="@type")
    type_: typing.Optional[EmojiCategoryType] = Field(None, alias="type")
