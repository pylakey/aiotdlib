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
    
    :param animation: Animation file to be sent
    :type animation: :class:`InputFile`
    
    :param thumbnail: Animation thumbnail; pass null to skip thumbnail uploading
    :type thumbnail: :class:`InputThumbnail`
    
    :param added_sticker_file_ids: File identifiers of the stickers added to the animation, if applicable
    :type added_sticker_file_ids: :class:`list[int]`
    
    :param duration: Duration of the animation, in seconds
    :type duration: :class:`int`
    
    :param width: Width of the animation; may be replaced by the server
    :type width: :class:`int`
    
    :param height: Height of the animation; may be replaced by the server
    :type height: :class:`int`
    
    :param caption: Animation caption; pass null to use an empty caption; 0-GetOption("message_caption_length_max") characters
    :type caption: :class:`FormattedText`
    
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
    
    :param audio: Audio file to be sent
    :type audio: :class:`InputFile`
    
    :param album_cover_thumbnail: Thumbnail of the cover for the album; pass null to skip thumbnail uploading
    :type album_cover_thumbnail: :class:`InputThumbnail`
    
    :param duration: Duration of the audio, in seconds; may be replaced by the server
    :type duration: :class:`int`
    
    :param title: Title of the audio; 0-64 characters; may be replaced by the server, defaults to None
    :type title: :class:`str`, optional
    
    :param performer: Performer of the audio; 0-64 characters, may be replaced by the server, defaults to None
    :type performer: :class:`str`, optional
    
    :param caption: Audio caption; pass null to use an empty caption; 0-GetOption("message_caption_length_max") characters
    :type caption: :class:`FormattedText`
    
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
    
    :param contact: Contact to send
    :type contact: :class:`Contact`
    
    """

    ID: str = Field("inputMessageContact", alias="@type")
    contact: Contact

    @staticmethod
    def read(q: dict) -> InputMessageContact:
        return InputMessageContact.construct(**q)


class InputMessageDice(InputMessageContent):
    """
    A dice message
    
    :param emoji: Emoji on which the dice throw animation is based
    :type emoji: :class:`str`
    
    :param clear_draft: True, if the chat message draft must be deleted
    :type clear_draft: :class:`bool`
    
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
    
    :param document: Document to be sent
    :type document: :class:`InputFile`
    
    :param thumbnail: Document thumbnail; pass null to skip thumbnail uploading
    :type thumbnail: :class:`InputThumbnail`
    
    :param disable_content_type_detection: If true, automatic file type detection will be disabled and the document will be always sent as file. Always true for files sent to secret chats
    :type disable_content_type_detection: :class:`bool`
    
    :param caption: Document caption; pass null to use an empty caption; 0-GetOption("message_caption_length_max") characters
    :type caption: :class:`FormattedText`
    
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
    
    :param from_chat_id: Identifier for the chat this forwarded message came from
    :type from_chat_id: :class:`int`
    
    :param message_id: Identifier of the message to forward
    :type message_id: :class:`int`
    
    :param in_game_share: True, if a game message is being shared from a launched game; applies only to game messages
    :type in_game_share: :class:`bool`
    
    :param copy_options: Options to be used to copy content of the message without reference to the original sender; pass null to forward the message as usual
    :type copy_options: :class:`MessageCopyOptions`
    
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
    
    :param bot_user_id: User identifier of the bot that owns the game
    :type bot_user_id: :class:`int`
    
    :param game_short_name: Short name of the game
    :type game_short_name: :class:`str`
    
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
    
    :param invoice: Invoice
    :type invoice: :class:`Invoice`
    
    :param title: Product title; 1-32 characters
    :type title: :class:`str`
    
    :param param_description: Product description; 0-255 characters, defaults to None
    :type param_description: :class:`str`, optional
    
    :param photo_url: Product photo URL; optional
    :type photo_url: :class:`str`
    
    :param photo_size: Product photo size
    :type photo_size: :class:`int`
    
    :param photo_width: Product photo width
    :type photo_width: :class:`int`
    
    :param photo_height: Product photo height
    :type photo_height: :class:`int`
    
    :param payload: The invoice payload
    :type payload: :class:`str`
    
    :param provider_token: Payment provider token
    :type provider_token: :class:`str`
    
    :param provider_data: JSON-encoded data about the invoice, which will be shared with the payment provider
    :type provider_data: :class:`str`
    
    :param start_parameter: Unique invoice bot deep link parameter for the generation of this invoice. If empty, it would be possible to pay directly from forwards of the invoice message
    :type start_parameter: :class:`str`
    
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
    
    :param location: Location to be sent
    :type location: :class:`Location`
    
    :param live_period: Period for which the location can be updated, in seconds; must be between 60 and 86400 for a live location and 0 otherwise
    :type live_period: :class:`int`
    
    :param heading: For live locations, a direction in which the location moves, in degrees; 1-360. Pass 0 if unknown
    :type heading: :class:`int`
    
    :param proximity_alert_radius: For live locations, a maximum distance to another chat member for proximity alerts, in meters (0-100000). Pass 0 if the notification is disabled. Can't be enabled in channels and Saved Messages
    :type proximity_alert_radius: :class:`int`
    
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
    
    :param photo: Photo to send. The photo must be at most 10 MB in size. The photo's width and height must not exceed 10000 in total. Width and height ratio must be at most 20
    :type photo: :class:`InputFile`
    
    :param thumbnail: Photo thumbnail to be sent; pass null to skip thumbnail uploading. The thumbnail is sent to the other party only in secret chats
    :type thumbnail: :class:`InputThumbnail`
    
    :param added_sticker_file_ids: File identifiers of the stickers added to the photo, if applicable
    :type added_sticker_file_ids: :class:`list[int]`
    
    :param width: Photo width
    :type width: :class:`int`
    
    :param height: Photo height
    :type height: :class:`int`
    
    :param caption: Photo caption; pass null to use an empty caption; 0-GetOption("message_caption_length_max") characters
    :type caption: :class:`FormattedText`
    
    :param ttl: Photo TTL (Time To Live), in seconds (0-60). A non-zero TTL can be specified only in private chats
    :type ttl: :class:`int`
    
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
    
    :param question: Poll question; 1-255 characters (up to 300 characters for bots)
    :type question: :class:`str`
    
    :param options: List of poll answer options, 2-10 strings 1-100 characters each
    :type options: :class:`list[str]`
    
    :param is_anonymous: True, if the poll voters are anonymous. Non-anonymous polls can't be sent or forwarded to channels
    :type is_anonymous: :class:`bool`
    
    :param type_: Type of the poll
    :type type_: :class:`PollType`
    
    :param open_period: Amount of time the poll will be active after creation, in seconds; for bots only
    :type open_period: :class:`int`
    
    :param close_date: Point in time (Unix timestamp) when the poll will automatically be closed; for bots only
    :type close_date: :class:`int`
    
    :param is_closed: True, if the poll needs to be sent already closed; for bots only
    :type is_closed: :class:`bool`
    
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
    
    :param sticker: Sticker to be sent
    :type sticker: :class:`InputFile`
    
    :param thumbnail: Sticker thumbnail; pass null to skip thumbnail uploading
    :type thumbnail: :class:`InputThumbnail`
    
    :param width: Sticker width
    :type width: :class:`int`
    
    :param height: Sticker height
    :type height: :class:`int`
    
    :param emoji: Emoji used to choose the sticker
    :type emoji: :class:`str`
    
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
    
    :param text: Formatted text to be sent; 1-GetOption("message_text_length_max") characters. Only Bold, Italic, Underline, Strikethrough, Spoiler, Code, Pre, PreCode, TextUrl and MentionName entities are allowed to be specified manually
    :type text: :class:`FormattedText`
    
    :param disable_web_page_preview: True, if rich web page previews for URLs in the message text must be disabled
    :type disable_web_page_preview: :class:`bool`
    
    :param clear_draft: True, if a chat message draft must be deleted
    :type clear_draft: :class:`bool`
    
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
    
    :param venue: Venue to send
    :type venue: :class:`Venue`
    
    """

    ID: str = Field("inputMessageVenue", alias="@type")
    venue: Venue

    @staticmethod
    def read(q: dict) -> InputMessageVenue:
        return InputMessageVenue.construct(**q)


class InputMessageVideo(InputMessageContent):
    """
    A video message
    
    :param video: Video to be sent
    :type video: :class:`InputFile`
    
    :param thumbnail: Video thumbnail; pass null to skip thumbnail uploading
    :type thumbnail: :class:`InputThumbnail`
    
    :param added_sticker_file_ids: File identifiers of the stickers added to the video, if applicable
    :type added_sticker_file_ids: :class:`list[int]`
    
    :param duration: Duration of the video, in seconds
    :type duration: :class:`int`
    
    :param width: Video width
    :type width: :class:`int`
    
    :param height: Video height
    :type height: :class:`int`
    
    :param supports_streaming: True, if the video is supposed to be streamed
    :type supports_streaming: :class:`bool`
    
    :param caption: Video caption; pass null to use an empty caption; 0-GetOption("message_caption_length_max") characters
    :type caption: :class:`FormattedText`
    
    :param ttl: Video TTL (Time To Live), in seconds (0-60). A non-zero TTL can be specified only in private chats
    :type ttl: :class:`int`
    
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
    
    :param video_note: Video note to be sent
    :type video_note: :class:`InputFile`
    
    :param thumbnail: Video thumbnail; pass null to skip thumbnail uploading
    :type thumbnail: :class:`InputThumbnail`
    
    :param duration: Duration of the video, in seconds
    :type duration: :class:`int`
    
    :param length: Video width and height; must be positive and not greater than 640
    :type length: :class:`int`
    
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
    
    :param voice_note: Voice note to be sent
    :type voice_note: :class:`InputFile`
    
    :param duration: Duration of the voice note, in seconds
    :type duration: :class:`int`
    
    :param waveform: Waveform representation of the voice note, in 5-bit format
    :type waveform: :class:`str`
    
    :param caption: Voice note caption; pass null to use an empty caption; 0-GetOption("message_caption_length_max") characters
    :type caption: :class:`FormattedText`
    
    """

    ID: str = Field("inputMessageVoiceNote", alias="@type")
    voice_note: InputFile
    duration: int
    waveform: str
    caption: FormattedText

    @staticmethod
    def read(q: dict) -> InputMessageVoiceNote:
        return InputMessageVoiceNote.construct(**q)
