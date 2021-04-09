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
    
    Params:
        name (:class:`str`)
            Name of the anchor
        
    """

    ID: str = Field("pageBlockAnchor", alias="@type")
    name: str

    @staticmethod
    def read(q: dict) -> PageBlockAnchor:
        return PageBlockAnchor.construct(**q)


class PageBlockAnimation(PageBlock):
    """
    An animation
    
    Params:
        animation (:class:`Animation`)
            Animation file; may be null
        
        caption (:class:`PageBlockCaption`)
            Animation caption
        
        need_autoplay (:class:`bool`)
            True, if the animation should be played automatically
        
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
    
    Params:
        audio (:class:`Audio`)
            Audio file; may be null
        
        caption (:class:`PageBlockCaption`)
            Audio file caption
        
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
    
    Params:
        author (:class:`RichText`)
            Author
        
        publish_date (:class:`int`)
            Point in time (Unix timestamp) when the article was published; 0 if unknown
        
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
    
    Params:
        text (:class:`RichText`)
            Quote text
        
        credit (:class:`RichText`)
            Quote credit
        
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
    
    Params:
        title (:class:`str`)
            Chat title
        
        photo (:class:`ChatPhotoInfo`)
            Chat photo; may be null
        
        username (:class:`str`)
            Chat username, by which all other information about the chat should be resolved
        
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
    
    Params:
        page_blocks (:obj:`list[PageBlock]`)
            Collage item contents
        
        caption (:class:`PageBlockCaption`)
            Block caption
        
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
    
    Params:
        cover (:class:`PageBlock`)
            Cover
        
    """

    ID: str = Field("pageBlockCover", alias="@type")
    cover: PageBlock

    @staticmethod
    def read(q: dict) -> PageBlockCover:
        return PageBlockCover.construct(**q)


class PageBlockDetails(PageBlock):
    """
    A collapsible block
    
    Params:
        header (:class:`RichText`)
            Always visible heading for the block
        
        page_blocks (:obj:`list[PageBlock]`)
            Block contents
        
        is_open (:class:`bool`)
            True, if the block is open by default
        
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
    
    Params:
        url (:class:`str`)
            Web page URL, if available
        
        html (:class:`str`)
            HTML-markup of the embedded page
        
        poster_photo (:class:`Photo`)
            Poster photo, if available; may be null
        
        width (:class:`int`)
            Block width; 0 if unknown
        
        height (:class:`int`)
            Block height; 0 if unknown
        
        caption (:class:`PageBlockCaption`)
            Block caption
        
        is_full_width (:class:`bool`)
            True, if the block should be full width
        
        allow_scrolling (:class:`bool`)
            True, if scrolling should be allowed
        
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
    
    Params:
        url (:class:`str`)
            Web page URL
        
        author (:class:`str`)
            Post author
        
        author_photo (:class:`Photo`)
            Post author photo; may be null
        
        date (:class:`int`)
            Point in time (Unix timestamp) when the post was created; 0 if unknown
        
        page_blocks (:obj:`list[PageBlock]`)
            Post content
        
        caption (:class:`PageBlockCaption`)
            Post caption
        
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
    
    Params:
        footer (:class:`RichText`)
            Footer
        
    """

    ID: str = Field("pageBlockFooter", alias="@type")
    footer: RichText

    @staticmethod
    def read(q: dict) -> PageBlockFooter:
        return PageBlockFooter.construct(**q)


class PageBlockHeader(PageBlock):
    """
    A header
    
    Params:
        header (:class:`RichText`)
            Header
        
    """

    ID: str = Field("pageBlockHeader", alias="@type")
    header: RichText

    @staticmethod
    def read(q: dict) -> PageBlockHeader:
        return PageBlockHeader.construct(**q)


class PageBlockKicker(PageBlock):
    """
    A kicker
    
    Params:
        kicker (:class:`RichText`)
            Kicker
        
    """

    ID: str = Field("pageBlockKicker", alias="@type")
    kicker: RichText

    @staticmethod
    def read(q: dict) -> PageBlockKicker:
        return PageBlockKicker.construct(**q)


class PageBlockList(PageBlock):
    """
    A list of data blocks
    
    Params:
        items (:obj:`list[PageBlockListItem]`)
            The items of the list
        
    """

    ID: str = Field("pageBlockList", alias="@type")
    items: list[PageBlockListItem]

    @staticmethod
    def read(q: dict) -> PageBlockList:
        return PageBlockList.construct(**q)


class PageBlockMap(PageBlock):
    """
    A map
    
    Params:
        location (:class:`Location`)
            Location of the map center
        
        zoom (:class:`int`)
            Map zoom level
        
        width (:class:`int`)
            Map width
        
        height (:class:`int`)
            Map height
        
        caption (:class:`PageBlockCaption`)
            Block caption
        
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
    
    Params:
        text (:class:`RichText`)
            Paragraph text
        
    """

    ID: str = Field("pageBlockParagraph", alias="@type")
    text: RichText

    @staticmethod
    def read(q: dict) -> PageBlockParagraph:
        return PageBlockParagraph.construct(**q)


class PageBlockPhoto(PageBlock):
    """
    A photo
    
    Params:
        photo (:class:`Photo`)
            Photo file; may be null
        
        caption (:class:`PageBlockCaption`)
            Photo caption
        
        url (:class:`str`)
            URL that needs to be opened when the photo is clicked
        
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
    
    Params:
        text (:class:`RichText`)
            Paragraph text
        
        language (:class:`str`)
            Programming language for which the text should be formatted
        
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
    
    Params:
        text (:class:`RichText`)
            Quote text
        
        credit (:class:`RichText`)
            Quote credit
        
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
    
    Params:
        header (:class:`RichText`)
            Block header
        
        articles (:obj:`list[PageBlockRelatedArticle]`)
            List of related articles
        
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
    
    Params:
        page_blocks (:obj:`list[PageBlock]`)
            Slideshow item contents
        
        caption (:class:`PageBlockCaption`)
            Block caption
        
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
    
    Params:
        subheader (:class:`RichText`)
            Subheader
        
    """

    ID: str = Field("pageBlockSubheader", alias="@type")
    subheader: RichText

    @staticmethod
    def read(q: dict) -> PageBlockSubheader:
        return PageBlockSubheader.construct(**q)


class PageBlockSubtitle(PageBlock):
    """
    The subtitle of a page
    
    Params:
        subtitle (:class:`RichText`)
            Subtitle
        
    """

    ID: str = Field("pageBlockSubtitle", alias="@type")
    subtitle: RichText

    @staticmethod
    def read(q: dict) -> PageBlockSubtitle:
        return PageBlockSubtitle.construct(**q)


class PageBlockTable(PageBlock):
    """
    A table
    
    Params:
        caption (:class:`RichText`)
            Table caption
        
        cells (:obj:`list[list[PageBlockTableCell]]`)
            Table cells
        
        is_bordered (:class:`bool`)
            True, if the table is bordered
        
        is_striped (:class:`bool`)
            True, if the table is striped
        
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
    
    Params:
        title (:class:`RichText`)
            Title
        
    """

    ID: str = Field("pageBlockTitle", alias="@type")
    title: RichText

    @staticmethod
    def read(q: dict) -> PageBlockTitle:
        return PageBlockTitle.construct(**q)


class PageBlockVideo(PageBlock):
    """
    A video
    
    Params:
        video (:class:`Video`)
            Video file; may be null
        
        caption (:class:`PageBlockCaption`)
            Video caption
        
        need_autoplay (:class:`bool`)
            True, if the video should be played automatically
        
        is_looped (:class:`bool`)
            True, if the video should be looped
        
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
    
    Params:
        voice_note (:class:`VoiceNote`)
            Voice note; may be null
        
        caption (:class:`PageBlockCaption`)
            Voice note caption
        
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
    
    Params:
        label (:class:`str`)
            Item label
        
        page_blocks (:obj:`list[PageBlock]`)
            Item blocks
        
    """

    ID: str = Field("pageBlockListItem", alias="@type")
    label: str
    page_blocks: list[PageBlock]

    @staticmethod
    def read(q: dict) -> PageBlockListItem:
        return PageBlockListItem.construct(**q)
