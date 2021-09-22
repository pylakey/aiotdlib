# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

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
    Represents a link to an animated GIF or an animated (i.e., without sound) H.264/MPEG-4 AVC video
    
    :param id: Unique identifier of the query result
    :type id: :class:`str`
    
    :param title: Title of the query result
    :type title: :class:`str`
    
    :param thumbnail_url: URL of the result thumbnail (JPEG, GIF, or MPEG4), if it exists
    :type thumbnail_url: :class:`str`
    
    :param thumbnail_mime_type: MIME type of the video thumbnail. If non-empty, must be one of "image/jpeg", "image/gif" and "video/mp4"
    :type thumbnail_mime_type: :class:`str`
    
    :param video_url: The URL of the video file (file size must not exceed 1MB)
    :type video_url: :class:`str`
    
    :param video_mime_type: MIME type of the video file. Must be one of "image/gif" and "video/mp4"
    :type video_mime_type: :class:`str`
    
    :param video_duration: Duration of the video, in seconds
    :type video_duration: :class:`int`
    
    :param video_width: Width of the video
    :type video_width: :class:`int`
    
    :param video_height: Height of the video
    :type video_height: :class:`int`
    
    :param reply_markup: The message reply markup. Must be of type replyMarkupInlineKeyboard or null
    :type reply_markup: :class:`ReplyMarkup`
    
    :param input_message_content: The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageAnimation, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
    :type input_message_content: :class:`InputMessageContent`
    
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
    
    :param thumbnail_url: URL of the result thumbnail, if it exists
    :type thumbnail_url: :class:`str`
    
    :param thumbnail_width: Thumbnail width, if known
    :type thumbnail_width: :class:`int`
    
    :param thumbnail_height: Thumbnail height, if known
    :type thumbnail_height: :class:`int`
    
    :param reply_markup: The message reply markup. Must be of type replyMarkupInlineKeyboard or null
    :type reply_markup: :class:`ReplyMarkup`
    
    :param input_message_content: The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
    :type input_message_content: :class:`InputMessageContent`
    
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
    
    :param id: Unique identifier of the query result
    :type id: :class:`str`
    
    :param title: Title of the audio file
    :type title: :class:`str`
    
    :param performer: Performer of the audio file
    :type performer: :class:`str`
    
    :param audio_url: The URL of the audio file
    :type audio_url: :class:`str`
    
    :param audio_duration: Audio file duration, in seconds
    :type audio_duration: :class:`int`
    
    :param reply_markup: The message reply markup. Must be of type replyMarkupInlineKeyboard or null
    :type reply_markup: :class:`ReplyMarkup`
    
    :param input_message_content: The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageAudio, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
    :type input_message_content: :class:`InputMessageContent`
    
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
    
    :param id: Unique identifier of the query result
    :type id: :class:`str`
    
    :param contact: User contact
    :type contact: :class:`Contact`
    
    :param thumbnail_url: URL of the result thumbnail, if it exists
    :type thumbnail_url: :class:`str`
    
    :param thumbnail_width: Thumbnail width, if known
    :type thumbnail_width: :class:`int`
    
    :param thumbnail_height: Thumbnail height, if known
    :type thumbnail_height: :class:`int`
    
    :param reply_markup: The message reply markup. Must be of type replyMarkupInlineKeyboard or null
    :type reply_markup: :class:`ReplyMarkup`
    
    :param input_message_content: The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
    :type input_message_content: :class:`InputMessageContent`
    
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
    
    :param id: Unique identifier of the query result
    :type id: :class:`str`
    
    :param title: Title of the resulting file
    :type title: :class:`str`
    
    :param param_description: Short description of the result, if known
    :type param_description: :class:`str`
    
    :param document_url: URL of the file
    :type document_url: :class:`str`
    
    :param mime_type: MIME type of the file content; only "application/pdf" and "application/zip" are currently allowed
    :type mime_type: :class:`str`
    
    :param thumbnail_url: The URL of the file thumbnail, if it exists
    :type thumbnail_url: :class:`str`
    
    :param thumbnail_width: Width of the thumbnail
    :type thumbnail_width: :class:`int`
    
    :param thumbnail_height: Height of the thumbnail
    :type thumbnail_height: :class:`int`
    
    :param reply_markup: The message reply markup. Must be of type replyMarkupInlineKeyboard or null
    :type reply_markup: :class:`ReplyMarkup`
    
    :param input_message_content: The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageDocument, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
    :type input_message_content: :class:`InputMessageContent`
    
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
    
    :param id: Unique identifier of the query result
    :type id: :class:`str`
    
    :param game_short_name: Short name of the game
    :type game_short_name: :class:`str`
    
    :param reply_markup: Message reply markup. Must be of type replyMarkupInlineKeyboard or null
    :type reply_markup: :class:`ReplyMarkup`
    
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
    
    :param id: Unique identifier of the query result
    :type id: :class:`str`
    
    :param location: Location result
    :type location: :class:`Location`
    
    :param live_period: Amount of time relative to the message sent time until the location can be updated, in seconds
    :type live_period: :class:`int`
    
    :param title: Title of the result
    :type title: :class:`str`
    
    :param thumbnail_url: URL of the result thumbnail, if it exists
    :type thumbnail_url: :class:`str`
    
    :param thumbnail_width: Thumbnail width, if known
    :type thumbnail_width: :class:`int`
    
    :param thumbnail_height: Thumbnail height, if known
    :type thumbnail_height: :class:`int`
    
    :param reply_markup: The message reply markup. Must be of type replyMarkupInlineKeyboard or null
    :type reply_markup: :class:`ReplyMarkup`
    
    :param input_message_content: The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
    :type input_message_content: :class:`InputMessageContent`
    
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
    
    :param id: Unique identifier of the query result
    :type id: :class:`str`
    
    :param title: Title of the result, if known
    :type title: :class:`str`
    
    :param param_description: A short description of the result, if known
    :type param_description: :class:`str`
    
    :param thumbnail_url: URL of the photo thumbnail, if it exists
    :type thumbnail_url: :class:`str`
    
    :param photo_url: The URL of the JPEG photo (photo size must not exceed 5MB)
    :type photo_url: :class:`str`
    
    :param photo_width: Width of the photo
    :type photo_width: :class:`int`
    
    :param photo_height: Height of the photo
    :type photo_height: :class:`int`
    
    :param reply_markup: The message reply markup. Must be of type replyMarkupInlineKeyboard or null
    :type reply_markup: :class:`ReplyMarkup`
    
    :param input_message_content: The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessagePhoto, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
    :type input_message_content: :class:`InputMessageContent`
    
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
    
    :param id: Unique identifier of the query result
    :type id: :class:`str`
    
    :param thumbnail_url: URL of the sticker thumbnail, if it exists
    :type thumbnail_url: :class:`str`
    
    :param sticker_url: The URL of the WEBP or TGS sticker (sticker file size must not exceed 5MB)
    :type sticker_url: :class:`str`
    
    :param sticker_width: Width of the sticker
    :type sticker_width: :class:`int`
    
    :param sticker_height: Height of the sticker
    :type sticker_height: :class:`int`
    
    :param reply_markup: The message reply markup. Must be of type replyMarkupInlineKeyboard or null
    :type reply_markup: :class:`ReplyMarkup`
    
    :param input_message_content: The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageSticker, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
    :type input_message_content: :class:`InputMessageContent`
    
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
    
    :param id: Unique identifier of the query result
    :type id: :class:`str`
    
    :param venue: Venue result
    :type venue: :class:`Venue`
    
    :param thumbnail_url: URL of the result thumbnail, if it exists
    :type thumbnail_url: :class:`str`
    
    :param thumbnail_width: Thumbnail width, if known
    :type thumbnail_width: :class:`int`
    
    :param thumbnail_height: Thumbnail height, if known
    :type thumbnail_height: :class:`int`
    
    :param reply_markup: The message reply markup. Must be of type replyMarkupInlineKeyboard or null
    :type reply_markup: :class:`ReplyMarkup`
    
    :param input_message_content: The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
    :type input_message_content: :class:`InputMessageContent`
    
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
    
    :param id: Unique identifier of the query result
    :type id: :class:`str`
    
    :param title: Title of the result
    :type title: :class:`str`
    
    :param param_description: A short description of the result, if known
    :type param_description: :class:`str`
    
    :param thumbnail_url: The URL of the video thumbnail (JPEG), if it exists
    :type thumbnail_url: :class:`str`
    
    :param video_url: URL of the embedded video player or video file
    :type video_url: :class:`str`
    
    :param mime_type: MIME type of the content of the video URL, only "text/html" or "video/mp4" are currently supported
    :type mime_type: :class:`str`
    
    :param video_width: Width of the video
    :type video_width: :class:`int`
    
    :param video_height: Height of the video
    :type video_height: :class:`int`
    
    :param video_duration: Video duration, in seconds
    :type video_duration: :class:`int`
    
    :param reply_markup: The message reply markup. Must be of type replyMarkupInlineKeyboard or null
    :type reply_markup: :class:`ReplyMarkup`
    
    :param input_message_content: The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageVideo, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
    :type input_message_content: :class:`InputMessageContent`
    
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
    
    :param id: Unique identifier of the query result
    :type id: :class:`str`
    
    :param title: Title of the voice note
    :type title: :class:`str`
    
    :param voice_note_url: The URL of the voice note file
    :type voice_note_url: :class:`str`
    
    :param voice_note_duration: Duration of the voice note, in seconds
    :type voice_note_duration: :class:`int`
    
    :param reply_markup: The message reply markup. Must be of type replyMarkupInlineKeyboard or null
    :type reply_markup: :class:`ReplyMarkup`
    
    :param input_message_content: The content of the message to be sent. Must be one of the following types: inputMessageText, inputMessageVoiceNote, inputMessageInvoice, inputMessageLocation, inputMessageVenue or inputMessageContact
    :type input_message_content: :class:`InputMessageContent`
    
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
