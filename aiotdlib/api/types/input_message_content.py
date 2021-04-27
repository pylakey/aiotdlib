# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .contact import Contact
from .formatted_text import FormattedText
from .input_file import InputFile
from .input_thumbnail import InputThumbnail
from .invoice import Invoice
from .location import Location
from .message_copy_options import MessageCopyOptions
from .poll_type import PollType
from .venue import Venue
from ..base_object import BaseObject


class InputMessageContent(BaseObject):
    """
    The content of a message to send
    
    """

    ID: str = Field("inputMessageContent", alias="@type")


class InputMessageAnimation(InputMessageContent):
    """
    An animation message (GIF-style).
    
    Params:
        animation (:class:`InputFile`)
            Animation file to be sent
        
        thumbnail (:class:`InputThumbnail`)
            Animation thumbnail, if available
        
        added_sticker_file_ids (:obj:`list[int]`)
            File identifiers of the stickers added to the animation, if applicable
        
        duration (:class:`int`)
            Duration of the animation, in seconds
        
        width (:class:`int`)
            Width of the animation; may be replaced by the server
        
        height (:class:`int`)
            Height of the animation; may be replaced by the server
        
        caption (:class:`FormattedText`)
            Animation caption; 0-GetOption("message_caption_length_max") characters
        
    """

    ID: str = Field("inputMessageAnimation", alias="@type")
    animation: InputFile
    thumbnail: InputThumbnail
    added_sticker_file_ids: list[int]
    duration: int
    width: int
    height: int
    caption: FormattedText

    @staticmethod
    def read(q: dict) -> InputMessageAnimation:
        return InputMessageAnimation.construct(**q)


class InputMessageAudio(InputMessageContent):
    """
    An audio message
    
    Params:
        audio (:class:`InputFile`)
            Audio file to be sent
        
        album_cover_thumbnail (:class:`InputThumbnail`)
            Thumbnail of the cover for the album, if available
        
        duration (:class:`int`)
            Duration of the audio, in seconds; may be replaced by the server
        
        title (:class:`str`)
            Title of the audio; 0-64 characters; may be replaced by the server
        
        performer (:class:`str`)
            Performer of the audio; 0-64 characters, may be replaced by the server
        
        caption (:class:`FormattedText`)
            Audio caption; 0-GetOption("message_caption_length_max") characters
        
    """

    ID: str = Field("inputMessageAudio", alias="@type")
    audio: InputFile
    album_cover_thumbnail: InputThumbnail
    duration: int
    title: typing.Optional[str] = Field(None, max_length=64)
    performer: typing.Optional[str] = Field(None, max_length=64)
    caption: FormattedText

    @staticmethod
    def read(q: dict) -> InputMessageAudio:
        return InputMessageAudio.construct(**q)


class InputMessageContact(InputMessageContent):
    """
    A message containing a user contact
    
    Params:
        contact (:class:`Contact`)
            Contact to send
        
    """

    ID: str = Field("inputMessageContact", alias="@type")
    contact: Contact

    @staticmethod
    def read(q: dict) -> InputMessageContact:
        return InputMessageContact.construct(**q)


class InputMessageDice(InputMessageContent):
    """
    A dice message
    
    Params:
        emoji (:class:`str`)
            Emoji on which the dice throw animation is based
        
        clear_draft (:class:`bool`)
            True, if a chat message draft should be deleted
        
    """

    ID: str = Field("inputMessageDice", alias="@type")
    emoji: str
    clear_draft: bool

    @staticmethod
    def read(q: dict) -> InputMessageDice:
        return InputMessageDice.construct(**q)


class InputMessageDocument(InputMessageContent):
    """
    A document message (general file)
    
    Params:
        document (:class:`InputFile`)
            Document to be sent
        
        thumbnail (:class:`InputThumbnail`)
            Document thumbnail, if available
        
        disable_content_type_detection (:class:`bool`)
            If true, automatic file type detection will be disabled and the document will be always sent as file. Always true for files sent to secret chats
        
        caption (:class:`FormattedText`)
            Document caption; 0-GetOption("message_caption_length_max") characters
        
    """

    ID: str = Field("inputMessageDocument", alias="@type")
    document: InputFile
    thumbnail: InputThumbnail
    disable_content_type_detection: bool
    caption: FormattedText

    @staticmethod
    def read(q: dict) -> InputMessageDocument:
        return InputMessageDocument.construct(**q)


class InputMessageForwarded(InputMessageContent):
    """
    A forwarded message
    
    Params:
        from_chat_id (:class:`int`)
            Identifier for the chat this forwarded message came from
        
        message_id (:class:`int`)
            Identifier of the message to forward
        
        in_game_share (:class:`bool`)
            True, if a game message should be shared within a launched game; applies only to game messages
        
        copy_options (:class:`MessageCopyOptions`)
            Options to be used to copy content of the message without a link to the original message
        
    """

    ID: str = Field("inputMessageForwarded", alias="@type")
    from_chat_id: int
    message_id: int
    in_game_share: bool
    copy_options: MessageCopyOptions

    @staticmethod
    def read(q: dict) -> InputMessageForwarded:
        return InputMessageForwarded.construct(**q)


class InputMessageGame(InputMessageContent):
    """
    A message with a game; not supported for channels or secret chats
    
    Params:
        bot_user_id (:class:`int`)
            User identifier of the bot that owns the game
        
        game_short_name (:class:`str`)
            Short name of the game
        
    """

    ID: str = Field("inputMessageGame", alias="@type")
    bot_user_id: int
    game_short_name: str

    @staticmethod
    def read(q: dict) -> InputMessageGame:
        return InputMessageGame.construct(**q)


class InputMessageInvoice(InputMessageContent):
    """
    A message with an invoice; can be used only by bots
    
    Params:
        invoice (:class:`Invoice`)
            Invoice
        
        title (:class:`str`)
            Product title; 1-32 characters
        
        param_description (:class:`str`)
            Product description; 0-255 characters
        
        photo_url (:class:`str`)
            Product photo URL; optional
        
        photo_size (:class:`int`)
            Product photo size
        
        photo_width (:class:`int`)
            Product photo width
        
        photo_height (:class:`int`)
            Product photo height
        
        payload (:class:`str`)
            The invoice payload
        
        provider_token (:class:`str`)
            Payment provider token
        
        provider_data (:class:`str`)
            JSON-encoded data about the invoice, which will be shared with the payment provider
        
        start_parameter (:class:`str`)
            Unique invoice bot deep link parameter for the generation of this invoice. If empty, it would be possible to pay directly from forwards of the invoice message
        
    """

    ID: str = Field("inputMessageInvoice", alias="@type")
    invoice: Invoice
    title: str = Field(..., min_length=1, max_length=32)
    param_description: typing.Optional[str] = Field(None, max_length=255)
    photo_url: str
    photo_size: int
    photo_width: int
    photo_height: int
    payload: str
    provider_token: str
    provider_data: str
    start_parameter: str

    @staticmethod
    def read(q: dict) -> InputMessageInvoice:
        return InputMessageInvoice.construct(**q)


class InputMessageLocation(InputMessageContent):
    """
    A message with a location
    
    Params:
        location (:class:`Location`)
            Location to be sent
        
        live_period (:class:`int`)
            Period for which the location can be updated, in seconds; should be between 60 and 86400 for a live location and 0 otherwise
        
        heading (:class:`int`)
            For live locations, a direction in which the location moves, in degrees; 1-360. Pass 0 if unknown
        
        proximity_alert_radius (:class:`int`)
            For live locations, a maximum distance to another chat member for proximity alerts, in meters (0-100000). Pass 0 if the notification is disabled. Can't be enabled in channels and Saved Messages
        
    """

    ID: str = Field("inputMessageLocation", alias="@type")
    location: Location
    live_period: int
    heading: int
    proximity_alert_radius: int

    @staticmethod
    def read(q: dict) -> InputMessageLocation:
        return InputMessageLocation.construct(**q)


class InputMessagePhoto(InputMessageContent):
    """
    A photo message
    
    Params:
        photo (:class:`InputFile`)
            Photo to send
        
        thumbnail (:class:`InputThumbnail`)
            Photo thumbnail to be sent, this is sent to the other party in secret chats only
        
        added_sticker_file_ids (:obj:`list[int]`)
            File identifiers of the stickers added to the photo, if applicable
        
        width (:class:`int`)
            Photo width
        
        height (:class:`int`)
            Photo height
        
        caption (:class:`FormattedText`)
            Photo caption; 0-GetOption("message_caption_length_max") characters
        
        ttl (:class:`int`)
            Photo TTL (Time To Live), in seconds (0-60). A non-zero TTL can be specified only in private chats
        
    """

    ID: str = Field("inputMessagePhoto", alias="@type")
    photo: InputFile
    thumbnail: InputThumbnail
    added_sticker_file_ids: list[int]
    width: int
    height: int
    caption: FormattedText
    ttl: int

    @staticmethod
    def read(q: dict) -> InputMessagePhoto:
        return InputMessagePhoto.construct(**q)


class InputMessagePoll(InputMessageContent):
    """
    A message with a poll. Polls can't be sent to secret chats. Polls can be sent only to a private chat with a bot
    
    Params:
        question (:class:`str`)
            Poll question; 1-255 characters (up to 300 characters for bots)
        
        options (:obj:`list[str]`)
            List of poll answer options, 2-10 strings 1-100 characters each
        
        is_anonymous (:class:`bool`)
            True, if the poll voters are anonymous. Non-anonymous polls can't be sent or forwarded to channels
        
        type_ (:class:`PollType`)
            Type of the poll
        
        open_period (:class:`int`)
            Amount of time the poll will be active after creation, in seconds; for bots only
        
        close_date (:class:`int`)
            Point in time (Unix timestamp) when the poll will be automatically closed; for bots only
        
        is_closed (:class:`bool`)
            True, if the poll needs to be sent already closed; for bots only
        
    """

    ID: str = Field("inputMessagePoll", alias="@type")
    question: str = Field(..., min_length=1, max_length=255)
    options: list[str]
    is_anonymous: bool
    type_: PollType = Field(..., alias='type')
    open_period: int
    close_date: int
    is_closed: bool

    @staticmethod
    def read(q: dict) -> InputMessagePoll:
        return InputMessagePoll.construct(**q)


class InputMessageSticker(InputMessageContent):
    """
    A sticker message
    
    Params:
        sticker (:class:`InputFile`)
            Sticker to be sent
        
        thumbnail (:class:`InputThumbnail`)
            Sticker thumbnail, if available
        
        width (:class:`int`)
            Sticker width
        
        height (:class:`int`)
            Sticker height
        
        emoji (:class:`str`)
            Emoji used to choose the sticker
        
    """

    ID: str = Field("inputMessageSticker", alias="@type")
    sticker: InputFile
    thumbnail: InputThumbnail
    width: int
    height: int
    emoji: str

    @staticmethod
    def read(q: dict) -> InputMessageSticker:
        return InputMessageSticker.construct(**q)


class InputMessageText(InputMessageContent):
    """
    A text message
    
    Params:
        text (:class:`FormattedText`)
            Formatted text to be sent; 1-GetOption("message_text_length_max") characters. Only Bold, Italic, Underline, Strikethrough, Code, Pre, PreCode, TextUrl and MentionName entities are allowed to be specified manually
        
        disable_web_page_preview (:class:`bool`)
            True, if rich web page previews for URLs in the message text should be disabled
        
        clear_draft (:class:`bool`)
            True, if a chat message draft should be deleted
        
    """

    ID: str = Field("inputMessageText", alias="@type")
    text: FormattedText
    disable_web_page_preview: bool
    clear_draft: bool

    @staticmethod
    def read(q: dict) -> InputMessageText:
        return InputMessageText.construct(**q)


class InputMessageVenue(InputMessageContent):
    """
    A message with information about a venue
    
    Params:
        venue (:class:`Venue`)
            Venue to send
        
    """

    ID: str = Field("inputMessageVenue", alias="@type")
    venue: Venue

    @staticmethod
    def read(q: dict) -> InputMessageVenue:
        return InputMessageVenue.construct(**q)


class InputMessageVideo(InputMessageContent):
    """
    A video message
    
    Params:
        video (:class:`InputFile`)
            Video to be sent
        
        thumbnail (:class:`InputThumbnail`)
            Video thumbnail, if available
        
        added_sticker_file_ids (:obj:`list[int]`)
            File identifiers of the stickers added to the video, if applicable
        
        duration (:class:`int`)
            Duration of the video, in seconds
        
        width (:class:`int`)
            Video width
        
        height (:class:`int`)
            Video height
        
        supports_streaming (:class:`bool`)
            True, if the video should be tried to be streamed
        
        caption (:class:`FormattedText`)
            Video caption; 0-GetOption("message_caption_length_max") characters
        
        ttl (:class:`int`)
            Video TTL (Time To Live), in seconds (0-60). A non-zero TTL can be specified only in private chats
        
    """

    ID: str = Field("inputMessageVideo", alias="@type")
    video: InputFile
    thumbnail: InputThumbnail
    added_sticker_file_ids: list[int]
    duration: int
    width: int
    height: int
    supports_streaming: bool
    caption: FormattedText
    ttl: int

    @staticmethod
    def read(q: dict) -> InputMessageVideo:
        return InputMessageVideo.construct(**q)


class InputMessageVideoNote(InputMessageContent):
    """
    A video note message
    
    Params:
        video_note (:class:`InputFile`)
            Video note to be sent
        
        thumbnail (:class:`InputThumbnail`)
            Video thumbnail, if available
        
        duration (:class:`int`)
            Duration of the video, in seconds
        
        length (:class:`int`)
            Video width and height; must be positive and not greater than 640
        
    """

    ID: str = Field("inputMessageVideoNote", alias="@type")
    video_note: InputFile
    thumbnail: InputThumbnail
    duration: int
    length: int

    @staticmethod
    def read(q: dict) -> InputMessageVideoNote:
        return InputMessageVideoNote.construct(**q)


class InputMessageVoiceNote(InputMessageContent):
    """
    A voice note message
    
    Params:
        voice_note (:class:`InputFile`)
            Voice note to be sent
        
        duration (:class:`int`)
            Duration of the voice note, in seconds
        
        waveform (:class:`str`)
            Waveform representation of the voice note, in 5-bit format
        
        caption (:class:`FormattedText`)
            Voice note caption; 0-GetOption("message_caption_length_max") characters
        
    """

    ID: str = Field("inputMessageVoiceNote", alias="@type")
    voice_note: InputFile
    duration: int
    waveform: str
    caption: FormattedText

    @staticmethod
    def read(q: dict) -> InputMessageVoiceNote:
        return InputMessageVoiceNote.construct(**q)
