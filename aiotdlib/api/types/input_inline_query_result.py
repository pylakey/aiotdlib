# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .contact import Contact
from .input_message_content import InputMessageContent
from .location import Location
from .reply_markup import ReplyMarkup
from .venue import Venue
from ..base_object import BaseObject


class InputInlineQueryResult(BaseObject):
    """
    Represents a single result of an inline query; for bots only
    
    """

    ID: str = Field("inputInlineQueryResult", alias="@type")


class InputInlineQueryResultAnimation(InputInlineQueryResult):
    """
    Represents a link to an animated GIF or an animated (i.e. without sound) H.264/MPEG-4 AVC video
    
    Params:
        id (:class:`str`)
            Unique identifier of the query result
        
        title (:class:`str`)
            Title of the query result
        
        thumbnail_url (:class:`str`)
            URL of the result thumbnail (JPEG, GIF, or MPEG4), if it exists
        
        thumbnail_mime_type (:class:`str`)
            MIME type of the video thumbnail. If non-empty, must be one of "image/jpeg", "image/gif" and "video/mp4"
        
        video_url (:class:`str`)
            The URL of the video file (file size must not exceed 1MB)
        
        video_mime_type (:class:`str`)
            MIME type of the video file. Must be one of "image/gif" and "video/mp4"
        
        video_duration (:class:`int`)
            Duration of the video, in seconds
        
        video_width (:class:`int`)
            Width of the video
        
        video_height (:class:`int`)
            Height of the video
        
        reply_markup (:class:`ReplyMarkup`)
            The message reply markup. Must be of type replyMarkupInlineKeyboard or null
        
        input_message_content (:class:`InputMessageContent`)
            The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageAnimation, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
        
    """

    ID: str = Field("inputInlineQueryResultAnimation", alias="@type")
    id: str
    title: str
    thumbnail_url: str
    thumbnail_mime_type: str
    video_url: str
    video_mime_type: str
    video_duration: int
    video_width: int
    video_height: int
    reply_markup: ReplyMarkup
    input_message_content: InputMessageContent

    @staticmethod
    def read(q: dict) -> InputInlineQueryResultAnimation:
        return InputInlineQueryResultAnimation.construct(**q)


class InputInlineQueryResultArticle(InputInlineQueryResult):
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
        
        thumbnail_url (:class:`str`)
            URL of the result thumbnail, if it exists
        
        thumbnail_width (:class:`int`)
            Thumbnail width, if known
        
        thumbnail_height (:class:`int`)
            Thumbnail height, if known
        
        reply_markup (:class:`ReplyMarkup`)
            The message reply markup. Must be of type replyMarkupInlineKeyboard or null
        
        input_message_content (:class:`InputMessageContent`)
            The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
        
    """

    ID: str = Field("inputInlineQueryResultArticle", alias="@type")
    id: str
    url: str
    hide_url: bool
    title: str
    param_description: str
    thumbnail_url: str
    thumbnail_width: int
    thumbnail_height: int
    reply_markup: ReplyMarkup
    input_message_content: InputMessageContent

    @staticmethod
    def read(q: dict) -> InputInlineQueryResultArticle:
        return InputInlineQueryResultArticle.construct(**q)


class InputInlineQueryResultAudio(InputInlineQueryResult):
    """
    Represents a link to an MP3 audio file
    
    Params:
        id (:class:`str`)
            Unique identifier of the query result
        
        title (:class:`str`)
            Title of the audio file
        
        performer (:class:`str`)
            Performer of the audio file
        
        audio_url (:class:`str`)
            The URL of the audio file
        
        audio_duration (:class:`int`)
            Audio file duration, in seconds
        
        reply_markup (:class:`ReplyMarkup`)
            The message reply markup. Must be of type replyMarkupInlineKeyboard or null
        
        input_message_content (:class:`InputMessageContent`)
            The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageAudio, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
        
    """

    ID: str = Field("inputInlineQueryResultAudio", alias="@type")
    id: str
    title: str
    performer: str
    audio_url: str
    audio_duration: int
    reply_markup: ReplyMarkup
    input_message_content: InputMessageContent

    @staticmethod
    def read(q: dict) -> InputInlineQueryResultAudio:
        return InputInlineQueryResultAudio.construct(**q)


class InputInlineQueryResultContact(InputInlineQueryResult):
    """
    Represents a user contact
    
    Params:
        id (:class:`str`)
            Unique identifier of the query result
        
        contact (:class:`Contact`)
            User contact
        
        thumbnail_url (:class:`str`)
            URL of the result thumbnail, if it exists
        
        thumbnail_width (:class:`int`)
            Thumbnail width, if known
        
        thumbnail_height (:class:`int`)
            Thumbnail height, if known
        
        reply_markup (:class:`ReplyMarkup`)
            The message reply markup. Must be of type replyMarkupInlineKeyboard or null
        
        input_message_content (:class:`InputMessageContent`)
            The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
        
    """

    ID: str = Field("inputInlineQueryResultContact", alias="@type")
    id: str
    contact: Contact
    thumbnail_url: str
    thumbnail_width: int
    thumbnail_height: int
    reply_markup: ReplyMarkup
    input_message_content: InputMessageContent

    @staticmethod
    def read(q: dict) -> InputInlineQueryResultContact:
        return InputInlineQueryResultContact.construct(**q)


class InputInlineQueryResultDocument(InputInlineQueryResult):
    """
    Represents a link to a file
    
    Params:
        id (:class:`str`)
            Unique identifier of the query result
        
        title (:class:`str`)
            Title of the resulting file
        
        param_description (:class:`str`)
            Short description of the result, if known
        
        document_url (:class:`str`)
            URL of the file
        
        mime_type (:class:`str`)
            MIME type of the file content; only "application/pdf" and "application/zip" are currently allowed
        
        thumbnail_url (:class:`str`)
            The URL of the file thumbnail, if it exists
        
        thumbnail_width (:class:`int`)
            Width of the thumbnail
        
        thumbnail_height (:class:`int`)
            Height of the thumbnail
        
        reply_markup (:class:`ReplyMarkup`)
            The message reply markup. Must be of type replyMarkupInlineKeyboard or null
        
        input_message_content (:class:`InputMessageContent`)
            The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageDocument, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
        
    """

    ID: str = Field("inputInlineQueryResultDocument", alias="@type")
    id: str
    title: str
    param_description: str
    document_url: str
    mime_type: str
    thumbnail_url: str
    thumbnail_width: int
    thumbnail_height: int
    reply_markup: ReplyMarkup
    input_message_content: InputMessageContent

    @staticmethod
    def read(q: dict) -> InputInlineQueryResultDocument:
        return InputInlineQueryResultDocument.construct(**q)


class InputInlineQueryResultGame(InputInlineQueryResult):
    """
    Represents a game
    
    Params:
        id (:class:`str`)
            Unique identifier of the query result
        
        game_short_name (:class:`str`)
            Short name of the game
        
        reply_markup (:class:`ReplyMarkup`)
            Message reply markup. Must be of type replyMarkupInlineKeyboard or null
        
    """

    ID: str = Field("inputInlineQueryResultGame", alias="@type")
    id: str
    game_short_name: str
    reply_markup: ReplyMarkup

    @staticmethod
    def read(q: dict) -> InputInlineQueryResultGame:
        return InputInlineQueryResultGame.construct(**q)


class InputInlineQueryResultLocation(InputInlineQueryResult):
    """
    Represents a point on the map
    
    Params:
        id (:class:`str`)
            Unique identifier of the query result
        
        location (:class:`Location`)
            Location result
        
        live_period (:class:`int`)
            Amount of time relative to the message sent time until the location can be updated, in seconds
        
        title (:class:`str`)
            Title of the result
        
        thumbnail_url (:class:`str`)
            URL of the result thumbnail, if it exists
        
        thumbnail_width (:class:`int`)
            Thumbnail width, if known
        
        thumbnail_height (:class:`int`)
            Thumbnail height, if known
        
        reply_markup (:class:`ReplyMarkup`)
            The message reply markup. Must be of type replyMarkupInlineKeyboard or null
        
        input_message_content (:class:`InputMessageContent`)
            The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
        
    """

    ID: str = Field("inputInlineQueryResultLocation", alias="@type")
    id: str
    location: Location
    live_period: int
    title: str
    thumbnail_url: str
    thumbnail_width: int
    thumbnail_height: int
    reply_markup: ReplyMarkup
    input_message_content: InputMessageContent

    @staticmethod
    def read(q: dict) -> InputInlineQueryResultLocation:
        return InputInlineQueryResultLocation.construct(**q)


class InputInlineQueryResultPhoto(InputInlineQueryResult):
    """
    Represents link to a JPEG image
    
    Params:
        id (:class:`str`)
            Unique identifier of the query result
        
        title (:class:`str`)
            Title of the result, if known
        
        param_description (:class:`str`)
            A short description of the result, if known
        
        thumbnail_url (:class:`str`)
            URL of the photo thumbnail, if it exists
        
        photo_url (:class:`str`)
            The URL of the JPEG photo (photo size must not exceed 5MB)
        
        photo_width (:class:`int`)
            Width of the photo
        
        photo_height (:class:`int`)
            Height of the photo
        
        reply_markup (:class:`ReplyMarkup`)
            The message reply markup. Must be of type replyMarkupInlineKeyboard or null
        
        input_message_content (:class:`InputMessageContent`)
            The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessagePhoto, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
        
    """

    ID: str = Field("inputInlineQueryResultPhoto", alias="@type")
    id: str
    title: str
    param_description: str
    thumbnail_url: str
    photo_url: str
    photo_width: int
    photo_height: int
    reply_markup: ReplyMarkup
    input_message_content: InputMessageContent

    @staticmethod
    def read(q: dict) -> InputInlineQueryResultPhoto:
        return InputInlineQueryResultPhoto.construct(**q)


class InputInlineQueryResultSticker(InputInlineQueryResult):
    """
    Represents a link to a WEBP or TGS sticker
    
    Params:
        id (:class:`str`)
            Unique identifier of the query result
        
        thumbnail_url (:class:`str`)
            URL of the sticker thumbnail, if it exists
        
        sticker_url (:class:`str`)
            The URL of the WEBP or TGS sticker (sticker file size must not exceed 5MB)
        
        sticker_width (:class:`int`)
            Width of the sticker
        
        sticker_height (:class:`int`)
            Height of the sticker
        
        reply_markup (:class:`ReplyMarkup`)
            The message reply markup. Must be of type replyMarkupInlineKeyboard or null
        
        input_message_content (:class:`InputMessageContent`)
            The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageSticker, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
        
    """

    ID: str = Field("inputInlineQueryResultSticker", alias="@type")
    id: str
    thumbnail_url: str
    sticker_url: str
    sticker_width: int
    sticker_height: int
    reply_markup: ReplyMarkup
    input_message_content: InputMessageContent

    @staticmethod
    def read(q: dict) -> InputInlineQueryResultSticker:
        return InputInlineQueryResultSticker.construct(**q)


class InputInlineQueryResultVenue(InputInlineQueryResult):
    """
    Represents information about a venue
    
    Params:
        id (:class:`str`)
            Unique identifier of the query result
        
        venue (:class:`Venue`)
            Venue result
        
        thumbnail_url (:class:`str`)
            URL of the result thumbnail, if it exists
        
        thumbnail_width (:class:`int`)
            Thumbnail width, if known
        
        thumbnail_height (:class:`int`)
            Thumbnail height, if known
        
        reply_markup (:class:`ReplyMarkup`)
            The message reply markup. Must be of type replyMarkupInlineKeyboard or null
        
        input_message_content (:class:`InputMessageContent`)
            The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
        
    """

    ID: str = Field("inputInlineQueryResultVenue", alias="@type")
    id: str
    venue: Venue
    thumbnail_url: str
    thumbnail_width: int
    thumbnail_height: int
    reply_markup: ReplyMarkup
    input_message_content: InputMessageContent

    @staticmethod
    def read(q: dict) -> InputInlineQueryResultVenue:
        return InputInlineQueryResultVenue.construct(**q)


class InputInlineQueryResultVideo(InputInlineQueryResult):
    """
    Represents a link to a page containing an embedded video player or a video file
    
    Params:
        id (:class:`str`)
            Unique identifier of the query result
        
        title (:class:`str`)
            Title of the result
        
        param_description (:class:`str`)
            A short description of the result, if known
        
        thumbnail_url (:class:`str`)
            The URL of the video thumbnail (JPEG), if it exists
        
        video_url (:class:`str`)
            URL of the embedded video player or video file
        
        mime_type (:class:`str`)
            MIME type of the content of the video URL, only "text/html" or "video/mp4" are currently supported
        
        video_width (:class:`int`)
            Width of the video
        
        video_height (:class:`int`)
            Height of the video
        
        video_duration (:class:`int`)
            Video duration, in seconds
        
        reply_markup (:class:`ReplyMarkup`)
            The message reply markup. Must be of type replyMarkupInlineKeyboard or null
        
        input_message_content (:class:`InputMessageContent`)
            The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageVideo, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
        
    """

    ID: str = Field("inputInlineQueryResultVideo", alias="@type")
    id: str
    title: str
    param_description: str
    thumbnail_url: str
    video_url: str
    mime_type: str
    video_width: int
    video_height: int
    video_duration: int
    reply_markup: ReplyMarkup
    input_message_content: InputMessageContent

    @staticmethod
    def read(q: dict) -> InputInlineQueryResultVideo:
        return InputInlineQueryResultVideo.construct(**q)


class InputInlineQueryResultVoiceNote(InputInlineQueryResult):
    """
    Represents a link to an opus-encoded audio file within an OGG container, single channel audio
    
    Params:
        id (:class:`str`)
            Unique identifier of the query result
        
        title (:class:`str`)
            Title of the voice note
        
        voice_note_url (:class:`str`)
            The URL of the voice note file
        
        voice_note_duration (:class:`int`)
            Duration of the voice note, in seconds
        
        reply_markup (:class:`ReplyMarkup`)
            The message reply markup. Must be of type replyMarkupInlineKeyboard or null
        
        input_message_content (:class:`InputMessageContent`)
            The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageVoiceNote, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
        
    """

    ID: str = Field("inputInlineQueryResultVoiceNote", alias="@type")
    id: str
    title: str
    voice_note_url: str
    voice_note_duration: int
    reply_markup: ReplyMarkup
    input_message_content: InputMessageContent

    @staticmethod
    def read(q: dict) -> InputInlineQueryResultVoiceNote:
        return InputInlineQueryResultVoiceNote.construct(**q)
