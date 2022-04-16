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
from .unread_reaction import UnreadReaction
from ..base_object import BaseObject


class Message(BaseObject):
    """
    Describes a message
    
    :param id: Message identifier; unique for the chat to which the message belongs
    :type id: :class:`int`
    
    :param sender_id: Identifier of the sender of the message
    :type sender_id: :class:`MessageSender`
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param sending_state: The sending state of the message; may be null, defaults to None
    :type sending_state: :class:`MessageSendingState`, optional
    
    :param scheduling_state: The scheduling state of the message; may be null, defaults to None
    :type scheduling_state: :class:`MessageSchedulingState`, optional
    
    :param is_outgoing: True, if the message is outgoing
    :type is_outgoing: :class:`bool`
    
    :param is_pinned: True, if the message is pinned
    :type is_pinned: :class:`bool`
    
    :param can_be_edited: True, if the message can be edited. For live location and poll messages this fields shows whether editMessageLiveLocation or stopPoll can be used with this message by the application
    :type can_be_edited: :class:`bool`
    
    :param can_be_forwarded: True, if the message can be forwarded
    :type can_be_forwarded: :class:`bool`
    
    :param can_be_saved: True, if content of the message can be saved locally or copied
    :type can_be_saved: :class:`bool`
    
    :param can_be_deleted_only_for_self: True, if the message can be deleted only for the current user while other users will continue to see it
    :type can_be_deleted_only_for_self: :class:`bool`
    
    :param can_be_deleted_for_all_users: True, if the message can be deleted for all users
    :type can_be_deleted_for_all_users: :class:`bool`
    
    :param can_get_added_reactions: True, if the list of added reactions is available through getMessageAddedReactions
    :type can_get_added_reactions: :class:`bool`
    
    :param can_get_statistics: True, if the message statistics are available through getMessageStatistics
    :type can_get_statistics: :class:`bool`
    
    :param can_get_message_thread: True, if information about the message thread is available through getMessageThread
    :type can_get_message_thread: :class:`bool`
    
    :param can_get_viewers: True, if chat members already viewed the message can be received through getMessageViewers
    :type can_get_viewers: :class:`bool`
    
    :param can_get_media_timestamp_links: True, if media timestamp links can be generated for media timestamp entities in the message text, caption or web page description through getMessageLink
    :type can_get_media_timestamp_links: :class:`bool`
    
    :param has_timestamped_media: True, if media timestamp entities refers to a media in this message as opposed to a media in the replied message
    :type has_timestamped_media: :class:`bool`
    
    :param is_channel_post: True, if the message is a channel post. All messages to channels are channel posts, all other messages are not channel posts
    :type is_channel_post: :class:`bool`
    
    :param contains_unread_mention: True, if the message contains an unread mention for the current user
    :type contains_unread_mention: :class:`bool`
    
    :param date: Point in time (Unix timestamp) when the message was sent
    :type date: :class:`int`
    
    :param edit_date: Point in time (Unix timestamp) when the message was last edited
    :type edit_date: :class:`int`
    
    :param forward_info: Information about the initial message sender; may be null, defaults to None
    :type forward_info: :class:`MessageForwardInfo`, optional
    
    :param interaction_info: Information about interactions with the message; may be null, defaults to None
    :type interaction_info: :class:`MessageInteractionInfo`, optional
    
    :param unread_reactions: Information about unread reactions added to the message
    :type unread_reactions: :class:`list[UnreadReaction]`
    
    :param reply_in_chat_id: If non-zero, the identifier of the chat to which the replied message belongs; Currently, only messages in the Replies chat can have different reply_in_chat_id and chat_id
    :type reply_in_chat_id: :class:`int`
    
    :param reply_to_message_id: If non-zero, the identifier of the message this message is replying to; can be the identifier of a deleted message
    :type reply_to_message_id: :class:`int`
    
    :param message_thread_id: If non-zero, the identifier of the message thread the message belongs to; unique within the chat to which the message belongs
    :type message_thread_id: :class:`int`
    
    :param ttl: For self-destructing messages, the message's TTL (Time To Live), in seconds; 0 if none. TDLib will send updateDeleteMessages or updateMessageContent once the TTL expires
    :type ttl: :class:`int`
    
    :param ttl_expires_in: Time left before the message expires, in seconds. If the TTL timer isn't started yet, equals to the value of the ttl field
    :type ttl_expires_in: :class:`float`
    
    :param via_bot_user_id: If non-zero, the user identifier of the bot through which this message was sent
    :type via_bot_user_id: :class:`int`
    
    :param author_signature: For channel posts and anonymous group messages, optional author signature
    :type author_signature: :class:`str`
    
    :param media_album_id: Unique identifier of an album this message belongs to. Only audios, documents, photos and videos can be grouped together in albums
    :type media_album_id: :class:`int`
    
    :param restriction_reason: If non-empty, contains a human-readable description of the reason why access to this message must be restricted
    :type restriction_reason: :class:`str`
    
    :param content: Content of the message
    :type content: :class:`MessageContent`
    
    :param reply_markup: Reply markup for the message; may be null, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    
    """

    ID: str = Field("message", alias="@type")
    id: int
    sender_id: MessageSender
    chat_id: int
    sending_state: typing.Optional[MessageSendingState] = None
    scheduling_state: typing.Optional[MessageSchedulingState] = None
    is_outgoing: bool
    is_pinned: bool
    can_be_edited: bool
    can_be_forwarded: bool
    can_be_saved: bool
    can_be_deleted_only_for_self: bool
    can_be_deleted_for_all_users: bool
    can_get_added_reactions: bool
    can_get_statistics: bool
    can_get_message_thread: bool
    can_get_viewers: bool
    can_get_media_timestamp_links: bool
    has_timestamped_media: bool
    is_channel_post: bool
    contains_unread_mention: bool
    date: int
    edit_date: int
    forward_info: typing.Optional[MessageForwardInfo] = None
    interaction_info: typing.Optional[MessageInteractionInfo] = None
    unread_reactions: list[UnreadReaction]
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
