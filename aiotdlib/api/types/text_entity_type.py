# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class TextEntityType(BaseObject):
    """
    Represents a part of the text which must be formatted differently
    
    """

    ID: str = Field("textEntityType", alias="@type")


class TextEntityTypeBankCardNumber(TextEntityType):
    """
    A bank card number. The getBankCardInfo method can be used to get information about the bank card
    
    """

    ID: str = Field("textEntityTypeBankCardNumber", alias="@type")

    @staticmethod
    def read(q: dict) -> TextEntityTypeBankCardNumber:
        return TextEntityTypeBankCardNumber.construct(**q)


class TextEntityTypeBold(TextEntityType):
    """
    A bold text
    
    """

    ID: str = Field("textEntityTypeBold", alias="@type")

    @staticmethod
    def read(q: dict) -> TextEntityTypeBold:
        return TextEntityTypeBold.construct(**q)


class TextEntityTypeBotCommand(TextEntityType):
    """
    A bot command, beginning with "/". This shouldn't be highlighted if there are no bots in the chat
    
    """

    ID: str = Field("textEntityTypeBotCommand", alias="@type")

    @staticmethod
    def read(q: dict) -> TextEntityTypeBotCommand:
        return TextEntityTypeBotCommand.construct(**q)


class TextEntityTypeCashtag(TextEntityType):
    """
    A cashtag text, beginning with "$" and consisting of capital english letters (i.e. "$USD")
    
    """

    ID: str = Field("textEntityTypeCashtag", alias="@type")

    @staticmethod
    def read(q: dict) -> TextEntityTypeCashtag:
        return TextEntityTypeCashtag.construct(**q)


class TextEntityTypeCode(TextEntityType):
    """
    Text that must be formatted as if inside a code HTML tag
    
    """

    ID: str = Field("textEntityTypeCode", alias="@type")

    @staticmethod
    def read(q: dict) -> TextEntityTypeCode:
        return TextEntityTypeCode.construct(**q)


class TextEntityTypeEmailAddress(TextEntityType):
    """
    An email address
    
    """

    ID: str = Field("textEntityTypeEmailAddress", alias="@type")

    @staticmethod
    def read(q: dict) -> TextEntityTypeEmailAddress:
        return TextEntityTypeEmailAddress.construct(**q)


class TextEntityTypeHashtag(TextEntityType):
    """
    A hashtag text, beginning with "#"
    
    """

    ID: str = Field("textEntityTypeHashtag", alias="@type")

    @staticmethod
    def read(q: dict) -> TextEntityTypeHashtag:
        return TextEntityTypeHashtag.construct(**q)


class TextEntityTypeItalic(TextEntityType):
    """
    An italic text
    
    """

    ID: str = Field("textEntityTypeItalic", alias="@type")

    @staticmethod
    def read(q: dict) -> TextEntityTypeItalic:
        return TextEntityTypeItalic.construct(**q)


class TextEntityTypeMention(TextEntityType):
    """
    A mention of a user by their username
    
    """

    ID: str = Field("textEntityTypeMention", alias="@type")

    @staticmethod
    def read(q: dict) -> TextEntityTypeMention:
        return TextEntityTypeMention.construct(**q)


class TextEntityTypeMentionName(TextEntityType):
    """
    A text shows instead of a raw mention of the user (e.g., when the user has no username)
    
    Params:
        user_id (:class:`int`)
            Identifier of the mentioned user
        
    """

    ID: str = Field("textEntityTypeMentionName", alias="@type")
    user_id: int

    @staticmethod
    def read(q: dict) -> TextEntityTypeMentionName:
        return TextEntityTypeMentionName.construct(**q)


class TextEntityTypePhoneNumber(TextEntityType):
    """
    A phone number
    
    """

    ID: str = Field("textEntityTypePhoneNumber", alias="@type")

    @staticmethod
    def read(q: dict) -> TextEntityTypePhoneNumber:
        return TextEntityTypePhoneNumber.construct(**q)


class TextEntityTypePre(TextEntityType):
    """
    Text that must be formatted as if inside a pre HTML tag
    
    """

    ID: str = Field("textEntityTypePre", alias="@type")

    @staticmethod
    def read(q: dict) -> TextEntityTypePre:
        return TextEntityTypePre.construct(**q)


class TextEntityTypePreCode(TextEntityType):
    """
    Text that must be formatted as if inside pre, and code HTML tags
    
    Params:
        language (:class:`str`)
            Programming language of the code; as defined by the sender
        
    """

    ID: str = Field("textEntityTypePreCode", alias="@type")
    language: str

    @staticmethod
    def read(q: dict) -> TextEntityTypePreCode:
        return TextEntityTypePreCode.construct(**q)


class TextEntityTypeStrikethrough(TextEntityType):
    """
    A strikethrough text
    
    """

    ID: str = Field("textEntityTypeStrikethrough", alias="@type")

    @staticmethod
    def read(q: dict) -> TextEntityTypeStrikethrough:
        return TextEntityTypeStrikethrough.construct(**q)


class TextEntityTypeTextUrl(TextEntityType):
    """
    A text description shown instead of a raw URL
    
    Params:
        url (:class:`str`)
            HTTP or tg:// URL to be opened when the link is clicked
        
    """

    ID: str = Field("textEntityTypeTextUrl", alias="@type")
    url: str

    @staticmethod
    def read(q: dict) -> TextEntityTypeTextUrl:
        return TextEntityTypeTextUrl.construct(**q)


class TextEntityTypeUnderline(TextEntityType):
    """
    An underlined text
    
    """

    ID: str = Field("textEntityTypeUnderline", alias="@type")

    @staticmethod
    def read(q: dict) -> TextEntityTypeUnderline:
        return TextEntityTypeUnderline.construct(**q)


class TextEntityTypeUrl(TextEntityType):
    """
    An HTTP URL
    
    """

    ID: str = Field("textEntityTypeUrl", alias="@type")

    @staticmethod
    def read(q: dict) -> TextEntityTypeUrl:
        return TextEntityTypeUrl.construct(**q)
