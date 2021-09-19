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
    
    Params:
        old_description (:class:`str`)
            Previous chat description
        
        new_description (:class:`str`)
            New chat description
        
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
    
    Params:
        invite_link (:class:`ChatInviteLink`)
            The invite link
        
    """

    ID: str = Field("chatEventInviteLinkDeleted", alias="@type")
    invite_link: ChatInviteLink

    @staticmethod
    def read(q: dict) -> ChatEventInviteLinkDeleted:
        return ChatEventInviteLinkDeleted.construct(**q)


class ChatEventInviteLinkEdited(ChatEventAction):
    """
    A chat invite link was edited
    
    Params:
        old_invite_link (:class:`ChatInviteLink`)
            Previous information about the invite link
        
        new_invite_link (:class:`ChatInviteLink`)
            New information about the invite link
        
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
    
    Params:
        invite_link (:class:`ChatInviteLink`)
            The invite link
        
    """

    ID: str = Field("chatEventInviteLinkRevoked", alias="@type")
    invite_link: ChatInviteLink

    @staticmethod
    def read(q: dict) -> ChatEventInviteLinkRevoked:
        return ChatEventInviteLinkRevoked.construct(**q)


class ChatEventInvitesToggled(ChatEventAction):
    """
    The can_invite_users permission of a supergroup chat was toggled
    
    Params:
        can_invite_users (:class:`bool`)
            New value of can_invite_users permission
        
    """

    ID: str = Field("chatEventInvitesToggled", alias="@type")
    can_invite_users: bool

    @staticmethod
    def read(q: dict) -> ChatEventInvitesToggled:
        return ChatEventInvitesToggled.construct(**q)


class ChatEventIsAllHistoryAvailableToggled(ChatEventAction):
    """
    The is_all_history_available setting of a supergroup was toggled
    
    Params:
        is_all_history_available (:class:`bool`)
            New value of is_all_history_available
        
    """

    ID: str = Field("chatEventIsAllHistoryAvailableToggled", alias="@type")
    is_all_history_available: bool

    @staticmethod
    def read(q: dict) -> ChatEventIsAllHistoryAvailableToggled:
        return ChatEventIsAllHistoryAvailableToggled.construct(**q)


class ChatEventLinkedChatChanged(ChatEventAction):
    """
    The linked chat of a supergroup was changed
    
    Params:
        old_linked_chat_id (:class:`int`)
            Previous supergroup linked chat identifier
        
        new_linked_chat_id (:class:`int`)
            New supergroup linked chat identifier
        
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
    
    Params:
        old_location (:class:`ChatLocation`)
            Previous location; may be null
        
        new_location (:class:`ChatLocation`)
            New location; may be null
        
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
    
    Params:
        user_id (:class:`int`)
            New member user identifier
        
        status (:class:`ChatMemberStatus`)
            New member status
        
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
    
    Params:
        invite_link (:class:`ChatInviteLink`)
            Invite link used to join the chat
        
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
    
    Params:
        user_id (:class:`int`)
            Affected chat member user identifier
        
        old_status (:class:`ChatMemberStatus`)
            Previous status of the chat member
        
        new_status (:class:`ChatMemberStatus`)
            New status of the chat member
        
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
    
    Params:
        member_id (:class:`MessageSender`)
            Affected chat member identifier
        
        old_status (:class:`ChatMemberStatus`)
            Previous status of the chat member
        
        new_status (:class:`ChatMemberStatus`)
            New status of the chat member
        
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
    
    Params:
        message (:class:`Message`)
            Deleted message
        
    """

    ID: str = Field("chatEventMessageDeleted", alias="@type")
    message: Message

    @staticmethod
    def read(q: dict) -> ChatEventMessageDeleted:
        return ChatEventMessageDeleted.construct(**q)


class ChatEventMessageEdited(ChatEventAction):
    """
    A message was edited
    
    Params:
        old_message (:class:`Message`)
            The original message before the edit
        
        new_message (:class:`Message`)
            The message after it was edited
        
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
    
    Params:
        message (:class:`Message`)
            Pinned message
        
    """

    ID: str = Field("chatEventMessagePinned", alias="@type")
    message: Message

    @staticmethod
    def read(q: dict) -> ChatEventMessagePinned:
        return ChatEventMessagePinned.construct(**q)


class ChatEventMessageTtlSettingChanged(ChatEventAction):
    """
    The message TTL setting was changed
    
    Params:
        old_message_ttl_setting (:class:`int`)
            Previous value of message_ttl_setting
        
        new_message_ttl_setting (:class:`int`)
            New value of message_ttl_setting
        
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
    
    Params:
        message (:class:`Message`)
            Unpinned message
        
    """

    ID: str = Field("chatEventMessageUnpinned", alias="@type")
    message: Message

    @staticmethod
    def read(q: dict) -> ChatEventMessageUnpinned:
        return ChatEventMessageUnpinned.construct(**q)


class ChatEventPermissionsChanged(ChatEventAction):
    """
    The chat permissions was changed
    
    Params:
        old_permissions (:class:`ChatPermissions`)
            Previous chat permissions
        
        new_permissions (:class:`ChatPermissions`)
            New chat permissions
        
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
    
    Params:
        old_photo (:class:`ChatPhoto`)
            Previous chat photo value; may be null
        
        new_photo (:class:`ChatPhoto`)
            New chat photo value; may be null
        
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
    
    Params:
        message (:class:`Message`)
            The message with the poll
        
    """

    ID: str = Field("chatEventPollStopped", alias="@type")
    message: Message

    @staticmethod
    def read(q: dict) -> ChatEventPollStopped:
        return ChatEventPollStopped.construct(**q)


class ChatEventSignMessagesToggled(ChatEventAction):
    """
    The sign_messages setting of a channel was toggled
    
    Params:
        sign_messages (:class:`bool`)
            New value of sign_messages
        
    """

    ID: str = Field("chatEventSignMessagesToggled", alias="@type")
    sign_messages: bool

    @staticmethod
    def read(q: dict) -> ChatEventSignMessagesToggled:
        return ChatEventSignMessagesToggled.construct(**q)


class ChatEventSlowModeDelayChanged(ChatEventAction):
    """
    The slow_mode_delay setting of a supergroup was changed
    
    Params:
        old_slow_mode_delay (:class:`int`)
            Previous value of slow_mode_delay
        
        new_slow_mode_delay (:class:`int`)
            New value of slow_mode_delay
        
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
    
    Params:
        old_sticker_set_id (:class:`int`)
            Previous identifier of the chat sticker set; 0 if none
        
        new_sticker_set_id (:class:`int`)
            New identifier of the chat sticker set; 0 if none
        
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
    
    Params:
        old_title (:class:`str`)
            Previous chat title
        
        new_title (:class:`str`)
            New chat title
        
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
    
    Params:
        old_username (:class:`str`)
            Previous chat username
        
        new_username (:class:`str`)
            New chat username
        
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
    
    Params:
        group_call_id (:class:`int`)
            Identifier of the voice chat. The voice chat can be received through the method getGroupCall
        
    """

    ID: str = Field("chatEventVoiceChatCreated", alias="@type")
    group_call_id: int

    @staticmethod
    def read(q: dict) -> ChatEventVoiceChatCreated:
        return ChatEventVoiceChatCreated.construct(**q)


class ChatEventVoiceChatDiscarded(ChatEventAction):
    """
    A voice chat was discarded
    
    Params:
        group_call_id (:class:`int`)
            Identifier of the voice chat. The voice chat can be received through the method getGroupCall
        
    """

    ID: str = Field("chatEventVoiceChatDiscarded", alias="@type")
    group_call_id: int

    @staticmethod
    def read(q: dict) -> ChatEventVoiceChatDiscarded:
        return ChatEventVoiceChatDiscarded.construct(**q)


class ChatEventVoiceChatMuteNewParticipantsToggled(ChatEventAction):
    """
    The mute_new_participants setting of a voice chat was toggled
    
    Params:
        mute_new_participants (:class:`bool`)
            New value of the mute_new_participants setting
        
    """

    ID: str = Field("chatEventVoiceChatMuteNewParticipantsToggled", alias="@type")
    mute_new_participants: bool

    @staticmethod
    def read(q: dict) -> ChatEventVoiceChatMuteNewParticipantsToggled:
        return ChatEventVoiceChatMuteNewParticipantsToggled.construct(**q)


class ChatEventVoiceChatParticipantIsMutedToggled(ChatEventAction):
    """
    A voice chat participant was muted or unmuted
    
    Params:
        participant_id (:class:`MessageSender`)
            Identifier of the affected group call participant
        
        is_muted (:class:`bool`)
            New value of is_muted
        
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
    
    Params:
        participant_id (:class:`MessageSender`)
            Identifier of the affected group call participant
        
        volume_level (:class:`int`)
            New value of volume_level; 1-20000 in hundreds of percents
        
    """

    ID: str = Field("chatEventVoiceChatParticipantVolumeLevelChanged", alias="@type")
    participant_id: MessageSender
    volume_level: int

    @staticmethod
    def read(q: dict) -> ChatEventVoiceChatParticipantVolumeLevelChanged:
        return ChatEventVoiceChatParticipantVolumeLevelChanged.construct(**q)
