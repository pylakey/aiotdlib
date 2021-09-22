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
    
    :param url: Original URL of the link
    :type url: :class:`str`
    
    :param display_url: URL to display
    :type display_url: :class:`str`
    
    :param type_: Type of the web page. Can be: article, photo, audio, video, document, profile, app, or something else
    :type type_: :class:`str`
    
    :param site_name: Short name of the site (e.g., Google Docs, App Store)
    :type site_name: :class:`str`
    
    :param title: Title of the content
    :type title: :class:`str`
    
    :param param_description: Description of the content
    :type param_description: :class:`FormattedText`
    
    :param photo: Image representing the content; may be null, defaults to None
    :type photo: :class:`Photo`, optional
    
    :param embed_url: URL to show in the embedded preview
    :type embed_url: :class:`str`
    
    :param embed_type: MIME type of the embedded preview, (e.g., text/html or video/mp4)
    :type embed_type: :class:`str`
    
    :param embed_width: Width of the embedded preview
    :type embed_width: :class:`int`
    
    :param embed_height: Height of the embedded preview
    :type embed_height: :class:`int`
    
    :param duration: Duration of the content, in seconds
    :type duration: :class:`int`
    
    :param author: Author of the content
    :type author: :class:`str`
    
    :param animation: Preview of the content as an animation, if available; may be null, defaults to None
    :type animation: :class:`Animation`, optional
    
    :param audio: Preview of the content as an audio file, if available; may be null, defaults to None
    :type audio: :class:`Audio`, optional
    
    :param document: Preview of the content as a document, if available (currently only available for small PDF files and ZIP archives); may be null, defaults to None
    :type document: :class:`Document`, optional
    
    :param sticker: Preview of the content as a sticker for small WEBP files, if available; may be null, defaults to None
    :type sticker: :class:`Sticker`, optional
    
    :param video: Preview of the content as a video, if available; may be null, defaults to None
    :type video: :class:`Video`, optional
    
    :param video_note: Preview of the content as a video note, if available; may be null, defaults to None
    :type video_note: :class:`VideoNote`, optional
    
    :param voice_note: Preview of the content as a voice note, if available; may be null, defaults to None
    :type voice_note: :class:`VoiceNote`, optional
    
    :param instant_view_version: Version of instant view, available for the web page (currently can be 1 or 2), 0 if none
    :type instant_view_version: :class:`int`
    
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
