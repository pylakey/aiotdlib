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
    
    :param id: Unique identifier of the query result
    :type id: :class:`str`
    
    :param animation: Animation file
    :type animation: :class:`Animation`
    
    :param title: Animation title
    :type title: :class:`str`
    
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
    
    :param id: Unique identifier of the query result
    :type id: :class:`str`
    
    :param url: URL of the result, if it exists
    :type url: :class:`str`
    
    :param hide_url: True, if the URL must be not shown
    :type hide_url: :class:`bool`
    
    :param title: Title of the result
    :type title: :class:`str`
    
    :param param_description: A short description of the result
    :type param_description: :class:`str`
    
    :param thumbnail: Result thumbnail in JPEG format; may be null, defaults to None
    :type thumbnail: :class:`Thumbnail`, optional
    
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
    
    :param id: Unique identifier of the query result
    :type id: :class:`str`
    
    :param audio: Audio file
    :type audio: :class:`Audio`
    
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
    
    :param id: Unique identifier of the query result
    :type id: :class:`str`
    
    :param contact: A user contact
    :type contact: :class:`Contact`
    
    :param thumbnail: Result thumbnail in JPEG format; may be null, defaults to None
    :type thumbnail: :class:`Thumbnail`, optional
    
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
    
    :param id: Unique identifier of the query result
    :type id: :class:`str`
    
    :param document: Document
    :type document: :class:`Document`
    
    :param title: Document title
    :type title: :class:`str`
    
    :param param_description: Document description
    :type param_description: :class:`str`
    
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
    
    :param id: Unique identifier of the query result
    :type id: :class:`str`
    
    :param game: Game result
    :type game: :class:`Game`
    
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
    
    :param id: Unique identifier of the query result
    :type id: :class:`str`
    
    :param location: Location result
    :type location: :class:`Location`
    
    :param title: Title of the result
    :type title: :class:`str`
    
    :param thumbnail: Result thumbnail in JPEG format; may be null, defaults to None
    :type thumbnail: :class:`Thumbnail`, optional
    
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
    
    :param id: Unique identifier of the query result
    :type id: :class:`str`
    
    :param photo: Photo
    :type photo: :class:`Photo`
    
    :param title: Title of the result, if known
    :type title: :class:`str`
    
    :param param_description: A short description of the result, if known
    :type param_description: :class:`str`
    
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
    
    :param id: Unique identifier of the query result
    :type id: :class:`str`
    
    :param sticker: Sticker
    :type sticker: :class:`Sticker`
    
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
    
    :param id: Unique identifier of the query result
    :type id: :class:`str`
    
    :param venue: Venue result
    :type venue: :class:`Venue`
    
    :param thumbnail: Result thumbnail in JPEG format; may be null, defaults to None
    :type thumbnail: :class:`Thumbnail`, optional
    
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
    
    :param id: Unique identifier of the query result
    :type id: :class:`str`
    
    :param video: Video
    :type video: :class:`Video`
    
    :param title: Title of the video
    :type title: :class:`str`
    
    :param param_description: Description of the video
    :type param_description: :class:`str`
    
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
    
    :param id: Unique identifier of the query result
    :type id: :class:`str`
    
    :param voice_note: Voice note
    :type voice_note: :class:`VoiceNote`
    
    :param title: Title of the voice note
    :type title: :class:`str`
    
    """

    ID: str = Field("inlineQueryResultVoiceNote", alias="@type")
    id: str
    voice_note: VoiceNote
    title: str

    @staticmethod
    def read(q: dict) -> InlineQueryResultVoiceNote:
        return InlineQueryResultVoiceNote.construct(**q)
