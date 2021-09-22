# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .chat_invite_link import ChatInviteLink
from .chat_location import ChatLocation
from .chat_member_status import ChatMemberStatus
from .chat_permissions import ChatPermissions
from .chat_photo import ChatPhoto
from .message import Message
from .message_sender import MessageSender
from ..base_object import BaseObject


class ChatEventAction(BaseObject):
    """
    Represents a chat event
    
    """

    ID: str = Field("chatEventAction", alias="@type")


class ChatEventDescriptionChanged(ChatEventAction):
    """
    The chat description was changed
    
    :param old_description: Previous chat description
    :type old_description: :class:`str`
    
    :param new_description: New chat description
    :type new_description: :class:`str`
    
    """

    ID: str = Field("chatEventDescriptionChanged", alias="@type")
    old_description: str
    new_description: str

    @staticmethod
    def read(q: dict) -> ChatEventDescriptionChanged:
        return ChatEventDescriptionChanged.construct(**q)


class ChatEventInviteLinkDeleted(ChatEventAction):
    """
    A revoked chat invite link was deleted
    
    :param invite_link: The invite link
    :type invite_link: :class:`ChatInviteLink`
    
    """

    ID: str = Field("chatEventInviteLinkDeleted", alias="@type")
    invite_link: ChatInviteLink

    @staticmethod
    def read(q: dict) -> ChatEventInviteLinkDeleted:
        return ChatEventInviteLinkDeleted.construct(**q)


class ChatEventInviteLinkEdited(ChatEventAction):
    """
    A chat invite link was edited
    
    :param old_invite_link: Previous information about the invite link
    :type old_invite_link: :class:`ChatInviteLink`
    
    :param new_invite_link: New information about the invite link
    :type new_invite_link: :class:`ChatInviteLink`
    
    """

    ID: str = Field("chatEventInviteLinkEdited", alias="@type")
    old_invite_link: ChatInviteLink
    new_invite_link: ChatInviteLink

    @staticmethod
    def read(q: dict) -> ChatEventInviteLinkEdited:
        return ChatEventInviteLinkEdited.construct(**q)


class ChatEventInviteLinkRevoked(ChatEventAction):
    """
    A chat invite link was revoked
    
    :param invite_link: The invite link
    :type invite_link: :class:`ChatInviteLink`
    
    """

    ID: str = Field("chatEventInviteLinkRevoked", alias="@type")
    invite_link: ChatInviteLink

    @staticmethod
    def read(q: dict) -> ChatEventInviteLinkRevoked:
        return ChatEventInviteLinkRevoked.construct(**q)


class ChatEventInvitesToggled(ChatEventAction):
    """
    The can_invite_users permission of a supergroup chat was toggled
    
    :param can_invite_users: New value of can_invite_users permission
    :type can_invite_users: :class:`bool`
    
    """

    ID: str = Field("chatEventInvitesToggled", alias="@type")
    can_invite_users: bool

    @staticmethod
    def read(q: dict) -> ChatEventInvitesToggled:
        return ChatEventInvitesToggled.construct(**q)


class ChatEventIsAllHistoryAvailableToggled(ChatEventAction):
    """
    The is_all_history_available setting of a supergroup was toggled
    
    :param is_all_history_available: New value of is_all_history_available
    :type is_all_history_available: :class:`bool`
    
    """

    ID: str = Field("chatEventIsAllHistoryAvailableToggled", alias="@type")
    is_all_history_available: bool

    @staticmethod
    def read(q: dict) -> ChatEventIsAllHistoryAvailableToggled:
        return ChatEventIsAllHistoryAvailableToggled.construct(**q)


class ChatEventLinkedChatChanged(ChatEventAction):
    """
    The linked chat of a supergroup was changed
    
    :param old_linked_chat_id: Previous supergroup linked chat identifier
    :type old_linked_chat_id: :class:`int`
    
    :param new_linked_chat_id: New supergroup linked chat identifier
    :type new_linked_chat_id: :class:`int`
    
    """

    ID: str = Field("chatEventLinkedChatChanged", alias="@type")
    old_linked_chat_id: int
    new_linked_chat_id: int

    @staticmethod
    def read(q: dict) -> ChatEventLinkedChatChanged:
        return ChatEventLinkedChatChanged.construct(**q)


class ChatEventLocationChanged(ChatEventAction):
    """
    The supergroup location was changed
    
    :param old_location: Previous location; may be null, defaults to None
    :type old_location: :class:`ChatLocation`, optional
    
    :param new_location: New location; may be null, defaults to None
    :type new_location: :class:`ChatLocation`, optional
    
    """

    ID: str = Field("chatEventLocationChanged", alias="@type")
    old_location: typing.Optional[ChatLocation] = None
    new_location: typing.Optional[ChatLocation] = None

    @staticmethod
    def read(q: dict) -> ChatEventLocationChanged:
        return ChatEventLocationChanged.construct(**q)


class ChatEventMemberInvited(ChatEventAction):
    """
    A new chat member was invited
    
    :param user_id: New member user identifier
    :type user_id: :class:`int`
    
    :param status: New member status
    :type status: :class:`ChatMemberStatus`
    
    """

    ID: str = Field("chatEventMemberInvited", alias="@type")
    user_id: int
    status: ChatMemberStatus

    @staticmethod
    def read(q: dict) -> ChatEventMemberInvited:
        return ChatEventMemberInvited.construct(**q)


class ChatEventMemberJoined(ChatEventAction):
    """
    A new member joined the chat
    
    """

    ID: str = Field("chatEventMemberJoined", alias="@type")

    @staticmethod
    def read(q: dict) -> ChatEventMemberJoined:
        return ChatEventMemberJoined.construct(**q)


class ChatEventMemberJoinedByInviteLink(ChatEventAction):
    """
    A new member joined the chat by an invite link
    
    :param invite_link: Invite link used to join the chat
    :type invite_link: :class:`ChatInviteLink`
    
    """

    ID: str = Field("chatEventMemberJoinedByInviteLink", alias="@type")
    invite_link: ChatInviteLink

    @staticmethod
    def read(q: dict) -> ChatEventMemberJoinedByInviteLink:
        return ChatEventMemberJoinedByInviteLink.construct(**q)


class ChatEventMemberLeft(ChatEventAction):
    """
    A member left the chat
    
    """

    ID: str = Field("chatEventMemberLeft", alias="@type")

    @staticmethod
    def read(q: dict) -> ChatEventMemberLeft:
        return ChatEventMemberLeft.construct(**q)


class ChatEventMemberPromoted(ChatEventAction):
    """
    A chat member has gained/lost administrator status, or the list of their administrator privileges has changed
    
    :param user_id: Affected chat member user identifier
    :type user_id: :class:`int`
    
    :param old_status: Previous status of the chat member
    :type old_status: :class:`ChatMemberStatus`
    
    :param new_status: New status of the chat member
    :type new_status: :class:`ChatMemberStatus`
    
    """

    ID: str = Field("chatEventMemberPromoted", alias="@type")
    user_id: int
    old_status: ChatMemberStatus
    new_status: ChatMemberStatus

    @staticmethod
    def read(q: dict) -> ChatEventMemberPromoted:
        return ChatEventMemberPromoted.construct(**q)


class ChatEventMemberRestricted(ChatEventAction):
    """
    A chat member was restricted/unrestricted or banned/unbanned, or the list of their restrictions has changed
    
    :param member_id: Affected chat member identifier
    :type member_id: :class:`MessageSender`
    
    :param old_status: Previous status of the chat member
    :type old_status: :class:`ChatMemberStatus`
    
    :param new_status: New status of the chat member
    :type new_status: :class:`ChatMemberStatus`
    
    """

    ID: str = Field("chatEventMemberRestricted", alias="@type")
    member_id: MessageSender
    old_status: ChatMemberStatus
    new_status: ChatMemberStatus

    @staticmethod
    def read(q: dict) -> ChatEventMemberRestricted:
        return ChatEventMemberRestricted.construct(**q)


class ChatEventMessageDeleted(ChatEventAction):
    """
    A message was deleted
    
    :param message: Deleted message
    :type message: :class:`Message`
    
    """

    ID: str = Field("chatEventMessageDeleted", alias="@type")
    message: Message

    @staticmethod
    def read(q: dict) -> ChatEventMessageDeleted:
        return ChatEventMessageDeleted.construct(**q)


class ChatEventMessageEdited(ChatEventAction):
    """
    A message was edited
    
    :param old_message: The original message before the edit
    :type old_message: :class:`Message`
    
    :param new_message: The message after it was edited
    :type new_message: :class:`Message`
    
    """

    ID: str = Field("chatEventMessageEdited", alias="@type")
    old_message: Message
    new_message: Message

    @staticmethod
    def read(q: dict) -> ChatEventMessageEdited:
        return ChatEventMessageEdited.construct(**q)


class ChatEventMessagePinned(ChatEventAction):
    """
    A message was pinned
    
    :param message: Pinned message
    :type message: :class:`Message`
    
    """

    ID: str = Field("chatEventMessagePinned", alias="@type")
    message: Message

    @staticmethod
    def read(q: dict) -> ChatEventMessagePinned:
        return ChatEventMessagePinned.construct(**q)


class ChatEventMessageTtlSettingChanged(ChatEventAction):
    """
    The message TTL setting was changed
    
    :param old_message_ttl_setting: Previous value of message_ttl_setting
    :type old_message_ttl_setting: :class:`int`
    
    :param new_message_ttl_setting: New value of message_ttl_setting
    :type new_message_ttl_setting: :class:`int`
    
    """

    ID: str = Field("chatEventMessageTtlSettingChanged", alias="@type")
    old_message_ttl_setting: int
    new_message_ttl_setting: int

    @staticmethod
    def read(q: dict) -> ChatEventMessageTtlSettingChanged:
        return ChatEventMessageTtlSettingChanged.construct(**q)


class ChatEventMessageUnpinned(ChatEventAction):
    """
    A message was unpinned
    
    :param message: Unpinned message
    :type message: :class:`Message`
    
    """

    ID: str = Field("chatEventMessageUnpinned", alias="@type")
    message: Message

    @staticmethod
    def read(q: dict) -> ChatEventMessageUnpinned:
        return ChatEventMessageUnpinned.construct(**q)


class ChatEventPermissionsChanged(ChatEventAction):
    """
    The chat permissions was changed
    
    :param old_permissions: Previous chat permissions
    :type old_permissions: :class:`ChatPermissions`
    
    :param new_permissions: New chat permissions
    :type new_permissions: :class:`ChatPermissions`
    
    """

    ID: str = Field("chatEventPermissionsChanged", alias="@type")
    old_permissions: ChatPermissions
    new_permissions: ChatPermissions

    @staticmethod
    def read(q: dict) -> ChatEventPermissionsChanged:
        return ChatEventPermissionsChanged.construct(**q)


class ChatEventPhotoChanged(ChatEventAction):
    """
    The chat photo was changed
    
    :param old_photo: Previous chat photo value; may be null, defaults to None
    :type old_photo: :class:`ChatPhoto`, optional
    
    :param new_photo: New chat photo value; may be null, defaults to None
    :type new_photo: :class:`ChatPhoto`, optional
    
    """

    ID: str = Field("chatEventPhotoChanged", alias="@type")
    old_photo: typing.Optional[ChatPhoto] = None
    new_photo: typing.Optional[ChatPhoto] = None

    @staticmethod
    def read(q: dict) -> ChatEventPhotoChanged:
        return ChatEventPhotoChanged.construct(**q)


class ChatEventPollStopped(ChatEventAction):
    """
    A poll in a message was stopped
    
    :param message: The message with the poll
    :type message: :class:`Message`
    
    """

    ID: str = Field("chatEventPollStopped", alias="@type")
    message: Message

    @staticmethod
    def read(q: dict) -> ChatEventPollStopped:
        return ChatEventPollStopped.construct(**q)


class ChatEventSignMessagesToggled(ChatEventAction):
    """
    The sign_messages setting of a channel was toggled
    
    :param sign_messages: New value of sign_messages
    :type sign_messages: :class:`bool`
    
    """

    ID: str = Field("chatEventSignMessagesToggled", alias="@type")
    sign_messages: bool

    @staticmethod
    def read(q: dict) -> ChatEventSignMessagesToggled:
        return ChatEventSignMessagesToggled.construct(**q)


class ChatEventSlowModeDelayChanged(ChatEventAction):
    """
    The slow_mode_delay setting of a supergroup was changed
    
    :param old_slow_mode_delay: Previous value of slow_mode_delay
    :type old_slow_mode_delay: :class:`int`
    
    :param new_slow_mode_delay: New value of slow_mode_delay
    :type new_slow_mode_delay: :class:`int`
    
    """

    ID: str = Field("chatEventSlowModeDelayChanged", alias="@type")
    old_slow_mode_delay: int
    new_slow_mode_delay: int

    @staticmethod
    def read(q: dict) -> ChatEventSlowModeDelayChanged:
        return ChatEventSlowModeDelayChanged.construct(**q)


class ChatEventStickerSetChanged(ChatEventAction):
    """
    The supergroup sticker set was changed
    
    :param old_sticker_set_id: Previous identifier of the chat sticker set; 0 if none
    :type old_sticker_set_id: :class:`int`
    
    :param new_sticker_set_id: New identifier of the chat sticker set; 0 if none
    :type new_sticker_set_id: :class:`int`
    
    """

    ID: str = Field("chatEventStickerSetChanged", alias="@type")
    old_sticker_set_id: int
    new_sticker_set_id: int

    @staticmethod
    def read(q: dict) -> ChatEventStickerSetChanged:
        return ChatEventStickerSetChanged.construct(**q)


class ChatEventTitleChanged(ChatEventAction):
    """
    The chat title was changed
    
    :param old_title: Previous chat title
    :type old_title: :class:`str`
    
    :param new_title: New chat title
    :type new_title: :class:`str`
    
    """

    ID: str = Field("chatEventTitleChanged", alias="@type")
    old_title: str
    new_title: str

    @staticmethod
    def read(q: dict) -> ChatEventTitleChanged:
        return ChatEventTitleChanged.construct(**q)


class ChatEventUsernameChanged(ChatEventAction):
    """
    The chat username was changed
    
    :param old_username: Previous chat username
    :type old_username: :class:`str`
    
    :param new_username: New chat username
    :type new_username: :class:`str`
    
    """

    ID: str = Field("chatEventUsernameChanged", alias="@type")
    old_username: str
    new_username: str

    @staticmethod
    def read(q: dict) -> ChatEventUsernameChanged:
        return ChatEventUsernameChanged.construct(**q)


class ChatEventVoiceChatCreated(ChatEventAction):
    """
    A voice chat was created
    
    :param group_call_id: Identifier of the voice chat. The voice chat can be received through the method getGroupCall
    :type group_call_id: :class:`int`
    
    """

    ID: str = Field("chatEventVoiceChatCreated", alias="@type")
    group_call_id: int

    @staticmethod
    def read(q: dict) -> ChatEventVoiceChatCreated:
        return ChatEventVoiceChatCreated.construct(**q)


class ChatEventVoiceChatDiscarded(ChatEventAction):
    """
    A voice chat was discarded
    
    :param group_call_id: Identifier of the voice chat. The voice chat can be received through the method getGroupCall
    :type group_call_id: :class:`int`
    
    """

    ID: str = Field("chatEventVoiceChatDiscarded", alias="@type")
    group_call_id: int

    @staticmethod
    def read(q: dict) -> ChatEventVoiceChatDiscarded:
        return ChatEventVoiceChatDiscarded.construct(**q)


class ChatEventVoiceChatMuteNewParticipantsToggled(ChatEventAction):
    """
    The mute_new_participants setting of a voice chat was toggled
    
    :param mute_new_participants: New value of the mute_new_participants setting
    :type mute_new_participants: :class:`bool`
    
    """

    ID: str = Field("chatEventVoiceChatMuteNewParticipantsToggled", alias="@type")
    mute_new_participants: bool

    @staticmethod
    def read(q: dict) -> ChatEventVoiceChatMuteNewParticipantsToggled:
        return ChatEventVoiceChatMuteNewParticipantsToggled.construct(**q)


class ChatEventVoiceChatParticipantIsMutedToggled(ChatEventAction):
    """
    A voice chat participant was muted or unmuted
    
    :param participant_id: Identifier of the affected group call participant
    :type participant_id: :class:`MessageSender`
    
    :param is_muted: New value of is_muted
    :type is_muted: :class:`bool`
    
    """

    ID: str = Field("chatEventVoiceChatParticipantIsMutedToggled", alias="@type")
    participant_id: MessageSender
    is_muted: bool

    @staticmethod
    def read(q: dict) -> ChatEventVoiceChatParticipantIsMutedToggled:
        return ChatEventVoiceChatParticipantIsMutedToggled.construct(**q)


class ChatEventVoiceChatParticipantVolumeLevelChanged(ChatEventAction):
    """
    A voice chat participant volume level was changed
    
    :param participant_id: Identifier of the affected group call participant
    :type participant_id: :class:`MessageSender`
    
    :param volume_level: New value of volume_level; 1-20000 in hundreds of percents
    :type volume_level: :class:`int`
    
    """

    ID: str = Field("chatEventVoiceChatParticipantVolumeLevelChanged", alias="@type")
    participant_id: MessageSender
    volume_level: int

    @staticmethod
    def read(q: dict) -> ChatEventVoiceChatParticipantVolumeLevelChanged:
        return ChatEventVoiceChatParticipantVolumeLevelChanged.construct(**q)
