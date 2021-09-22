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
    
    :param id: Chat unique identifier
    :type id: :class:`int`
    
    :param type_: Type of the chat
    :type type_: :class:`ChatType`
    
    :param title: Chat title
    :type title: :class:`str`
    
    :param photo: Chat photo; may be null, defaults to None
    :type photo: :class:`ChatPhotoInfo`, optional
    
    :param permissions: Actions that non-administrator chat members are allowed to take in the chat
    :type permissions: :class:`ChatPermissions`
    
    :param last_message: Last message in the chat; may be null, defaults to None
    :type last_message: :class:`Message`, optional
    
    :param positions: Positions of the chat in chat lists
    :type positions: :class:`list[ChatPosition]`
    
    :param is_marked_as_unread: True, if the chat is marked as unread
    :type is_marked_as_unread: :class:`bool`
    
    :param is_blocked: True, if the chat is blocked by the current user and private messages from the chat can't be received
    :type is_blocked: :class:`bool`
    
    :param has_scheduled_messages: True, if the chat has scheduled messages
    :type has_scheduled_messages: :class:`bool`
    
    :param can_be_deleted_only_for_self: True, if the chat messages can be deleted only for the current user while other users will continue to see the messages
    :type can_be_deleted_only_for_self: :class:`bool`
    
    :param can_be_deleted_for_all_users: True, if the chat messages can be deleted for all users
    :type can_be_deleted_for_all_users: :class:`bool`
    
    :param can_be_reported: True, if the chat can be reported to Telegram moderators through reportChat or reportChatPhoto
    :type can_be_reported: :class:`bool`
    
    :param default_disable_notification: Default value of the disable_notification parameter, used when a message is sent to the chat
    :type default_disable_notification: :class:`bool`
    
    :param unread_count: Number of unread messages in the chat
    :type unread_count: :class:`int`
    
    :param last_read_inbox_message_id: Identifier of the last read incoming message
    :type last_read_inbox_message_id: :class:`int`
    
    :param last_read_outbox_message_id: Identifier of the last read outgoing message
    :type last_read_outbox_message_id: :class:`int`
    
    :param unread_mention_count: Number of unread messages with a mention/reply in the chat
    :type unread_mention_count: :class:`int`
    
    :param notification_settings: Notification settings for this chat
    :type notification_settings: :class:`ChatNotificationSettings`
    
    :param message_ttl_setting: Current message Time To Live setting (self-destruct timer) for the chat; 0 if not defined. TTL is counted from the time message or its content is viewed in secret chats and from the send date in other chats
    :type message_ttl_setting: :class:`int`
    
    :param theme_name: If non-empty, name of a theme, set for the chat
    :type theme_name: :class:`str`
    
    :param action_bar: Describes actions which should be possible to do through a chat action bar; may be null, defaults to None
    :type action_bar: :class:`ChatActionBar`, optional
    
    :param voice_chat: Contains information about voice chat of the chat
    :type voice_chat: :class:`VoiceChat`
    
    :param reply_markup_message_id: Identifier of the message from which reply markup needs to be used; 0 if there is no default custom reply markup in the chat
    :type reply_markup_message_id: :class:`int`
    
    :param draft_message: A draft of a message in the chat; may be null, defaults to None
    :type draft_message: :class:`DraftMessage`, optional
    
    :param client_data: Contains application-specific data associated with the chat. (For example, the chat scroll position or local chat notification settings can be stored here.) Persistent if the message database is used
    :type client_data: :class:`str`
    
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
    theme_name: str
    action_bar: typing.Optional[ChatActionBar] = None
    voice_chat: VoiceChat
    reply_markup_message_id: int
    draft_message: typing.Optional[DraftMessage] = None
    client_data: str

    @staticmethod
    def read(q: dict) -> Chat:
        return Chat.construct(**q)
