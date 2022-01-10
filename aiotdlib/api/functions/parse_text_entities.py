# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import TextParseMode


class ParseTextEntities(BaseObject):
    """
    Parses Bold, Italic, Underline, Strikethrough, Spoiler, Code, Pre, PreCode, TextUrl and MentionName entities contained in the text. Can be called synchronously
    
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
