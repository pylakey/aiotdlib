# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import TextParseMode
from ..base_object import BaseObject


class ParseTextEntities(BaseObject):
    """
    Parses Bold, Italic, Underline, Strikethrough, Code, Pre, PreCode, TextUrl and MentionName entities contained in the text. Can be called synchronously
    
    :param text: The text to parse
    :type text: :class:`str`
    
    :param parse_mode: Text parse mode
    :type parse_mode: :class:`TextParseMode`
    
    """

    ID: str = Field("parseTextEntities", alias="@type")
    text: str
    parse_mode: TextParseMode

    @staticmethod
    def read(q: dict) -> ParseTextEntities:
        return ParseTextEntities.construct(**q)
