# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

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
    
    Params:
        name (:class:`str`)
            Anchor name
        
    """

    ID: str = Field("richTextAnchor", alias="@type")
    name: str

    @staticmethod
    def read(q: dict) -> RichTextAnchor:
        return RichTextAnchor.construct(**q)


class RichTextAnchorLink(RichText):
    """
    A link to an anchor on the same web page
    
    Params:
        text (:class:`RichText`)
            The link text
        
        anchor_name (:class:`str`)
            The anchor name. If the name is empty, the link should bring back to top
        
        url (:class:`str`)
            An HTTP URL, opening the anchor
        
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
    
    Params:
        text (:class:`RichText`)
            Text
        
    """

    ID: str = Field("richTextBold", alias="@type")
    text: RichText

    @staticmethod
    def read(q: dict) -> RichTextBold:
        return RichTextBold.construct(**q)


class RichTextEmailAddress(RichText):
    """
    A rich text email link
    
    Params:
        text (:class:`RichText`)
            Text
        
        email_address (:class:`str`)
            Email address
        
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
    
    Params:
        text (:class:`RichText`)
            Text
        
    """

    ID: str = Field("richTextFixed", alias="@type")
    text: RichText

    @staticmethod
    def read(q: dict) -> RichTextFixed:
        return RichTextFixed.construct(**q)


class RichTextIcon(RichText):
    """
    A small image inside the text
    
    Params:
        document (:class:`Document`)
            The image represented as a document. The image can be in GIF, JPEG or PNG format
        
        width (:class:`int`)
            Width of a bounding box in which the image should be shown; 0 if unknown
        
        height (:class:`int`)
            Height of a bounding box in which the image should be shown; 0 if unknown
        
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
    
    Params:
        text (:class:`RichText`)
            Text
        
    """

    ID: str = Field("richTextItalic", alias="@type")
    text: RichText

    @staticmethod
    def read(q: dict) -> RichTextItalic:
        return RichTextItalic.construct(**q)


class RichTextMarked(RichText):
    """
    A marked rich text
    
    Params:
        text (:class:`RichText`)
            Text
        
    """

    ID: str = Field("richTextMarked", alias="@type")
    text: RichText

    @staticmethod
    def read(q: dict) -> RichTextMarked:
        return RichTextMarked.construct(**q)


class RichTextPhoneNumber(RichText):
    """
    A rich text phone number
    
    Params:
        text (:class:`RichText`)
            Text
        
        phone_number (:class:`str`)
            Phone number
        
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
    
    Params:
        text (:class:`str`)
            Text
        
    """

    ID: str = Field("richTextPlain", alias="@type")
    text: str

    @staticmethod
    def read(q: dict) -> RichTextPlain:
        return RichTextPlain.construct(**q)


class RichTextReference(RichText):
    """
    A reference to a richTexts object on the same web page
    
    Params:
        text (:class:`RichText`)
            The text
        
        anchor_name (:class:`str`)
            The name of a richTextAnchor object, which is the first element of the target richTexts object
        
        url (:class:`str`)
            An HTTP URL, opening the reference
        
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
    
    Params:
        text (:class:`RichText`)
            Text
        
    """

    ID: str = Field("richTextStrikethrough", alias="@type")
    text: RichText

    @staticmethod
    def read(q: dict) -> RichTextStrikethrough:
        return RichTextStrikethrough.construct(**q)


class RichTextSubscript(RichText):
    """
    A subscript rich text
    
    Params:
        text (:class:`RichText`)
            Text
        
    """

    ID: str = Field("richTextSubscript", alias="@type")
    text: RichText

    @staticmethod
    def read(q: dict) -> RichTextSubscript:
        return RichTextSubscript.construct(**q)


class RichTextSuperscript(RichText):
    """
    A superscript rich text
    
    Params:
        text (:class:`RichText`)
            Text
        
    """

    ID: str = Field("richTextSuperscript", alias="@type")
    text: RichText

    @staticmethod
    def read(q: dict) -> RichTextSuperscript:
        return RichTextSuperscript.construct(**q)


class RichTextUnderline(RichText):
    """
    An underlined rich text
    
    Params:
        text (:class:`RichText`)
            Text
        
    """

    ID: str = Field("richTextUnderline", alias="@type")
    text: RichText

    @staticmethod
    def read(q: dict) -> RichTextUnderline:
        return RichTextUnderline.construct(**q)


class RichTextUrl(RichText):
    """
    A rich text URL link
    
    Params:
        text (:class:`RichText`)
            Text
        
        url (:class:`str`)
            URL
        
        is_cached (:class:`bool`)
            True, if the URL has cached instant view server-side
        
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
    
    Params:
        texts (:obj:`list[RichText]`)
            Texts
        
    """

    ID: str = Field("richTexts", alias="@type")
    texts: list[RichText]

    @staticmethod
    def read(q: dict) -> RichTexts:
        return RichTexts.construct(**q)
