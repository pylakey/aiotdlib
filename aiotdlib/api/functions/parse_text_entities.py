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
    Parses Bold, Italic, Underline, Strikethrough, Code, Pre, PreCode, TextUrl and MentionName entities contained in the text. Can be called synchronously
    
    Params:
        text (:class:`str`)
            The text to parse
        
        parse_mode (:class:`TextParseMode`)
            Text parse mode
        
    """

    ID: str = Field("parseTextEntities", alias="@type")
    text: str
    parse_mode: TextParseMode

    @staticmethod
    def read(q: dict) -> ParseTextEntities:
        return ParseTextEntities.construct(**q)
