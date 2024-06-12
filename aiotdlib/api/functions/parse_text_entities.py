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
    TextParseMode,
)


class ParseTextEntities(BaseObject):
    """
    Parses Bold, Italic, Underline, Strikethrough, Spoiler, CustomEmoji, BlockQuote, ExpandableBlockQuote, Code, Pre, PreCode, TextUrl and MentionName entities from a marked-up text. Can be called synchronously

    :param text: The text to parse
    :type text: :class:`String`
    :param parse_mode: Text parse mode
    :type parse_mode: :class:`TextParseMode`
    """

    ID: typing.Literal["parseTextEntities"] = Field("parseTextEntities", validation_alias="@type", alias="@type")
    text: String
    parse_mode: TextParseMode
