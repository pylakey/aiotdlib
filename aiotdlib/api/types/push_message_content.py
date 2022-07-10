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
from .photo import Photo
from .sticker import Sticker
from .video import Video
from .video_note import VideoNote
from .voice_note import VoiceNote
from ..base_object import BaseObject


class PushMessageContent(BaseObject):
    """
    Contains content of a push message notification
    
    """

    ID: str = Field("pushMessageContent", alias="@type")


class PushMessageContentAnimation(PushMessageContent):
    """
    An animation message (GIF-style).
    
    :param animation: Message content; may be null, defaults to None
    :type animation: :class:`Animation`, optional
    
    :param caption: Animation caption
    :type caption: :class:`str`
    
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`bool`
    
    """

    ID: str = Field("pushMessageContentAnimation", alias="@type")
    animation: typing.Optional[Animation] = None
    caption: str
    is_pinned: bool

    @staticmethod
    def read(q: dict) -> PushMessageContentAnimation:
        return PushMessageContentAnimation.construct(**q)


class PushMessageContentAudio(PushMessageContent):
    """
    An audio message
    
    :param audio: Message content; may be null, defaults to None
    :type audio: :class:`Audio`, optional
    
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`bool`
    
    """

    ID: str = Field("pushMessageContentAudio", alias="@type")
    audio: typing.Optional[Audio] = None
    is_pinned: bool

    @staticmethod
    def read(q: dict) -> PushMessageContentAudio:
        return PushMessageContentAudio.construct(**q)


class PushMessageContentBasicGroupChatCreate(PushMessageContent):
    """
    A newly created basic group
    
    """

    ID: str = Field("pushMessageContentBasicGroupChatCreate", alias="@type")

    @staticmethod
    def read(q: dict) -> PushMessageContentBasicGroupChatCreate:
        return PushMessageContentBasicGroupChatCreate.construct(**q)


class PushMessageContentChatAddMembers(PushMessageContent):
    """
    New chat members were invited to a group
    
    :param member_name: Name of the added member
    :type member_name: :class:`str`
    
    :param is_current_user: True, if the current user was added to the group
    :type is_current_user: :class:`bool`
    
    :param is_returned: True, if the user has returned to the group themselves
    :type is_returned: :class:`bool`
    
    """

    ID: str = Field("pushMessageContentChatAddMembers", alias="@type")
    member_name: str
    is_current_user: bool
    is_returned: bool

    @staticmethod
    def read(q: dict) -> PushMessageContentChatAddMembers:
        return PushMessageContentChatAddMembers.construct(**q)


class PushMessageContentChatChangePhoto(PushMessageContent):
    """
    A chat photo was edited
    
    """

    ID: str = Field("pushMessageContentChatChangePhoto", alias="@type")

    @staticmethod
    def read(q: dict) -> PushMessageContentChatChangePhoto:
        return PushMessageContentChatChangePhoto.construct(**q)


class PushMessageContentChatChangeTitle(PushMessageContent):
    """
    A chat title was edited
    
    :param title: New chat title
    :type title: :class:`str`
    
    """

    ID: str = Field("pushMessageContentChatChangeTitle", alias="@type")
    title: str

    @staticmethod
    def read(q: dict) -> PushMessageContentChatChangeTitle:
        return PushMessageContentChatChangeTitle.construct(**q)


class PushMessageContentChatDeleteMember(PushMessageContent):
    """
    A chat member was deleted
    
    :param member_name: Name of the deleted member
    :type member_name: :class:`str`
    
    :param is_current_user: True, if the current user was deleted from the group
    :type is_current_user: :class:`bool`
    
    :param is_left: True, if the user has left the group themselves
    :type is_left: :class:`bool`
    
    """

    ID: str = Field("pushMessageContentChatDeleteMember", alias="@type")
    member_name: str
    is_current_user: bool
    is_left: bool

    @staticmethod
    def read(q: dict) -> PushMessageContentChatDeleteMember:
        return PushMessageContentChatDeleteMember.construct(**q)


class PushMessageContentChatJoinByLink(PushMessageContent):
    """
    A new member joined the chat via an invite link
    
    """

    ID: str = Field("pushMessageContentChatJoinByLink", alias="@type")

    @staticmethod
    def read(q: dict) -> PushMessageContentChatJoinByLink:
        return PushMessageContentChatJoinByLink.construct(**q)


class PushMessageContentChatJoinByRequest(PushMessageContent):
    """
    A new member was accepted to the chat by an administrator
    
    """

    ID: str = Field("pushMessageContentChatJoinByRequest", alias="@type")

    @staticmethod
    def read(q: dict) -> PushMessageContentChatJoinByRequest:
        return PushMessageContentChatJoinByRequest.construct(**q)


class PushMessageContentChatSetTheme(PushMessageContent):
    """
    A chat theme was edited
    
    :param theme_name: If non-empty, name of a new theme, set for the chat. Otherwise chat theme was reset to the default one
    :type theme_name: :class:`str`
    
    """

    ID: str = Field("pushMessageContentChatSetTheme", alias="@type")
    theme_name: str

    @staticmethod
    def read(q: dict) -> PushMessageContentChatSetTheme:
        return PushMessageContentChatSetTheme.construct(**q)


class PushMessageContentContact(PushMessageContent):
    """
    A message with a user contact
    
    :param name: Contact's name
    :type name: :class:`str`
    
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`bool`
    
    """

    ID: str = Field("pushMessageContentContact", alias="@type")
    name: str
    is_pinned: bool

    @staticmethod
    def read(q: dict) -> PushMessageContentContact:
        return PushMessageContentContact.construct(**q)


class PushMessageContentContactRegistered(PushMessageContent):
    """
    A contact has registered with Telegram
    
    """

    ID: str = Field("pushMessageContentContactRegistered", alias="@type")

    @staticmethod
    def read(q: dict) -> PushMessageContentContactRegistered:
        return PushMessageContentContactRegistered.construct(**q)


class PushMessageContentDocument(PushMessageContent):
    """
    A document message (a general file)
    
    :param document: Message content; may be null, defaults to None
    :type document: :class:`Document`, optional
    
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`bool`
    
    """

    ID: str = Field("pushMessageContentDocument", alias="@type")
    document: typing.Optional[Document] = None
    is_pinned: bool

    @staticmethod
    def read(q: dict) -> PushMessageContentDocument:
        return PushMessageContentDocument.construct(**q)


class PushMessageContentGame(PushMessageContent):
    """
    A message with a game
    
    :param title: Game title, empty for pinned game message
    :type title: :class:`str`
    
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`bool`
    
    """

    ID: str = Field("pushMessageContentGame", alias="@type")
    title: str
    is_pinned: bool

    @staticmethod
    def read(q: dict) -> PushMessageContentGame:
        return PushMessageContentGame.construct(**q)


class PushMessageContentGameScore(PushMessageContent):
    """
    A new high score was achieved in a game
    
    :param title: Game title, empty for pinned message
    :type title: :class:`str`
    
    :param score: New score, 0 for pinned message
    :type score: :class:`int`
    
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`bool`
    
    """

    ID: str = Field("pushMessageContentGameScore", alias="@type")
    title: str
    score: int
    is_pinned: bool

    @staticmethod
    def read(q: dict) -> PushMessageContentGameScore:
        return PushMessageContentGameScore.construct(**q)


class PushMessageContentHidden(PushMessageContent):
    """
    A general message with hidden content
    
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`bool`
    
    """

    ID: str = Field("pushMessageContentHidden", alias="@type")
    is_pinned: bool

    @staticmethod
    def read(q: dict) -> PushMessageContentHidden:
        return PushMessageContentHidden.construct(**q)


class PushMessageContentInvoice(PushMessageContent):
    """
    A message with an invoice from a bot
    
    :param price: Product price
    :type price: :class:`str`
    
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`bool`
    
    """

    ID: str = Field("pushMessageContentInvoice", alias="@type")
    price: str
    is_pinned: bool

    @staticmethod
    def read(q: dict) -> PushMessageContentInvoice:
        return PushMessageContentInvoice.construct(**q)


class PushMessageContentLocation(PushMessageContent):
    """
    A message with a location
    
    :param is_live: True, if the location is live
    :type is_live: :class:`bool`
    
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`bool`
    
    """

    ID: str = Field("pushMessageContentLocation", alias="@type")
    is_live: bool
    is_pinned: bool

    @staticmethod
    def read(q: dict) -> PushMessageContentLocation:
        return PushMessageContentLocation.construct(**q)


class PushMessageContentMediaAlbum(PushMessageContent):
    """
    A media album
    
    :param total_count: Number of messages in the album
    :type total_count: :class:`int`
    
    :param has_photos: True, if the album has at least one photo
    :type has_photos: :class:`bool`
    
    :param has_videos: True, if the album has at least one video
    :type has_videos: :class:`bool`
    
    :param has_audios: True, if the album has at least one audio file
    :type has_audios: :class:`bool`
    
    :param has_documents: True, if the album has at least one document
    :type has_documents: :class:`bool`
    
    """

    ID: str = Field("pushMessageContentMediaAlbum", alias="@type")
    total_count: int
    has_photos: bool
    has_videos: bool
    has_audios: bool
    has_documents: bool

    @staticmethod
    def read(q: dict) -> PushMessageContentMediaAlbum:
        return PushMessageContentMediaAlbum.construct(**q)


class PushMessageContentMessageForwards(PushMessageContent):
    """
    A forwarded messages
    
    :param total_count: Number of forwarded messages
    :type total_count: :class:`int`
    
    """

    ID: str = Field("pushMessageContentMessageForwards", alias="@type")
    total_count: int

    @staticmethod
    def read(q: dict) -> PushMessageContentMessageForwards:
        return PushMessageContentMessageForwards.construct(**q)


class PushMessageContentPhoto(PushMessageContent):
    """
    A photo message
    
    :param photo: Message content; may be null, defaults to None
    :type photo: :class:`Photo`, optional
    
    :param caption: Photo caption
    :type caption: :class:`str`
    
    :param is_secret: True, if the photo is secret
    :type is_secret: :class:`bool`
    
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`bool`
    
    """

    ID: str = Field("pushMessageContentPhoto", alias="@type")
    photo: typing.Optional[Photo] = None
    caption: str
    is_secret: bool
    is_pinned: bool

    @staticmethod
    def read(q: dict) -> PushMessageContentPhoto:
        return PushMessageContentPhoto.construct(**q)


class PushMessageContentPoll(PushMessageContent):
    """
    A message with a poll
    
    :param question: Poll question
    :type question: :class:`str`
    
    :param is_regular: True, if the poll is regular and not in quiz mode
    :type is_regular: :class:`bool`
    
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`bool`
    
    """

    ID: str = Field("pushMessageContentPoll", alias="@type")
    question: str
    is_regular: bool
    is_pinned: bool

    @staticmethod
    def read(q: dict) -> PushMessageContentPoll:
        return PushMessageContentPoll.construct(**q)


class PushMessageContentRecurringPayment(PushMessageContent):
    """
    A new recurrent payment was made by the current user
    
    :param amount: The paid amount
    :type amount: :class:`str`
    
    """

    ID: str = Field("pushMessageContentRecurringPayment", alias="@type")
    amount: str

    @staticmethod
    def read(q: dict) -> PushMessageContentRecurringPayment:
        return PushMessageContentRecurringPayment.construct(**q)


class PushMessageContentScreenshotTaken(PushMessageContent):
    """
    A screenshot of a message in the chat has been taken
    
    """

    ID: str = Field("pushMessageContentScreenshotTaken", alias="@type")

    @staticmethod
    def read(q: dict) -> PushMessageContentScreenshotTaken:
        return PushMessageContentScreenshotTaken.construct(**q)


class PushMessageContentSticker(PushMessageContent):
    """
    A message with a sticker
    
    :param sticker: Message content; may be null, defaults to None
    :type sticker: :class:`Sticker`, optional
    
    :param emoji: Emoji corresponding to the sticker; may be empty
    :type emoji: :class:`str`
    
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`bool`
    
    """

    ID: str = Field("pushMessageContentSticker", alias="@type")
    sticker: typing.Optional[Sticker] = None
    emoji: str
    is_pinned: bool

    @staticmethod
    def read(q: dict) -> PushMessageContentSticker:
        return PushMessageContentSticker.construct(**q)


class PushMessageContentText(PushMessageContent):
    """
    A text message
    
    :param text: Message text
    :type text: :class:`str`
    
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`bool`
    
    """

    ID: str = Field("pushMessageContentText", alias="@type")
    text: str
    is_pinned: bool

    @staticmethod
    def read(q: dict) -> PushMessageContentText:
        return PushMessageContentText.construct(**q)


class PushMessageContentVideo(PushMessageContent):
    """
    A video message
    
    :param video: Message content; may be null, defaults to None
    :type video: :class:`Video`, optional
    
    :param caption: Video caption
    :type caption: :class:`str`
    
    :param is_secret: True, if the video is secret
    :type is_secret: :class:`bool`
    
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`bool`
    
    """

    ID: str = Field("pushMessageContentVideo", alias="@type")
    video: typing.Optional[Video] = None
    caption: str
    is_secret: bool
    is_pinned: bool

    @staticmethod
    def read(q: dict) -> PushMessageContentVideo:
        return PushMessageContentVideo.construct(**q)


class PushMessageContentVideoNote(PushMessageContent):
    """
    A video note message
    
    :param video_note: Message content; may be null, defaults to None
    :type video_note: :class:`VideoNote`, optional
    
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`bool`
    
    """

    ID: str = Field("pushMessageContentVideoNote", alias="@type")
    video_note: typing.Optional[VideoNote] = None
    is_pinned: bool

    @staticmethod
    def read(q: dict) -> PushMessageContentVideoNote:
        return PushMessageContentVideoNote.construct(**q)


class PushMessageContentVoiceNote(PushMessageContent):
    """
    A voice note message
    
    :param voice_note: Message content; may be null, defaults to None
    :type voice_note: :class:`VoiceNote`, optional
    
    :param is_pinned: True, if the message is a pinned message with the specified content
    :type is_pinned: :class:`bool`
    
    """

    ID: str = Field("pushMessageContentVoiceNote", alias="@type")
    voice_note: typing.Optional[VoiceNote] = None
    is_pinned: bool

    @staticmethod
    def read(q: dict) -> PushMessageContentVoiceNote:
        return PushMessageContentVoiceNote.construct(**q)
