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
from .contact import Contact
from .document import Document
from .game import Game
from .location import Location
from .photo import Photo
from .sticker import Sticker
from .thumbnail import Thumbnail
from .venue import Venue
from .video import Video
from .voice_note import VoiceNote
from ..base_object import BaseObject


class InlineQueryResult(BaseObject):
    """
    Represents a single result of an inline query
    
    """

    ID: str = Field("inlineQueryResult", alias="@type")


class InlineQueryResultAnimation(InlineQueryResult):
    """
    Represents an animation file
    
    Params:
        id (:class:`str`)
            Unique identifier of the query result
        
        animation (:class:`Animation`)
            Animation file
        
        title (:class:`str`)
            Animation title
        
    """

    ID: str = Field("inlineQueryResultAnimation", alias="@type")
    id: str
    animation: Animation
    title: str

    @staticmethod
    def read(q: dict) -> InlineQueryResultAnimation:
        return InlineQueryResultAnimation.construct(**q)


class InlineQueryResultArticle(InlineQueryResult):
    """
    Represents a link to an article or web page
    
    Params:
        id (:class:`str`)
            Unique identifier of the query result
        
        url (:class:`str`)
            URL of the result, if it exists
        
        hide_url (:class:`bool`)
            True, if the URL must be not shown
        
        title (:class:`str`)
            Title of the result
        
        param_description (:class:`str`)
            A short description of the result
        
        thumbnail (:class:`Thumbnail`)
            Result thumbnail in JPEG format; may be null
        
    """

    ID: str = Field("inlineQueryResultArticle", alias="@type")
    id: str
    url: str
    hide_url: bool
    title: str
    param_description: str
    thumbnail: typing.Optional[Thumbnail] = None

    @staticmethod
    def read(q: dict) -> InlineQueryResultArticle:
        return InlineQueryResultArticle.construct(**q)


class InlineQueryResultAudio(InlineQueryResult):
    """
    Represents an audio file
    
    Params:
        id (:class:`str`)
            Unique identifier of the query result
        
        audio (:class:`Audio`)
            Audio file
        
    """

    ID: str = Field("inlineQueryResultAudio", alias="@type")
    id: str
    audio: Audio

    @staticmethod
    def read(q: dict) -> InlineQueryResultAudio:
        return InlineQueryResultAudio.construct(**q)


class InlineQueryResultContact(InlineQueryResult):
    """
    Represents a user contact
    
    Params:
        id (:class:`str`)
            Unique identifier of the query result
        
        contact (:class:`Contact`)
            A user contact
        
        thumbnail (:class:`Thumbnail`)
            Result thumbnail in JPEG format; may be null
        
    """

    ID: str = Field("inlineQueryResultContact", alias="@type")
    id: str
    contact: Contact
    thumbnail: typing.Optional[Thumbnail] = None

    @staticmethod
    def read(q: dict) -> InlineQueryResultContact:
        return InlineQueryResultContact.construct(**q)


class InlineQueryResultDocument(InlineQueryResult):
    """
    Represents a document
    
    Params:
        id (:class:`str`)
            Unique identifier of the query result
        
        document (:class:`Document`)
            Document
        
        title (:class:`str`)
            Document title
        
        param_description (:class:`str`)
            Document description
        
    """

    ID: str = Field("inlineQueryResultDocument", alias="@type")
    id: str
    document: Document
    title: str
    param_description: str

    @staticmethod
    def read(q: dict) -> InlineQueryResultDocument:
        return InlineQueryResultDocument.construct(**q)


class InlineQueryResultGame(InlineQueryResult):
    """
    Represents information about a game
    
    Params:
        id (:class:`str`)
            Unique identifier of the query result
        
        game (:class:`Game`)
            Game result
        
    """

    ID: str = Field("inlineQueryResultGame", alias="@type")
    id: str
    game: Game

    @staticmethod
    def read(q: dict) -> InlineQueryResultGame:
        return InlineQueryResultGame.construct(**q)


class InlineQueryResultLocation(InlineQueryResult):
    """
    Represents a point on the map
    
    Params:
        id (:class:`str`)
            Unique identifier of the query result
        
        location (:class:`Location`)
            Location result
        
        title (:class:`str`)
            Title of the result
        
        thumbnail (:class:`Thumbnail`)
            Result thumbnail in JPEG format; may be null
        
    """

    ID: str = Field("inlineQueryResultLocation", alias="@type")
    id: str
    location: Location
    title: str
    thumbnail: typing.Optional[Thumbnail] = None

    @staticmethod
    def read(q: dict) -> InlineQueryResultLocation:
        return InlineQueryResultLocation.construct(**q)


class InlineQueryResultPhoto(InlineQueryResult):
    """
    Represents a photo
    
    Params:
        id (:class:`str`)
            Unique identifier of the query result
        
        photo (:class:`Photo`)
            Photo
        
        title (:class:`str`)
            Title of the result, if known
        
        param_description (:class:`str`)
            A short description of the result, if known
        
    """

    ID: str = Field("inlineQueryResultPhoto", alias="@type")
    id: str
    photo: Photo
    title: str
    param_description: str

    @staticmethod
    def read(q: dict) -> InlineQueryResultPhoto:
        return InlineQueryResultPhoto.construct(**q)


class InlineQueryResultSticker(InlineQueryResult):
    """
    Represents a sticker
    
    Params:
        id (:class:`str`)
            Unique identifier of the query result
        
        sticker (:class:`Sticker`)
            Sticker
        
    """

    ID: str = Field("inlineQueryResultSticker", alias="@type")
    id: str
    sticker: Sticker

    @staticmethod
    def read(q: dict) -> InlineQueryResultSticker:
        return InlineQueryResultSticker.construct(**q)


class InlineQueryResultVenue(InlineQueryResult):
    """
    Represents information about a venue
    
    Params:
        id (:class:`str`)
            Unique identifier of the query result
        
        venue (:class:`Venue`)
            Venue result
        
        thumbnail (:class:`Thumbnail`)
            Result thumbnail in JPEG format; may be null
        
    """

    ID: str = Field("inlineQueryResultVenue", alias="@type")
    id: str
    venue: Venue
    thumbnail: typing.Optional[Thumbnail] = None

    @staticmethod
    def read(q: dict) -> InlineQueryResultVenue:
        return InlineQueryResultVenue.construct(**q)


class InlineQueryResultVideo(InlineQueryResult):
    """
    Represents a video
    
    Params:
        id (:class:`str`)
            Unique identifier of the query result
        
        video (:class:`Video`)
            Video
        
        title (:class:`str`)
            Title of the video
        
        param_description (:class:`str`)
            Description of the video
        
    """

    ID: str = Field("inlineQueryResultVideo", alias="@type")
    id: str
    video: Video
    title: str
    param_description: str

    @staticmethod
    def read(q: dict) -> InlineQueryResultVideo:
        return InlineQueryResultVideo.construct(**q)


class InlineQueryResultVoiceNote(InlineQueryResult):
    """
    Represents a voice note
    
    Params:
        id (:class:`str`)
            Unique identifier of the query result
        
        voice_note (:class:`VoiceNote`)
            Voice note
        
        title (:class:`str`)
            Title of the voice note
        
    """

    ID: str = Field("inlineQueryResultVoiceNote", alias="@type")
    id: str
    voice_note: VoiceNote
    title: str

    @staticmethod
    def read(q: dict) -> InlineQueryResultVoiceNote:
        return InlineQueryResultVoiceNote.construct(**q)
