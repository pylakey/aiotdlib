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
from .document import Document
from .formatted_text import FormattedText
from .photo import Photo
from .sticker import Sticker
from .video import Video
from .video_note import VideoNote
from .voice_note import VoiceNote
from ..base_object import BaseObject


class WebPage(BaseObject):
    """
    Describes a web page preview
    
    Params:
        url (:class:`str`)
            Original URL of the link
        
        display_url (:class:`str`)
            URL to display
        
        type_ (:class:`str`)
            Type of the web page. Can be: article, photo, audio, video, document, profile, app, or something else
        
        site_name (:class:`str`)
            Short name of the site (e.g., Google Docs, App Store)
        
        title (:class:`str`)
            Title of the content
        
        param_description (:class:`FormattedText`)
            Description of the content
        
        photo (:class:`Photo`)
            Image representing the content; may be null
        
        embed_url (:class:`str`)
            URL to show in the embedded preview
        
        embed_type (:class:`str`)
            MIME type of the embedded preview, (e.g., text/html or video/mp4)
        
        embed_width (:class:`int`)
            Width of the embedded preview
        
        embed_height (:class:`int`)
            Height of the embedded preview
        
        duration (:class:`int`)
            Duration of the content, in seconds
        
        author (:class:`str`)
            Author of the content
        
        animation (:class:`Animation`)
            Preview of the content as an animation, if available; may be null
        
        audio (:class:`Audio`)
            Preview of the content as an audio file, if available; may be null
        
        document (:class:`Document`)
            Preview of the content as a document, if available (currently only available for small PDF files and ZIP archives); may be null
        
        sticker (:class:`Sticker`)
            Preview of the content as a sticker for small WEBP files, if available; may be null
        
        video (:class:`Video`)
            Preview of the content as a video, if available; may be null
        
        video_note (:class:`VideoNote`)
            Preview of the content as a video note, if available; may be null
        
        voice_note (:class:`VoiceNote`)
            Preview of the content as a voice note, if available; may be null
        
        instant_view_version (:class:`int`)
            Version of instant view, available for the web page (currently can be 1 or 2), 0 if none
        
    """

    ID: str = Field("webPage", alias="@type")
    url: str
    display_url: str
    type_: str = Field(..., alias='type')
    site_name: str
    title: str
    param_description: FormattedText
    photo: typing.Optional[Photo] = None
    embed_url: str
    embed_type: str
    embed_width: int
    embed_height: int
    duration: int
    author: str
    animation: typing.Optional[Animation] = None
    audio: typing.Optional[Audio] = None
    document: typing.Optional[Document] = None
    sticker: typing.Optional[Sticker] = None
    video: typing.Optional[Video] = None
    video_note: typing.Optional[VideoNote] = None
    voice_note: typing.Optional[VoiceNote] = None
    instant_view_version: int

    @staticmethod
    def read(q: dict) -> WebPage:
        return WebPage.construct(**q)
