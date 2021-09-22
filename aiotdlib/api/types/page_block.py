# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .animation import Animation
from .audio import Audio
from .chat_photo_info import ChatPhotoInfo
from .location import Location
from .page_block_caption import PageBlockCaption
from .page_block_related_article import PageBlockRelatedArticle
from .page_block_table_cell import PageBlockTableCell
from .photo import Photo
from .rich_text import RichText
from .video import Video
from .voice_note import VoiceNote
from ..base_object import BaseObject


class PageBlock(BaseObject):
    """
    Describes a block of an instant view web page
    
    """

    ID: str = Field("pageBlock", alias="@type")


class PageBlockAnchor(PageBlock):
    """
    An invisible anchor on a page, which can be used in a URL to open the page from the specified anchor
    
    :param name: Name of the anchor
    :type name: :class:`str`
    
    """

    ID: str = Field("pageBlockAnchor", alias="@type")
    name: str

    @staticmethod
    def read(q: dict) -> PageBlockAnchor:
        return PageBlockAnchor.construct(**q)


class PageBlockAnimation(PageBlock):
    """
    An animation
    
    :param animation: Animation file; may be null, defaults to None
    :type animation: :class:`Animation`, optional
    
    :param caption: Animation caption
    :type caption: :class:`PageBlockCaption`
    
    :param need_autoplay: True, if the animation should be played automatically
    :type need_autoplay: :class:`bool`
    
    """

    ID: str = Field("pageBlockAnimation", alias="@type")
    animation: typing.Optional[Animation] = None
    caption: PageBlockCaption
    need_autoplay: bool

    @staticmethod
    def read(q: dict) -> PageBlockAnimation:
        return PageBlockAnimation.construct(**q)


class PageBlockAudio(PageBlock):
    """
    An audio file
    
    :param audio: Audio file; may be null, defaults to None
    :type audio: :class:`Audio`, optional
    
    :param caption: Audio file caption
    :type caption: :class:`PageBlockCaption`
    
    """

    ID: str = Field("pageBlockAudio", alias="@type")
    audio: typing.Optional[Audio] = None
    caption: PageBlockCaption

    @staticmethod
    def read(q: dict) -> PageBlockAudio:
        return PageBlockAudio.construct(**q)


class PageBlockAuthorDate(PageBlock):
    """
    The author and publishing date of a page
    
    :param author: Author
    :type author: :class:`RichText`
    
    :param publish_date: Point in time (Unix timestamp) when the article was published; 0 if unknown
    :type publish_date: :class:`int`
    
    """

    ID: str = Field("pageBlockAuthorDate", alias="@type")
    author: RichText
    publish_date: int

    @staticmethod
    def read(q: dict) -> PageBlockAuthorDate:
        return PageBlockAuthorDate.construct(**q)


class PageBlockBlockQuote(PageBlock):
    """
    A block quote
    
    :param text: Quote text
    :type text: :class:`RichText`
    
    :param credit: Quote credit
    :type credit: :class:`RichText`
    
    """

    ID: str = Field("pageBlockBlockQuote", alias="@type")
    text: RichText
    credit: RichText

    @staticmethod
    def read(q: dict) -> PageBlockBlockQuote:
        return PageBlockBlockQuote.construct(**q)


class PageBlockChatLink(PageBlock):
    """
    A link to a chat
    
    :param title: Chat title
    :type title: :class:`str`
    
    :param photo: Chat photo; may be null, defaults to None
    :type photo: :class:`ChatPhotoInfo`, optional
    
    :param username: Chat username, by which all other information about the chat should be resolved
    :type username: :class:`str`
    
    """

    ID: str = Field("pageBlockChatLink", alias="@type")
    title: str
    photo: typing.Optional[ChatPhotoInfo] = None
    username: str

    @staticmethod
    def read(q: dict) -> PageBlockChatLink:
        return PageBlockChatLink.construct(**q)


class PageBlockCollage(PageBlock):
    """
    A collage
    
    :param page_blocks: Collage item contents
    :type page_blocks: :class:`list[PageBlock]`
    
    :param caption: Block caption
    :type caption: :class:`PageBlockCaption`
    
    """

    ID: str = Field("pageBlockCollage", alias="@type")
    page_blocks: list[PageBlock]
    caption: PageBlockCaption

    @staticmethod
    def read(q: dict) -> PageBlockCollage:
        return PageBlockCollage.construct(**q)


class PageBlockCover(PageBlock):
    """
    A page cover
    
    :param cover: Cover
    :type cover: :class:`PageBlock`
    
    """

    ID: str = Field("pageBlockCover", alias="@type")
    cover: PageBlock

    @staticmethod
    def read(q: dict) -> PageBlockCover:
        return PageBlockCover.construct(**q)


class PageBlockDetails(PageBlock):
    """
    A collapsible block
    
    :param header: Always visible heading for the block
    :type header: :class:`RichText`
    
    :param page_blocks: Block contents
    :type page_blocks: :class:`list[PageBlock]`
    
    :param is_open: True, if the block is open by default
    :type is_open: :class:`bool`
    
    """

    ID: str = Field("pageBlockDetails", alias="@type")
    header: RichText
    page_blocks: list[PageBlock]
    is_open: bool

    @staticmethod
    def read(q: dict) -> PageBlockDetails:
        return PageBlockDetails.construct(**q)


class PageBlockDivider(PageBlock):
    """
    An empty block separating a page
    
    """

    ID: str = Field("pageBlockDivider", alias="@type")

    @staticmethod
    def read(q: dict) -> PageBlockDivider:
        return PageBlockDivider.construct(**q)


class PageBlockEmbedded(PageBlock):
    """
    An embedded web page
    
    :param url: Web page URL, if available
    :type url: :class:`str`
    
    :param html: HTML-markup of the embedded page
    :type html: :class:`str`
    
    :param poster_photo: Poster photo, if available; may be null, defaults to None
    :type poster_photo: :class:`Photo`, optional
    
    :param width: Block width; 0 if unknown
    :type width: :class:`int`
    
    :param height: Block height; 0 if unknown
    :type height: :class:`int`
    
    :param caption: Block caption
    :type caption: :class:`PageBlockCaption`
    
    :param is_full_width: True, if the block should be full width
    :type is_full_width: :class:`bool`
    
    :param allow_scrolling: True, if scrolling should be allowed
    :type allow_scrolling: :class:`bool`
    
    """

    ID: str = Field("pageBlockEmbedded", alias="@type")
    url: str
    html: str
    poster_photo: typing.Optional[Photo] = None
    width: int
    height: int
    caption: PageBlockCaption
    is_full_width: bool
    allow_scrolling: bool

    @staticmethod
    def read(q: dict) -> PageBlockEmbedded:
        return PageBlockEmbedded.construct(**q)


class PageBlockEmbeddedPost(PageBlock):
    """
    An embedded post
    
    :param url: Web page URL
    :type url: :class:`str`
    
    :param author: Post author
    :type author: :class:`str`
    
    :param author_photo: Post author photo; may be null, defaults to None
    :type author_photo: :class:`Photo`, optional
    
    :param date: Point in time (Unix timestamp) when the post was created; 0 if unknown
    :type date: :class:`int`
    
    :param page_blocks: Post content
    :type page_blocks: :class:`list[PageBlock]`
    
    :param caption: Post caption
    :type caption: :class:`PageBlockCaption`
    
    """

    ID: str = Field("pageBlockEmbeddedPost", alias="@type")
    url: str
    author: str
    author_photo: typing.Optional[Photo] = None
    date: int
    page_blocks: list[PageBlock]
    caption: PageBlockCaption

    @staticmethod
    def read(q: dict) -> PageBlockEmbeddedPost:
        return PageBlockEmbeddedPost.construct(**q)


class PageBlockFooter(PageBlock):
    """
    The footer of a page
    
    :param footer: Footer
    :type footer: :class:`RichText`
    
    """

    ID: str = Field("pageBlockFooter", alias="@type")
    footer: RichText

    @staticmethod
    def read(q: dict) -> PageBlockFooter:
        return PageBlockFooter.construct(**q)


class PageBlockHeader(PageBlock):
    """
    A header
    
    :param header: Header
    :type header: :class:`RichText`
    
    """

    ID: str = Field("pageBlockHeader", alias="@type")
    header: RichText

    @staticmethod
    def read(q: dict) -> PageBlockHeader:
        return PageBlockHeader.construct(**q)


class PageBlockKicker(PageBlock):
    """
    A kicker
    
    :param kicker: Kicker
    :type kicker: :class:`RichText`
    
    """

    ID: str = Field("pageBlockKicker", alias="@type")
    kicker: RichText

    @staticmethod
    def read(q: dict) -> PageBlockKicker:
        return PageBlockKicker.construct(**q)


class PageBlockList(PageBlock):
    """
    A list of data blocks
    
    :param items: The items of the list
    :type items: :class:`list[PageBlockListItem]`
    
    """

    ID: str = Field("pageBlockList", alias="@type")
    items: list[PageBlockListItem]

    @staticmethod
    def read(q: dict) -> PageBlockList:
        return PageBlockList.construct(**q)


class PageBlockMap(PageBlock):
    """
    A map
    
    :param location: Location of the map center
    :type location: :class:`Location`
    
    :param zoom: Map zoom level
    :type zoom: :class:`int`
    
    :param width: Map width
    :type width: :class:`int`
    
    :param height: Map height
    :type height: :class:`int`
    
    :param caption: Block caption
    :type caption: :class:`PageBlockCaption`
    
    """

    ID: str = Field("pageBlockMap", alias="@type")
    location: Location
    zoom: int
    width: int
    height: int
    caption: PageBlockCaption

    @staticmethod
    def read(q: dict) -> PageBlockMap:
        return PageBlockMap.construct(**q)


class PageBlockParagraph(PageBlock):
    """
    A text paragraph
    
    :param text: Paragraph text
    :type text: :class:`RichText`
    
    """

    ID: str = Field("pageBlockParagraph", alias="@type")
    text: RichText

    @staticmethod
    def read(q: dict) -> PageBlockParagraph:
        return PageBlockParagraph.construct(**q)


class PageBlockPhoto(PageBlock):
    """
    A photo
    
    :param photo: Photo file; may be null, defaults to None
    :type photo: :class:`Photo`, optional
    
    :param caption: Photo caption
    :type caption: :class:`PageBlockCaption`
    
    :param url: URL that needs to be opened when the photo is clicked
    :type url: :class:`str`
    
    """

    ID: str = Field("pageBlockPhoto", alias="@type")
    photo: typing.Optional[Photo] = None
    caption: PageBlockCaption
    url: str

    @staticmethod
    def read(q: dict) -> PageBlockPhoto:
        return PageBlockPhoto.construct(**q)


class PageBlockPreformatted(PageBlock):
    """
    A preformatted text paragraph
    
    :param text: Paragraph text
    :type text: :class:`RichText`
    
    :param language: Programming language for which the text should be formatted
    :type language: :class:`str`
    
    """

    ID: str = Field("pageBlockPreformatted", alias="@type")
    text: RichText
    language: str

    @staticmethod
    def read(q: dict) -> PageBlockPreformatted:
        return PageBlockPreformatted.construct(**q)


class PageBlockPullQuote(PageBlock):
    """
    A pull quote
    
    :param text: Quote text
    :type text: :class:`RichText`
    
    :param credit: Quote credit
    :type credit: :class:`RichText`
    
    """

    ID: str = Field("pageBlockPullQuote", alias="@type")
    text: RichText
    credit: RichText

    @staticmethod
    def read(q: dict) -> PageBlockPullQuote:
        return PageBlockPullQuote.construct(**q)


class PageBlockRelatedArticles(PageBlock):
    """
    Related articles
    
    :param header: Block header
    :type header: :class:`RichText`
    
    :param articles: List of related articles
    :type articles: :class:`list[PageBlockRelatedArticle]`
    
    """

    ID: str = Field("pageBlockRelatedArticles", alias="@type")
    header: RichText
    articles: list[PageBlockRelatedArticle]

    @staticmethod
    def read(q: dict) -> PageBlockRelatedArticles:
        return PageBlockRelatedArticles.construct(**q)


class PageBlockSlideshow(PageBlock):
    """
    A slideshow
    
    :param page_blocks: Slideshow item contents
    :type page_blocks: :class:`list[PageBlock]`
    
    :param caption: Block caption
    :type caption: :class:`PageBlockCaption`
    
    """

    ID: str = Field("pageBlockSlideshow", alias="@type")
    page_blocks: list[PageBlock]
    caption: PageBlockCaption

    @staticmethod
    def read(q: dict) -> PageBlockSlideshow:
        return PageBlockSlideshow.construct(**q)


class PageBlockSubheader(PageBlock):
    """
    A subheader
    
    :param subheader: Subheader
    :type subheader: :class:`RichText`
    
    """

    ID: str = Field("pageBlockSubheader", alias="@type")
    subheader: RichText

    @staticmethod
    def read(q: dict) -> PageBlockSubheader:
        return PageBlockSubheader.construct(**q)


class PageBlockSubtitle(PageBlock):
    """
    The subtitle of a page
    
    :param subtitle: Subtitle
    :type subtitle: :class:`RichText`
    
    """

    ID: str = Field("pageBlockSubtitle", alias="@type")
    subtitle: RichText

    @staticmethod
    def read(q: dict) -> PageBlockSubtitle:
        return PageBlockSubtitle.construct(**q)


class PageBlockTable(PageBlock):
    """
    A table
    
    :param caption: Table caption
    :type caption: :class:`RichText`
    
    :param cells: Table cells
    :type cells: :class:`list[list[PageBlockTableCell]]`
    
    :param is_bordered: True, if the table is bordered
    :type is_bordered: :class:`bool`
    
    :param is_striped: True, if the table is striped
    :type is_striped: :class:`bool`
    
    """

    ID: str = Field("pageBlockTable", alias="@type")
    caption: RichText
    cells: list[list[PageBlockTableCell]]
    is_bordered: bool
    is_striped: bool

    @staticmethod
    def read(q: dict) -> PageBlockTable:
        return PageBlockTable.construct(**q)


class PageBlockTitle(PageBlock):
    """
    The title of a page
    
    :param title: Title
    :type title: :class:`RichText`
    
    """

    ID: str = Field("pageBlockTitle", alias="@type")
    title: RichText

    @staticmethod
    def read(q: dict) -> PageBlockTitle:
        return PageBlockTitle.construct(**q)


class PageBlockVideo(PageBlock):
    """
    A video
    
    :param video: Video file; may be null, defaults to None
    :type video: :class:`Video`, optional
    
    :param caption: Video caption
    :type caption: :class:`PageBlockCaption`
    
    :param need_autoplay: True, if the video should be played automatically
    :type need_autoplay: :class:`bool`
    
    :param is_looped: True, if the video should be looped
    :type is_looped: :class:`bool`
    
    """

    ID: str = Field("pageBlockVideo", alias="@type")
    video: typing.Optional[Video] = None
    caption: PageBlockCaption
    need_autoplay: bool
    is_looped: bool

    @staticmethod
    def read(q: dict) -> PageBlockVideo:
        return PageBlockVideo.construct(**q)


class PageBlockVoiceNote(PageBlock):
    """
    A voice note
    
    :param voice_note: Voice note; may be null, defaults to None
    :type voice_note: :class:`VoiceNote`, optional
    
    :param caption: Voice note caption
    :type caption: :class:`PageBlockCaption`
    
    """

    ID: str = Field("pageBlockVoiceNote", alias="@type")
    voice_note: typing.Optional[VoiceNote] = None
    caption: PageBlockCaption

    @staticmethod
    def read(q: dict) -> PageBlockVoiceNote:
        return PageBlockVoiceNote.construct(**q)


class PageBlockListItem(BaseObject):
    """
    Describes an item of a list page block
    
    :param label: Item label
    :type label: :class:`str`
    
    :param page_blocks: Item blocks
    :type page_blocks: :class:`list[PageBlock]`
    
    """

    ID: str = Field("pageBlockListItem", alias="@type")
    label: str
    page_blocks: list[PageBlock]

    @staticmethod
    def read(q: dict) -> PageBlockListItem:
        return PageBlockListItem.construct(**q)
