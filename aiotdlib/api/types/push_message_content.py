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
    
    Params:
        animation (:class:`Animation`)
            Message content; may be null
        
        caption (:class:`str`)
            Animation caption
        
        is_pinned (:class:`bool`)
            True, if the message is a pinned message with the specified content
        
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
    
    Params:
        audio (:class:`Audio`)
            Message content; may be null
        
        is_pinned (:class:`bool`)
            True, if the message is a pinned message with the specified content
        
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
    
    Params:
        member_name (:class:`str`)
            Name of the added member
        
        is_current_user (:class:`bool`)
            True, if the current user was added to the group
        
        is_returned (:class:`bool`)
            True, if the user has returned to the group themselves
        
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
    
    Params:
        title (:class:`str`)
            New chat title
        
    """

    ID: str = Field("pushMessageContentChatChangeTitle", alias="@type")
    title: str

    @staticmethod
    def read(q: dict) -> PushMessageContentChatChangeTitle:
        return PushMessageContentChatChangeTitle.construct(**q)


class PushMessageContentChatDeleteMember(PushMessageContent):
    """
    A chat member was deleted
    
    Params:
        member_name (:class:`str`)
            Name of the deleted member
        
        is_current_user (:class:`bool`)
            True, if the current user was deleted from the group
        
        is_left (:class:`bool`)
            True, if the user has left the group themselves
        
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
    A new member joined the chat by invite link
    
    """

    ID: str = Field("pushMessageContentChatJoinByLink", alias="@type")

    @staticmethod
    def read(q: dict) -> PushMessageContentChatJoinByLink:
        return PushMessageContentChatJoinByLink.construct(**q)


class PushMessageContentContact(PushMessageContent):
    """
    A message with a user contact
    
    Params:
        name (:class:`str`)
            Contact's name
        
        is_pinned (:class:`bool`)
            True, if the message is a pinned message with the specified content
        
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
    
    Params:
        document (:class:`Document`)
            Message content; may be null
        
        is_pinned (:class:`bool`)
            True, if the message is a pinned message with the specified content
        
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
    
    Params:
        title (:class:`str`)
            Game title, empty for pinned game message
        
        is_pinned (:class:`bool`)
            True, if the message is a pinned message with the specified content
        
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
    
    Params:
        title (:class:`str`)
            Game title, empty for pinned message
        
        score (:class:`int`)
            New score, 0 for pinned message
        
        is_pinned (:class:`bool`)
            True, if the message is a pinned message with the specified content
        
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
    
    Params:
        is_pinned (:class:`bool`)
            True, if the message is a pinned message with the specified content
        
    """

    ID: str = Field("pushMessageContentHidden", alias="@type")
    is_pinned: bool

    @staticmethod
    def read(q: dict) -> PushMessageContentHidden:
        return PushMessageContentHidden.construct(**q)


class PushMessageContentInvoice(PushMessageContent):
    """
    A message with an invoice from a bot
    
    Params:
        price (:class:`str`)
            Product price
        
        is_pinned (:class:`bool`)
            True, if the message is a pinned message with the specified content
        
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
    
    Params:
        is_live (:class:`bool`)
            True, if the location is live
        
        is_pinned (:class:`bool`)
            True, if the message is a pinned message with the specified content
        
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
    
    Params:
        total_count (:class:`int`)
            Number of messages in the album
        
        has_photos (:class:`bool`)
            True, if the album has at least one photo
        
        has_videos (:class:`bool`)
            True, if the album has at least one video
        
        has_audios (:class:`bool`)
            True, if the album has at least one audio file
        
        has_documents (:class:`bool`)
            True, if the album has at least one document
        
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
    
    Params:
        total_count (:class:`int`)
            Number of forwarded messages
        
    """

    ID: str = Field("pushMessageContentMessageForwards", alias="@type")
    total_count: int

    @staticmethod
    def read(q: dict) -> PushMessageContentMessageForwards:
        return PushMessageContentMessageForwards.construct(**q)


class PushMessageContentPhoto(PushMessageContent):
    """
    A photo message
    
    Params:
        photo (:class:`Photo`)
            Message content; may be null
        
        caption (:class:`str`)
            Photo caption
        
        is_secret (:class:`bool`)
            True, if the photo is secret
        
        is_pinned (:class:`bool`)
            True, if the message is a pinned message with the specified content
        
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
    
    Params:
        question (:class:`str`)
            Poll question
        
        is_regular (:class:`bool`)
            True, if the poll is regular and not in quiz mode
        
        is_pinned (:class:`bool`)
            True, if the message is a pinned message with the specified content
        
    """

    ID: str = Field("pushMessageContentPoll", alias="@type")
    question: str
    is_regular: bool
    is_pinned: bool

    @staticmethod
    def read(q: dict) -> PushMessageContentPoll:
        return PushMessageContentPoll.construct(**q)


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
    
    Params:
        sticker (:class:`Sticker`)
            Message content; may be null
        
        emoji (:class:`str`)
            Emoji corresponding to the sticker; may be empty
        
        is_pinned (:class:`bool`)
            True, if the message is a pinned message with the specified content
        
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
    
    Params:
        text (:class:`str`)
            Message text
        
        is_pinned (:class:`bool`)
            True, if the message is a pinned message with the specified content
        
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
    
    Params:
        video (:class:`Video`)
            Message content; may be null
        
        caption (:class:`str`)
            Video caption
        
        is_secret (:class:`bool`)
            True, if the video is secret
        
        is_pinned (:class:`bool`)
            True, if the message is a pinned message with the specified content
        
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
    
    Params:
        video_note (:class:`VideoNote`)
            Message content; may be null
        
        is_pinned (:class:`bool`)
            True, if the message is a pinned message with the specified content
        
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
    
    Params:
        voice_note (:class:`VoiceNote`)
            Message content; may be null
        
        is_pinned (:class:`bool`)
            True, if the message is a pinned message with the specified content
        
    """

    ID: str = Field("pushMessageContentVoiceNote", alias="@type")
    voice_note: typing.Optional[VoiceNote] = None
    is_pinned: bool

    @staticmethod
    def read(q: dict) -> PushMessageContentVoiceNote:
        return PushMessageContentVoiceNote.construct(**q)
