# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .chat_action_bar import ChatActionBar
from .chat_notification_settings import ChatNotificationSettings
from .chat_permissions import ChatPermissions
from .chat_photo_info import ChatPhotoInfo
from .chat_position import ChatPosition
from .chat_type import ChatType
from .draft_message import DraftMessage
from .message import Message
from .voice_chat import VoiceChat
from ..base_object import BaseObject


class Chat(BaseObject):
    """
    A chat. (Can be a private chat, basic group, supergroup, or secret chat)
    
    Params:
        id (:class:`int`)
            Chat unique identifier
        
        type_ (:class:`ChatType`)
            Type of the chat
        
        title (:class:`str`)
            Chat title
        
        photo (:class:`ChatPhotoInfo`)
            Chat photo; may be null
        
        permissions (:class:`ChatPermissions`)
            Actions that non-administrator chat members are allowed to take in the chat
        
        last_message (:class:`Message`)
            Last message in the chat; may be null
        
        positions (:obj:`list[ChatPosition]`)
            Positions of the chat in chat lists
        
        is_marked_as_unread (:class:`bool`)
            True, if the chat is marked as unread
        
        is_blocked (:class:`bool`)
            True, if the chat is blocked by the current user and private messages from the chat can't be received
        
        has_scheduled_messages (:class:`bool`)
            True, if the chat has scheduled messages
        
        can_be_deleted_only_for_self (:class:`bool`)
            True, if the chat messages can be deleted only for the current user while other users will continue to see the messages
        
        can_be_deleted_for_all_users (:class:`bool`)
            True, if the chat messages can be deleted for all users
        
        can_be_reported (:class:`bool`)
            True, if the chat can be reported to Telegram moderators through reportChat or reportChatPhoto
        
        default_disable_notification (:class:`bool`)
            Default value of the disable_notification parameter, used when a message is sent to the chat
        
        unread_count (:class:`int`)
            Number of unread messages in the chat
        
        last_read_inbox_message_id (:class:`int`)
            Identifier of the last read incoming message
        
        last_read_outbox_message_id (:class:`int`)
            Identifier of the last read outgoing message
        
        unread_mention_count (:class:`int`)
            Number of unread messages with a mention/reply in the chat
        
        notification_settings (:class:`ChatNotificationSettings`)
            Notification settings for this chat
        
        message_ttl_setting (:class:`int`)
            Current message Time To Live setting (self-destruct timer) for the chat; 0 if not defined. TTL is counted from the time message or its content is viewed in secret chats and from the send date in other chats
        
        action_bar (:class:`ChatActionBar`)
            Describes actions which should be possible to do through a chat action bar; may be null
        
        voice_chat (:class:`VoiceChat`)
            Contains information about voice chat of the chat
        
        reply_markup_message_id (:class:`int`)
            Identifier of the message from which reply markup needs to be used; 0 if there is no default custom reply markup in the chat
        
        draft_message (:class:`DraftMessage`)
            A draft of a message in the chat; may be null
        
        client_data (:class:`str`)
            Contains application-specific data associated with the chat. (For example, the chat scroll position or local chat notification settings can be stored here.) Persistent if the message database is used
        
    """

    ID: str = Field("chat", alias="@type")
    id: int
    type_: ChatType = Field(..., alias='type')
    title: str
    photo: typing.Optional[ChatPhotoInfo] = None
    permissions: ChatPermissions
    last_message: typing.Optional[Message] = None
    positions: list[ChatPosition]
    is_marked_as_unread: bool
    is_blocked: bool
    has_scheduled_messages: bool
    can_be_deleted_only_for_self: bool
    can_be_deleted_for_all_users: bool
    can_be_reported: bool
    default_disable_notification: bool
    unread_count: int
    last_read_inbox_message_id: int
    last_read_outbox_message_id: int
    unread_mention_count: int
    notification_settings: ChatNotificationSettings
    message_ttl_setting: int
    action_bar: typing.Optional[ChatActionBar] = None
    voice_chat: VoiceChat
    reply_markup_message_id: int
    draft_message: typing.Optional[DraftMessage] = None
    client_data: str

    @staticmethod
    def read(q: dict) -> Chat:
        return Chat.construct(**q)
