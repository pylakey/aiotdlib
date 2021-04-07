# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class TextParseMode(BaseObject):
    """
    Describes the way the text should be parsed for TextEntities
    
    """

    ID: str = Field("textParseMode", alias="@type")


class TextParseModeHTML(TextParseMode):
    """
    The text uses HTML-style formatting. The same as Telegram Bot API "HTML" parse mode
    
    """

    ID: str = Field("textParseModeHTML", alias="@type")

    @staticmethod
    def read(q: dict) -> TextParseModeHTML:
        return TextParseModeHTML.construct(**q)


class TextParseModeMarkdown(TextParseMode):
    """
    The text uses Markdown-style formatting
    
    Params:
        version (:class:`int`)
            Version of the parser: 0 or 1 - Telegram Bot API "Markdown" parse mode, 2 - Telegram Bot API "MarkdownV2" parse mode
        
    """

    ID: str = Field("textParseModeMarkdown", alias="@type")
    version: int

    @staticmethod
    def read(q: dict) -> TextParseModeMarkdown:
        return TextParseModeMarkdown.construct(**q)
