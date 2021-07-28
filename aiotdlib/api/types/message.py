# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .message_content import MessageContent
from .message_forward_info import MessageForwardInfo
from .message_interaction_info import MessageInteractionInfo
from .message_scheduling_state import MessageSchedulingState
from .message_sender import MessageSender
from .message_sending_state import MessageSendingState
from .reply_markup import ReplyMarkup
from ..base_object import BaseObject


class Message(BaseObject):
    """
    Describes a message
    
    Params:
        id (:class:`int`)
            Message identifier; unique for the chat to which the message belongs
        
        sender (:class:`MessageSender`)
            The sender of the message
        
        chat_id (:class:`int`)
            Chat identifier
        
        sending_state (:class:`MessageSendingState`)
            Information about the sending state of the message; may be null
        
        scheduling_state (:class:`MessageSchedulingState`)
            Information about the scheduling state of the message; may be null
        
        is_outgoing (:class:`bool`)
            True, if the message is outgoing
        
        is_pinned (:class:`bool`)
            True, if the message is pinned
        
        can_be_edited (:class:`bool`)
            True, if the message can be edited. For live location and poll messages this fields shows whether editMessageLiveLocation or stopPoll can be used with this message by the application
        
        can_be_forwarded (:class:`bool`)
            True, if the message can be forwarded
        
        can_be_deleted_only_for_self (:class:`bool`)
            True, if the message can be deleted only for the current user while other users will continue to see it
        
        can_be_deleted_for_all_users (:class:`bool`)
            True, if the message can be deleted for all users
        
        can_get_statistics (:class:`bool`)
            True, if the message statistics are available
        
        can_get_message_thread (:class:`bool`)
            True, if the message thread info is available
        
        is_channel_post (:class:`bool`)
            True, if the message is a channel post. All messages to channels are channel posts, all other messages are not channel posts
        
        contains_unread_mention (:class:`bool`)
            True, if the message contains an unread mention for the current user
        
        date (:class:`int`)
            Point in time (Unix timestamp) when the message was sent
        
        edit_date (:class:`int`)
            Point in time (Unix timestamp) when the message was last edited
        
        forward_info (:class:`MessageForwardInfo`)
            Information about the initial message sender; may be null
        
        interaction_info (:class:`MessageInteractionInfo`)
            Information about interactions with the message; may be null
        
        reply_in_chat_id (:class:`int`)
            If non-zero, the identifier of the chat to which the replied message belongs; Currently, only messages in the Replies chat can have different reply_in_chat_id and chat_id
        
        reply_to_message_id (:class:`int`)
            If non-zero, the identifier of the message this message is replying to; can be the identifier of a deleted message
        
        message_thread_id (:class:`int`)
            If non-zero, the identifier of the message thread the message belongs to; unique within the chat to which the message belongs
        
        ttl (:class:`int`)
            For self-destructing messages, the message's TTL (Time To Live), in seconds; 0 if none. TDLib will send updateDeleteMessages or updateMessageContent once the TTL expires
        
        ttl_expires_in (:class:`float`)
            Time left before the message expires, in seconds. If the TTL timer isn't started yet, equals to the value of the ttl field
        
        via_bot_user_id (:class:`int`)
            If non-zero, the user identifier of the bot through which this message was sent
        
        author_signature (:class:`str`)
            For channel posts and anonymous group messages, optional author signature
        
        media_album_id (:class:`int`)
            Unique identifier of an album this message belongs to. Only audios, documents, photos and videos can be grouped together in albums
        
        restriction_reason (:class:`str`)
            If non-empty, contains a human-readable description of the reason why access to this message must be restricted
        
        content (:class:`MessageContent`)
            Content of the message
        
        reply_markup (:class:`ReplyMarkup`)
            Reply markup for the message; may be null
        
    """

    ID: str = Field("message", alias="@type")
    id: int
    sender: MessageSender
    chat_id: int
    sending_state: typing.Optional[MessageSendingState] = None
    scheduling_state: typing.Optional[MessageSchedulingState] = None
    is_outgoing: bool
    is_pinned: bool
    can_be_edited: bool
    can_be_forwarded: bool
    can_be_deleted_only_for_self: bool
    can_be_deleted_for_all_users: bool
    can_get_statistics: bool
    can_get_message_thread: bool
    is_channel_post: bool
    contains_unread_mention: bool
    date: int
    edit_date: int
    forward_info: typing.Optional[MessageForwardInfo] = None
    interaction_info: typing.Optional[MessageInteractionInfo] = None
    reply_in_chat_id: int
    reply_to_message_id: int
    message_thread_id: int
    ttl: int
    ttl_expires_in: float
    via_bot_user_id: int
    author_signature: str
    media_album_id: int
    restriction_reason: str
    content: MessageContent
    reply_markup: typing.Optional[ReplyMarkup] = None

    @staticmethod
    def read(q: dict) -> Message:
        return Message.construct(**q)
