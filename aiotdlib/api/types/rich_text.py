# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .document import Document
from ..base_object import BaseObject


class RichText(BaseObject):
    """
    Describes a text object inside an instant-view web page
    
    """

    ID: str = Field("richText", alias="@type")


class RichTextAnchor(RichText):
    """
    An anchor
    
    :param name: Anchor name
    :type name: :class:`str`
    
    """

    ID: str = Field("richTextAnchor", alias="@type")
    name: str

    @staticmethod
    def read(q: dict) -> RichTextAnchor:
        return RichTextAnchor.construct(**q)


class RichTextAnchorLink(RichText):
    """
    A link to an anchor on the same web page
    
    :param text: The link text
    :type text: :class:`RichText`
    
    :param anchor_name: The anchor name. If the name is empty, the link should bring back to top
    :type anchor_name: :class:`str`
    
    :param url: An HTTP URL, opening the anchor
    :type url: :class:`str`
    
    """

    ID: str = Field("richTextAnchorLink", alias="@type")
    text: RichText
    anchor_name: str
    url: str

    @staticmethod
    def read(q: dict) -> RichTextAnchorLink:
        return RichTextAnchorLink.construct(**q)


class RichTextBold(RichText):
    """
    A bold rich text
    
    :param text: Text
    :type text: :class:`RichText`
    
    """

    ID: str = Field("richTextBold", alias="@type")
    text: RichText

    @staticmethod
    def read(q: dict) -> RichTextBold:
        return RichTextBold.construct(**q)


class RichTextEmailAddress(RichText):
    """
    A rich text email link
    
    :param text: Text
    :type text: :class:`RichText`
    
    :param email_address: Email address
    :type email_address: :class:`str`
    
    """

    ID: str = Field("richTextEmailAddress", alias="@type")
    text: RichText
    email_address: str

    @staticmethod
    def read(q: dict) -> RichTextEmailAddress:
        return RichTextEmailAddress.construct(**q)


class RichTextFixed(RichText):
    """
    A fixed-width rich text
    
    :param text: Text
    :type text: :class:`RichText`
    
    """

    ID: str = Field("richTextFixed", alias="@type")
    text: RichText

    @staticmethod
    def read(q: dict) -> RichTextFixed:
        return RichTextFixed.construct(**q)


class RichTextIcon(RichText):
    """
    A small image inside the text
    
    :param document: The image represented as a document. The image can be in GIF, JPEG or PNG format
    :type document: :class:`Document`
    
    :param width: Width of a bounding box in which the image should be shown; 0 if unknown
    :type width: :class:`int`
    
    :param height: Height of a bounding box in which the image should be shown; 0 if unknown
    :type height: :class:`int`
    
    """

    ID: str = Field("richTextIcon", alias="@type")
    document: Document
    width: int
    height: int

    @staticmethod
    def read(q: dict) -> RichTextIcon:
        return RichTextIcon.construct(**q)


class RichTextItalic(RichText):
    """
    An italicized rich text
    
    :param text: Text
    :type text: :class:`RichText`
    
    """

    ID: str = Field("richTextItalic", alias="@type")
    text: RichText

    @staticmethod
    def read(q: dict) -> RichTextItalic:
        return RichTextItalic.construct(**q)


class RichTextMarked(RichText):
    """
    A marked rich text
    
    :param text: Text
    :type text: :class:`RichText`
    
    """

    ID: str = Field("richTextMarked", alias="@type")
    text: RichText

    @staticmethod
    def read(q: dict) -> RichTextMarked:
        return RichTextMarked.construct(**q)


class RichTextPhoneNumber(RichText):
    """
    A rich text phone number
    
    :param text: Text
    :type text: :class:`RichText`
    
    :param phone_number: Phone number
    :type phone_number: :class:`str`
    
    """

    ID: str = Field("richTextPhoneNumber", alias="@type")
    text: RichText
    phone_number: str

    @staticmethod
    def read(q: dict) -> RichTextPhoneNumber:
        return RichTextPhoneNumber.construct(**q)


class RichTextPlain(RichText):
    """
    A plain text
    
    :param text: Text
    :type text: :class:`str`
    
    """

    ID: str = Field("richTextPlain", alias="@type")
    text: str

    @staticmethod
    def read(q: dict) -> RichTextPlain:
        return RichTextPlain.construct(**q)


class RichTextReference(RichText):
    """
    A reference to a richTexts object on the same web page
    
    :param text: The text
    :type text: :class:`RichText`
    
    :param anchor_name: The name of a richTextAnchor object, which is the first element of the target richTexts object
    :type anchor_name: :class:`str`
    
    :param url: An HTTP URL, opening the reference
    :type url: :class:`str`
    
    """

    ID: str = Field("richTextReference", alias="@type")
    text: RichText
    anchor_name: str
    url: str

    @staticmethod
    def read(q: dict) -> RichTextReference:
        return RichTextReference.construct(**q)


class RichTextStrikethrough(RichText):
    """
    A strikethrough rich text
    
    :param text: Text
    :type text: :class:`RichText`
    
    """

    ID: str = Field("richTextStrikethrough", alias="@type")
    text: RichText

    @staticmethod
    def read(q: dict) -> RichTextStrikethrough:
        return RichTextStrikethrough.construct(**q)


class RichTextSubscript(RichText):
    """
    A subscript rich text
    
    :param text: Text
    :type text: :class:`RichText`
    
    """

    ID: str = Field("richTextSubscript", alias="@type")
    text: RichText

    @staticmethod
    def read(q: dict) -> RichTextSubscript:
        return RichTextSubscript.construct(**q)


class RichTextSuperscript(RichText):
    """
    A superscript rich text
    
    :param text: Text
    :type text: :class:`RichText`
    
    """

    ID: str = Field("richTextSuperscript", alias="@type")
    text: RichText

    @staticmethod
    def read(q: dict) -> RichTextSuperscript:
        return RichTextSuperscript.construct(**q)


class RichTextUnderline(RichText):
    """
    An underlined rich text
    
    :param text: Text
    :type text: :class:`RichText`
    
    """

    ID: str = Field("richTextUnderline", alias="@type")
    text: RichText

    @staticmethod
    def read(q: dict) -> RichTextUnderline:
        return RichTextUnderline.construct(**q)


class RichTextUrl(RichText):
    """
    A rich text URL link
    
    :param text: Text
    :type text: :class:`RichText`
    
    :param url: URL
    :type url: :class:`str`
    
    :param is_cached: True, if the URL has cached instant view server-side
    :type is_cached: :class:`bool`
    
    """

    ID: str = Field("richTextUrl", alias="@type")
    text: RichText
    url: str
    is_cached: bool

    @staticmethod
    def read(q: dict) -> RichTextUrl:
        return RichTextUrl.construct(**q)


class RichTexts(RichText):
    """
    A concatenation of rich texts
    
    :param texts: Texts
    :type texts: :class:`list[RichText]`
    
    """

    ID: str = Field("richTexts", alias="@type")
    texts: list[RichText]

    @staticmethod
    def read(q: dict) -> RichTexts:
        return RichTexts.construct(**q)
