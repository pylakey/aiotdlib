# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .address import Address
from .authorization_state import AuthorizationState
from .background import Background
from .basic_group import BasicGroup
from .basic_group_full_info import BasicGroupFullInfo
from .call import Call
from .callback_query_payload import CallbackQueryPayload
from .chat import Chat
from .chat_action import ChatAction
from .chat_action_bar import ChatActionBar
from .chat_filter_info import ChatFilterInfo
from .chat_invite_link import ChatInviteLink
from .chat_list import ChatList
from .chat_member import ChatMember
from .chat_nearby import ChatNearby
from .chat_notification_settings import ChatNotificationSettings
from .chat_permissions import ChatPermissions
from .chat_photo_info import ChatPhotoInfo
from .chat_position import ChatPosition
from .chat_type import ChatType
from .connection_state import ConnectionState
from .draft_message import DraftMessage
from .file import File
from .group_call import GroupCall
from .group_call_participant import GroupCallParticipant
from .language_pack_string import LanguagePackString
from .location import Location
from .message import Message
from .message_content import MessageContent
from .message_interaction_info import MessageInteractionInfo
from .notification import Notification
from .notification_group import NotificationGroup
from .notification_group_type import NotificationGroupType
from .notification_settings_scope import NotificationSettingsScope
from .option_value import OptionValue
from .order_info import OrderInfo
from .poll import Poll
from .reply_markup import ReplyMarkup
from .scope_notification_settings import ScopeNotificationSettings
from .secret_chat import SecretChat
from .sticker_set import StickerSet
from .sticker_sets import StickerSets
from .suggested_action import SuggestedAction
from .supergroup import Supergroup
from .supergroup_full_info import SupergroupFullInfo
from .terms_of_service import TermsOfService
from .user import User
from .user_full_info import UserFullInfo
from .user_privacy_setting import UserPrivacySetting
from .user_privacy_setting_rules import UserPrivacySettingRules
from .user_status import UserStatus
from .voice_chat import VoiceChat
from ..base_object import BaseObject


class Update(BaseObject):
    """
    Contains notifications about data changes
    
    """

    ID: str = Field("update", alias="@type")


class UpdateActiveNotifications(Update):
    """
    Contains active notifications that was shown on previous application launches. This update is sent only if the message database is used. In that case it comes once before any updateNotification and updateNotificationGroup update
    
    Params:
        groups (:obj:`list[NotificationGroup]`)
            Lists of active notification groups
        
    """

    ID: str = Field("updateActiveNotifications", alias="@type")
    groups: list[NotificationGroup]

    @staticmethod
    def read(q: dict) -> UpdateActiveNotifications:
        return UpdateActiveNotifications.construct(**q)


class UpdateAnimationSearchParameters(Update):
    """
    The parameters of animation search through GetOption("animation_search_bot_username") bot has changed
    
    Params:
        provider (:class:`str`)
            Name of the animation search provider
        
        emojis (:obj:`list[str]`)
            The new list of emojis suggested for searching
        
    """

    ID: str = Field("updateAnimationSearchParameters", alias="@type")
    provider: str
    emojis: list[str]

    @staticmethod
    def read(q: dict) -> UpdateAnimationSearchParameters:
        return UpdateAnimationSearchParameters.construct(**q)


class UpdateAuthorizationState(Update):
    """
    The user authorization state has changed
    
    Params:
        authorization_state (:class:`AuthorizationState`)
            New authorization state
        
    """

    ID: str = Field("updateAuthorizationState", alias="@type")
    authorization_state: AuthorizationState

    @staticmethod
    def read(q: dict) -> UpdateAuthorizationState:
        return UpdateAuthorizationState.construct(**q)


class UpdateBasicGroup(Update):
    """
    Some data of a basic group has changed. This update is guaranteed to come before the basic group identifier is returned to the application
    
    Params:
        basic_group (:class:`BasicGroup`)
            New data about the group
        
    """

    ID: str = Field("updateBasicGroup", alias="@type")
    basic_group: BasicGroup

    @staticmethod
    def read(q: dict) -> UpdateBasicGroup:
        return UpdateBasicGroup.construct(**q)


class UpdateBasicGroupFullInfo(Update):
    """
    Some data from basicGroupFullInfo has been changed
    
    Params:
        basic_group_id (:class:`int`)
            Identifier of a basic group
        
        basic_group_full_info (:class:`BasicGroupFullInfo`)
            New full information about the group
        
    """

    ID: str = Field("updateBasicGroupFullInfo", alias="@type")
    basic_group_id: int
    basic_group_full_info: BasicGroupFullInfo

    @staticmethod
    def read(q: dict) -> UpdateBasicGroupFullInfo:
        return UpdateBasicGroupFullInfo.construct(**q)


class UpdateCall(Update):
    """
    New call was created or information about a call was updated
    
    Params:
        call (:class:`Call`)
            New data about a call
        
    """

    ID: str = Field("updateCall", alias="@type")
    call: Call

    @staticmethod
    def read(q: dict) -> UpdateCall:
        return UpdateCall.construct(**q)


class UpdateChatActionBar(Update):
    """
    The chat action bar was changed
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        action_bar (:class:`ChatActionBar`)
            The new value of the action bar; may be null
        
    """

    ID: str = Field("updateChatActionBar", alias="@type")
    chat_id: int
    action_bar: typing.Optional[ChatActionBar] = None

    @staticmethod
    def read(q: dict) -> UpdateChatActionBar:
        return UpdateChatActionBar.construct(**q)


class UpdateChatDefaultDisableNotification(Update):
    """
    The value of the default disable_notification parameter, used when a message is sent to the chat, was changed
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        default_disable_notification (:class:`bool`)
            The new default_disable_notification value
        
    """

    ID: str = Field("updateChatDefaultDisableNotification", alias="@type")
    chat_id: int
    default_disable_notification: bool

    @staticmethod
    def read(q: dict) -> UpdateChatDefaultDisableNotification:
        return UpdateChatDefaultDisableNotification.construct(**q)


class UpdateChatDraftMessage(Update):
    """
    A chat draft has changed. Be aware that the update may come in the currently opened chat but with old content of the draft. If the user has changed the content of the draft, this update shouldn't be applied
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        draft_message (:class:`DraftMessage`)
            The new draft message; may be null
        
        positions (:obj:`list[ChatPosition]`)
            The new chat positions in the chat lists
        
    """

    ID: str = Field("updateChatDraftMessage", alias="@type")
    chat_id: int
    draft_message: typing.Optional[DraftMessage] = None
    positions: list[ChatPosition]

    @staticmethod
    def read(q: dict) -> UpdateChatDraftMessage:
        return UpdateChatDraftMessage.construct(**q)


class UpdateChatFilters(Update):
    """
    The list of chat filters or a chat filter has changed
    
    Params:
        chat_filters (:obj:`list[ChatFilterInfo]`)
            The new list of chat filters
        
    """

    ID: str = Field("updateChatFilters", alias="@type")
    chat_filters: list[ChatFilterInfo]

    @staticmethod
    def read(q: dict) -> UpdateChatFilters:
        return UpdateChatFilters.construct(**q)


class UpdateChatHasScheduledMessages(Update):
    """
    A chat's has_scheduled_messages field has changed
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        has_scheduled_messages (:class:`bool`)
            New value of has_scheduled_messages
        
    """

    ID: str = Field("updateChatHasScheduledMessages", alias="@type")
    chat_id: int
    has_scheduled_messages: bool

    @staticmethod
    def read(q: dict) -> UpdateChatHasScheduledMessages:
        return UpdateChatHasScheduledMessages.construct(**q)


class UpdateChatIsBlocked(Update):
    """
    A chat was blocked or unblocked
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        is_blocked (:class:`bool`)
            New value of is_blocked
        
    """

    ID: str = Field("updateChatIsBlocked", alias="@type")
    chat_id: int
    is_blocked: bool

    @staticmethod
    def read(q: dict) -> UpdateChatIsBlocked:
        return UpdateChatIsBlocked.construct(**q)


class UpdateChatIsMarkedAsUnread(Update):
    """
    A chat was marked as unread or was read
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        is_marked_as_unread (:class:`bool`)
            New value of is_marked_as_unread
        
    """

    ID: str = Field("updateChatIsMarkedAsUnread", alias="@type")
    chat_id: int
    is_marked_as_unread: bool

    @staticmethod
    def read(q: dict) -> UpdateChatIsMarkedAsUnread:
        return UpdateChatIsMarkedAsUnread.construct(**q)


class UpdateChatLastMessage(Update):
    """
    The last message of a chat was changed. If last_message is null, then the last message in the chat became unknown. Some new unknown messages might be added to the chat in this case
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        last_message (:class:`Message`)
            The new last message in the chat; may be null
        
        positions (:obj:`list[ChatPosition]`)
            The new chat positions in the chat lists
        
    """

    ID: str = Field("updateChatLastMessage", alias="@type")
    chat_id: int
    last_message: typing.Optional[Message] = None
    positions: list[ChatPosition]

    @staticmethod
    def read(q: dict) -> UpdateChatLastMessage:
        return UpdateChatLastMessage.construct(**q)


class UpdateChatMember(Update):
    """
    User rights changed in a chat; for bots only
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        actor_user_id (:class:`int`)
            Identifier of the user, changing the rights
        
        date (:class:`int`)
            Point in time (Unix timestamp) when the user rights was changed
        
        invite_link (:class:`ChatInviteLink`)
            If user has joined the chat using an invite link, the invite link; may be null
        
        old_chat_member (:class:`ChatMember`)
            Previous chat member
        
        new_chat_member (:class:`ChatMember`)
            New chat member
        
    """

    ID: str = Field("updateChatMember", alias="@type")
    chat_id: int
    actor_user_id: int
    date: int
    invite_link: typing.Optional[ChatInviteLink] = None
    old_chat_member: ChatMember
    new_chat_member: ChatMember

    @staticmethod
    def read(q: dict) -> UpdateChatMember:
        return UpdateChatMember.construct(**q)


class UpdateChatMessageTtlSetting(Update):
    """
    The message Time To Live setting for a chat was changed
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        message_ttl_setting (:class:`int`)
            New value of message_ttl_setting
        
    """

    ID: str = Field("updateChatMessageTtlSetting", alias="@type")
    chat_id: int
    message_ttl_setting: int

    @staticmethod
    def read(q: dict) -> UpdateChatMessageTtlSetting:
        return UpdateChatMessageTtlSetting.construct(**q)


class UpdateChatNotificationSettings(Update):
    """
    Notification settings for a chat were changed
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        notification_settings (:class:`ChatNotificationSettings`)
            The new notification settings
        
    """

    ID: str = Field("updateChatNotificationSettings", alias="@type")
    chat_id: int
    notification_settings: ChatNotificationSettings

    @staticmethod
    def read(q: dict) -> UpdateChatNotificationSettings:
        return UpdateChatNotificationSettings.construct(**q)


class UpdateChatOnlineMemberCount(Update):
    """
    The number of online group members has changed. This update with non-zero count is sent only for currently opened chats. There is no guarantee that it will be sent just after the count has changed
    
    Params:
        chat_id (:class:`int`)
            Identifier of the chat
        
        online_member_count (:class:`int`)
            New number of online members in the chat, or 0 if unknown
        
    """

    ID: str = Field("updateChatOnlineMemberCount", alias="@type")
    chat_id: int
    online_member_count: int

    @staticmethod
    def read(q: dict) -> UpdateChatOnlineMemberCount:
        return UpdateChatOnlineMemberCount.construct(**q)


class UpdateChatPermissions(Update):
    """
    Chat permissions was changed
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        permissions (:class:`ChatPermissions`)
            The new chat permissions
        
    """

    ID: str = Field("updateChatPermissions", alias="@type")
    chat_id: int
    permissions: ChatPermissions

    @staticmethod
    def read(q: dict) -> UpdateChatPermissions:
        return UpdateChatPermissions.construct(**q)


class UpdateChatPhoto(Update):
    """
    A chat photo was changed
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        photo (:class:`ChatPhotoInfo`)
            The new chat photo; may be null
        
    """

    ID: str = Field("updateChatPhoto", alias="@type")
    chat_id: int
    photo: typing.Optional[ChatPhotoInfo] = None

    @staticmethod
    def read(q: dict) -> UpdateChatPhoto:
        return UpdateChatPhoto.construct(**q)


class UpdateChatPosition(Update):
    """
    The position of a chat in a chat list has changed. Instead of this update updateChatLastMessage or updateChatDraftMessage might be sent
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        position (:class:`ChatPosition`)
            New chat position. If new order is 0, then the chat needs to be removed from the list
        
    """

    ID: str = Field("updateChatPosition", alias="@type")
    chat_id: int
    position: ChatPosition

    @staticmethod
    def read(q: dict) -> UpdateChatPosition:
        return UpdateChatPosition.construct(**q)


class UpdateChatReadInbox(Update):
    """
    Incoming messages were read or number of unread messages has been changed
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        last_read_inbox_message_id (:class:`int`)
            Identifier of the last read incoming message
        
        unread_count (:class:`int`)
            The number of unread messages left in the chat
        
    """

    ID: str = Field("updateChatReadInbox", alias="@type")
    chat_id: int
    last_read_inbox_message_id: int
    unread_count: int

    @staticmethod
    def read(q: dict) -> UpdateChatReadInbox:
        return UpdateChatReadInbox.construct(**q)


class UpdateChatReadOutbox(Update):
    """
    Outgoing messages were read
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        last_read_outbox_message_id (:class:`int`)
            Identifier of last read outgoing message
        
    """

    ID: str = Field("updateChatReadOutbox", alias="@type")
    chat_id: int
    last_read_outbox_message_id: int

    @staticmethod
    def read(q: dict) -> UpdateChatReadOutbox:
        return UpdateChatReadOutbox.construct(**q)


class UpdateChatReplyMarkup(Update):
    """
    The default chat reply markup was changed. Can occur because new messages with reply markup were received or because an old reply markup was hidden by the user
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        reply_markup_message_id (:class:`int`)
            Identifier of the message from which reply markup needs to be used; 0 if there is no default custom reply markup in the chat
        
    """

    ID: str = Field("updateChatReplyMarkup", alias="@type")
    chat_id: int
    reply_markup_message_id: int

    @staticmethod
    def read(q: dict) -> UpdateChatReplyMarkup:
        return UpdateChatReplyMarkup.construct(**q)


class UpdateChatTitle(Update):
    """
    The title of a chat was changed
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        title (:class:`str`)
            The new chat title
        
    """

    ID: str = Field("updateChatTitle", alias="@type")
    chat_id: int
    title: str

    @staticmethod
    def read(q: dict) -> UpdateChatTitle:
        return UpdateChatTitle.construct(**q)


class UpdateChatUnreadMentionCount(Update):
    """
    The chat unread_mention_count has changed
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        unread_mention_count (:class:`int`)
            The number of unread mention messages left in the chat
        
    """

    ID: str = Field("updateChatUnreadMentionCount", alias="@type")
    chat_id: int
    unread_mention_count: int

    @staticmethod
    def read(q: dict) -> UpdateChatUnreadMentionCount:
        return UpdateChatUnreadMentionCount.construct(**q)


class UpdateChatVoiceChat(Update):
    """
    A chat voice chat state has changed
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        voice_chat (:class:`VoiceChat`)
            New value of voice_chat
        
    """

    ID: str = Field("updateChatVoiceChat", alias="@type")
    chat_id: int
    voice_chat: VoiceChat

    @staticmethod
    def read(q: dict) -> UpdateChatVoiceChat:
        return UpdateChatVoiceChat.construct(**q)


class UpdateConnectionState(Update):
    """
    The connection state has changed. This update must be used only to show a human-readable description of the connection state
    
    Params:
        state (:class:`ConnectionState`)
            The new connection state
        
    """

    ID: str = Field("updateConnectionState", alias="@type")
    state: ConnectionState

    @staticmethod
    def read(q: dict) -> UpdateConnectionState:
        return UpdateConnectionState.construct(**q)


class UpdateDeleteMessages(Update):
    """
    Some messages were deleted
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        message_ids (:obj:`list[int]`)
            Identifiers of the deleted messages
        
        is_permanent (:class:`bool`)
            True, if the messages are permanently deleted by a user (as opposed to just becoming inaccessible)
        
        from_cache (:class:`bool`)
            True, if the messages are deleted only from the cache and can possibly be retrieved again in the future
        
    """

    ID: str = Field("updateDeleteMessages", alias="@type")
    chat_id: int
    message_ids: list[int]
    is_permanent: bool
    from_cache: bool

    @staticmethod
    def read(q: dict) -> UpdateDeleteMessages:
        return UpdateDeleteMessages.construct(**q)


class UpdateDiceEmojis(Update):
    """
    The list of supported dice emojis has changed
    
    Params:
        emojis (:obj:`list[str]`)
            The new list of supported dice emojis
        
    """

    ID: str = Field("updateDiceEmojis", alias="@type")
    emojis: list[str]

    @staticmethod
    def read(q: dict) -> UpdateDiceEmojis:
        return UpdateDiceEmojis.construct(**q)


class UpdateFavoriteStickers(Update):
    """
    The list of favorite stickers was updated
    
    Params:
        sticker_ids (:obj:`list[int]`)
            The new list of file identifiers of favorite stickers
        
    """

    ID: str = Field("updateFavoriteStickers", alias="@type")
    sticker_ids: list[int]

    @staticmethod
    def read(q: dict) -> UpdateFavoriteStickers:
        return UpdateFavoriteStickers.construct(**q)


class UpdateFile(Update):
    """
    Information about a file was updated
    
    Params:
        file (:class:`File`)
            New data about the file
        
    """

    ID: str = Field("updateFile", alias="@type")
    file: File

    @staticmethod
    def read(q: dict) -> UpdateFile:
        return UpdateFile.construct(**q)


class UpdateFileGenerationStart(Update):
    """
    The file generation process needs to be started by the application
    
    Params:
        generation_id (:class:`int`)
            Unique identifier for the generation process
        
        original_path (:class:`str`)
            The path to a file from which a new file is generated; may be empty
        
        destination_path (:class:`str`)
            The path to a file that should be created and where the new file should be generated
        
        conversion (:class:`str`)
            String specifying the conversion applied to the original file. If conversion is "#url#" than original_path contains an HTTP/HTTPS URL of a file, which should be downloaded by the application
        
    """

    ID: str = Field("updateFileGenerationStart", alias="@type")
    generation_id: int
    original_path: str
    destination_path: str
    conversion: str

    @staticmethod
    def read(q: dict) -> UpdateFileGenerationStart:
        return UpdateFileGenerationStart.construct(**q)


class UpdateFileGenerationStop(Update):
    """
    File generation is no longer needed
    
    Params:
        generation_id (:class:`int`)
            Unique identifier for the generation process
        
    """

    ID: str = Field("updateFileGenerationStop", alias="@type")
    generation_id: int

    @staticmethod
    def read(q: dict) -> UpdateFileGenerationStop:
        return UpdateFileGenerationStop.construct(**q)


class UpdateGroupCall(Update):
    """
    Information about a group call was updated
    
    Params:
        group_call (:class:`GroupCall`)
            New data about a group call
        
    """

    ID: str = Field("updateGroupCall", alias="@type")
    group_call: GroupCall

    @staticmethod
    def read(q: dict) -> UpdateGroupCall:
        return UpdateGroupCall.construct(**q)


class UpdateGroupCallParticipant(Update):
    """
    Information about a group call participant was changed. The updates are sent only after the group call is received through getGroupCall and only if the call is joined or being joined
    
    Params:
        group_call_id (:class:`int`)
            Identifier of group call
        
        participant (:class:`GroupCallParticipant`)
            New data about a participant
        
    """

    ID: str = Field("updateGroupCallParticipant", alias="@type")
    group_call_id: int
    participant: GroupCallParticipant

    @staticmethod
    def read(q: dict) -> UpdateGroupCallParticipant:
        return UpdateGroupCallParticipant.construct(**q)


class UpdateHavePendingNotifications(Update):
    """
    Describes whether there are some pending notification updates. Can be used to prevent application from killing, while there are some pending notifications
    
    Params:
        have_delayed_notifications (:class:`bool`)
            True, if there are some delayed notification updates, which will be sent soon
        
        have_unreceived_notifications (:class:`bool`)
            True, if there can be some yet unreceived notifications, which are being fetched from the server
        
    """

    ID: str = Field("updateHavePendingNotifications", alias="@type")
    have_delayed_notifications: bool
    have_unreceived_notifications: bool

    @staticmethod
    def read(q: dict) -> UpdateHavePendingNotifications:
        return UpdateHavePendingNotifications.construct(**q)


class UpdateInstalledStickerSets(Update):
    """
    The list of installed sticker sets was updated
    
    Params:
        is_masks (:class:`bool`)
            True, if the list of installed mask sticker sets was updated
        
        sticker_set_ids (:obj:`list[int]`)
            The new list of installed ordinary sticker sets
        
    """

    ID: str = Field("updateInstalledStickerSets", alias="@type")
    is_masks: bool
    sticker_set_ids: list[int]

    @staticmethod
    def read(q: dict) -> UpdateInstalledStickerSets:
        return UpdateInstalledStickerSets.construct(**q)


class UpdateLanguagePackStrings(Update):
    """
    Some language pack strings have been updated
    
    Params:
        localization_target (:class:`str`)
            Localization target to which the language pack belongs
        
        language_pack_id (:class:`str`)
            Identifier of the updated language pack
        
        strings (:obj:`list[LanguagePackString]`)
            List of changed language pack strings
        
    """

    ID: str = Field("updateLanguagePackStrings", alias="@type")
    localization_target: str
    language_pack_id: str
    strings: list[LanguagePackString]

    @staticmethod
    def read(q: dict) -> UpdateLanguagePackStrings:
        return UpdateLanguagePackStrings.construct(**q)


class UpdateMessageContent(Update):
    """
    The message content has changed
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        message_id (:class:`int`)
            Message identifier
        
        new_content (:class:`MessageContent`)
            New message content
        
    """

    ID: str = Field("updateMessageContent", alias="@type")
    chat_id: int
    message_id: int
    new_content: MessageContent

    @staticmethod
    def read(q: dict) -> UpdateMessageContent:
        return UpdateMessageContent.construct(**q)


class UpdateMessageContentOpened(Update):
    """
    The message content was opened. Updates voice note messages to "listened", video note messages to "viewed" and starts the TTL timer for self-destructing messages
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        message_id (:class:`int`)
            Message identifier
        
    """

    ID: str = Field("updateMessageContentOpened", alias="@type")
    chat_id: int
    message_id: int

    @staticmethod
    def read(q: dict) -> UpdateMessageContentOpened:
        return UpdateMessageContentOpened.construct(**q)


class UpdateMessageEdited(Update):
    """
    A message was edited. Changes in the message content will come in a separate updateMessageContent
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        message_id (:class:`int`)
            Message identifier
        
        edit_date (:class:`int`)
            Point in time (Unix timestamp) when the message was edited
        
        reply_markup (:class:`ReplyMarkup`)
            New message reply markup; may be null
        
    """

    ID: str = Field("updateMessageEdited", alias="@type")
    chat_id: int
    message_id: int
    edit_date: int
    reply_markup: typing.Optional[ReplyMarkup] = None

    @staticmethod
    def read(q: dict) -> UpdateMessageEdited:
        return UpdateMessageEdited.construct(**q)


class UpdateMessageInteractionInfo(Update):
    """
    The information about interactions with a message has changed
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        message_id (:class:`int`)
            Message identifier
        
        interaction_info (:class:`MessageInteractionInfo`)
            New information about interactions with the message; may be null
        
    """

    ID: str = Field("updateMessageInteractionInfo", alias="@type")
    chat_id: int
    message_id: int
    interaction_info: typing.Optional[MessageInteractionInfo] = None

    @staticmethod
    def read(q: dict) -> UpdateMessageInteractionInfo:
        return UpdateMessageInteractionInfo.construct(**q)


class UpdateMessageIsPinned(Update):
    """
    The message pinned state was changed
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        message_id (:class:`int`)
            The message identifier
        
        is_pinned (:class:`bool`)
            True, if the message is pinned
        
    """

    ID: str = Field("updateMessageIsPinned", alias="@type")
    chat_id: int
    message_id: int
    is_pinned: bool

    @staticmethod
    def read(q: dict) -> UpdateMessageIsPinned:
        return UpdateMessageIsPinned.construct(**q)


class UpdateMessageLiveLocationViewed(Update):
    """
    A message with a live location was viewed. When the update is received, the application is supposed to update the live location
    
    Params:
        chat_id (:class:`int`)
            Identifier of the chat with the live location message
        
        message_id (:class:`int`)
            Identifier of the message with live location
        
    """

    ID: str = Field("updateMessageLiveLocationViewed", alias="@type")
    chat_id: int
    message_id: int

    @staticmethod
    def read(q: dict) -> UpdateMessageLiveLocationViewed:
        return UpdateMessageLiveLocationViewed.construct(**q)


class UpdateMessageMentionRead(Update):
    """
    A message with an unread mention was read
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        message_id (:class:`int`)
            Message identifier
        
        unread_mention_count (:class:`int`)
            The new number of unread mention messages left in the chat
        
    """

    ID: str = Field("updateMessageMentionRead", alias="@type")
    chat_id: int
    message_id: int
    unread_mention_count: int

    @staticmethod
    def read(q: dict) -> UpdateMessageMentionRead:
        return UpdateMessageMentionRead.construct(**q)


class UpdateMessageSendAcknowledged(Update):
    """
    A request to send a message has reached the Telegram server. This doesn't mean that the message will be sent successfully or even that the send message request will be processed. This update will be sent only if the option "use_quick_ack" is set to true. This update may be sent multiple times for the same message
    
    Params:
        chat_id (:class:`int`)
            The chat identifier of the sent message
        
        message_id (:class:`int`)
            A temporary message identifier
        
    """

    ID: str = Field("updateMessageSendAcknowledged", alias="@type")
    chat_id: int
    message_id: int

    @staticmethod
    def read(q: dict) -> UpdateMessageSendAcknowledged:
        return UpdateMessageSendAcknowledged.construct(**q)


class UpdateMessageSendFailed(Update):
    """
    A message failed to send. Be aware that some messages being sent can be irrecoverably deleted, in which case updateDeleteMessages will be received instead of this update
    
    Params:
        message (:class:`Message`)
            Contains information about the message which failed to send
        
        old_message_id (:class:`int`)
            The previous temporary message identifier
        
        error_code (:class:`int`)
            An error code
        
        error_message (:class:`str`)
            Error message
        
    """

    ID: str = Field("updateMessageSendFailed", alias="@type")
    message: Message
    old_message_id: int
    error_code: int
    error_message: str

    @staticmethod
    def read(q: dict) -> UpdateMessageSendFailed:
        return UpdateMessageSendFailed.construct(**q)


class UpdateMessageSendSucceeded(Update):
    """
    A message has been successfully sent
    
    Params:
        message (:class:`Message`)
            Information about the sent message. Usually only the message identifier, date, and content are changed, but almost all other fields can also change
        
        old_message_id (:class:`int`)
            The previous temporary message identifier
        
    """

    ID: str = Field("updateMessageSendSucceeded", alias="@type")
    message: Message
    old_message_id: int

    @staticmethod
    def read(q: dict) -> UpdateMessageSendSucceeded:
        return UpdateMessageSendSucceeded.construct(**q)


class UpdateNewCallSignalingData(Update):
    """
    New call signaling data arrived
    
    Params:
        call_id (:class:`int`)
            The call identifier
        
        data (:class:`str`)
            The data
        
    """

    ID: str = Field("updateNewCallSignalingData", alias="@type")
    call_id: int
    data: str

    @staticmethod
    def read(q: dict) -> UpdateNewCallSignalingData:
        return UpdateNewCallSignalingData.construct(**q)


class UpdateNewCallbackQuery(Update):
    """
    A new incoming callback query; for bots only
    
    Params:
        id (:class:`int`)
            Unique query identifier
        
        sender_user_id (:class:`int`)
            Identifier of the user who sent the query
        
        chat_id (:class:`int`)
            Identifier of the chat where the query was sent
        
        message_id (:class:`int`)
            Identifier of the message, from which the query originated
        
        chat_instance (:class:`int`)
            Identifier that uniquely corresponds to the chat to which the message was sent
        
        payload (:class:`CallbackQueryPayload`)
            Query payload
        
    """

    ID: str = Field("updateNewCallbackQuery", alias="@type")
    id: int
    sender_user_id: int
    chat_id: int
    message_id: int
    chat_instance: int
    payload: CallbackQueryPayload

    @staticmethod
    def read(q: dict) -> UpdateNewCallbackQuery:
        return UpdateNewCallbackQuery.construct(**q)


class UpdateNewChat(Update):
    """
    A new chat has been loaded/created. This update is guaranteed to come before the chat identifier is returned to the application. The chat field changes will be reported through separate updates
    
    Params:
        chat (:class:`Chat`)
            The chat
        
    """

    ID: str = Field("updateNewChat", alias="@type")
    chat: Chat

    @staticmethod
    def read(q: dict) -> UpdateNewChat:
        return UpdateNewChat.construct(**q)


class UpdateNewChosenInlineResult(Update):
    """
    The user has chosen a result of an inline query; for bots only
    
    Params:
        sender_user_id (:class:`int`)
            Identifier of the user who sent the query
        
        user_location (:class:`Location`)
            User location; may be null
        
        query (:class:`str`)
            Text of the query
        
        result_id (:class:`str`)
            Identifier of the chosen result
        
        inline_message_id (:class:`str`)
            Identifier of the sent inline message, if known
        
    """

    ID: str = Field("updateNewChosenInlineResult", alias="@type")
    sender_user_id: int
    user_location: typing.Optional[Location] = None
    query: str
    result_id: str
    inline_message_id: str

    @staticmethod
    def read(q: dict) -> UpdateNewChosenInlineResult:
        return UpdateNewChosenInlineResult.construct(**q)


class UpdateNewCustomEvent(Update):
    """
    A new incoming event; for bots only
    
    Params:
        event (:class:`str`)
            A JSON-serialized event
        
    """

    ID: str = Field("updateNewCustomEvent", alias="@type")
    event: str

    @staticmethod
    def read(q: dict) -> UpdateNewCustomEvent:
        return UpdateNewCustomEvent.construct(**q)


class UpdateNewCustomQuery(Update):
    """
    A new incoming query; for bots only
    
    Params:
        id (:class:`int`)
            The query identifier
        
        data (:class:`str`)
            JSON-serialized query data
        
        timeout (:class:`int`)
            Query timeout
        
    """

    ID: str = Field("updateNewCustomQuery", alias="@type")
    id: int
    data: str
    timeout: int

    @staticmethod
    def read(q: dict) -> UpdateNewCustomQuery:
        return UpdateNewCustomQuery.construct(**q)


class UpdateNewInlineCallbackQuery(Update):
    """
    A new incoming callback query from a message sent via a bot; for bots only
    
    Params:
        id (:class:`int`)
            Unique query identifier
        
        sender_user_id (:class:`int`)
            Identifier of the user who sent the query
        
        inline_message_id (:class:`str`)
            Identifier of the inline message, from which the query originated
        
        chat_instance (:class:`int`)
            An identifier uniquely corresponding to the chat a message was sent to
        
        payload (:class:`CallbackQueryPayload`)
            Query payload
        
    """

    ID: str = Field("updateNewInlineCallbackQuery", alias="@type")
    id: int
    sender_user_id: int
    inline_message_id: str
    chat_instance: int
    payload: CallbackQueryPayload

    @staticmethod
    def read(q: dict) -> UpdateNewInlineCallbackQuery:
        return UpdateNewInlineCallbackQuery.construct(**q)


class UpdateNewInlineQuery(Update):
    """
    A new incoming inline query; for bots only
    
    Params:
        id (:class:`int`)
            Unique query identifier
        
        sender_user_id (:class:`int`)
            Identifier of the user who sent the query
        
        user_location (:class:`Location`)
            User location; may be null
        
        chat_type (:class:`ChatType`)
            Contains information about the type of the chat, from which the query originated; may be null if unknown
        
        query (:class:`str`)
            Text of the query
        
        offset (:class:`str`)
            Offset of the first entry to return
        
    """

    ID: str = Field("updateNewInlineQuery", alias="@type")
    id: int
    sender_user_id: int
    user_location: typing.Optional[Location] = None
    chat_type: typing.Optional[ChatType] = None
    query: str
    offset: str

    @staticmethod
    def read(q: dict) -> UpdateNewInlineQuery:
        return UpdateNewInlineQuery.construct(**q)


class UpdateNewMessage(Update):
    """
    A new message was received; can also be an outgoing message
    
    Params:
        message (:class:`Message`)
            The new message
        
    """

    ID: str = Field("updateNewMessage", alias="@type")
    message: Message

    @staticmethod
    def read(q: dict) -> UpdateNewMessage:
        return UpdateNewMessage.construct(**q)


class UpdateNewPreCheckoutQuery(Update):
    """
    A new incoming pre-checkout query; for bots only. Contains full information about a checkout
    
    Params:
        id (:class:`int`)
            Unique query identifier
        
        sender_user_id (:class:`int`)
            Identifier of the user who sent the query
        
        currency (:class:`str`)
            Currency for the product price
        
        total_amount (:class:`int`)
            Total price for the product, in the minimal quantity of the currency
        
        invoice_payload (:class:`str`)
            Invoice payload
        
        shipping_option_id (:class:`str`)
            Identifier of a shipping option chosen by the user; may be empty if not applicable
        
        order_info (:class:`OrderInfo`)
            Information about the order; may be null
        
    """

    ID: str = Field("updateNewPreCheckoutQuery", alias="@type")
    id: int
    sender_user_id: int
    currency: str
    total_amount: int
    invoice_payload: str
    shipping_option_id: str
    order_info: typing.Optional[OrderInfo] = None

    @staticmethod
    def read(q: dict) -> UpdateNewPreCheckoutQuery:
        return UpdateNewPreCheckoutQuery.construct(**q)


class UpdateNewShippingQuery(Update):
    """
    A new incoming shipping query; for bots only. Only for invoices with flexible price
    
    Params:
        id (:class:`int`)
            Unique query identifier
        
        sender_user_id (:class:`int`)
            Identifier of the user who sent the query
        
        invoice_payload (:class:`str`)
            Invoice payload
        
        shipping_address (:class:`Address`)
            User shipping address
        
    """

    ID: str = Field("updateNewShippingQuery", alias="@type")
    id: int
    sender_user_id: int
    invoice_payload: str
    shipping_address: Address

    @staticmethod
    def read(q: dict) -> UpdateNewShippingQuery:
        return UpdateNewShippingQuery.construct(**q)


class UpdateNotification(Update):
    """
    A notification was changed
    
    Params:
        notification_group_id (:class:`int`)
            Unique notification group identifier
        
        notification (:class:`Notification`)
            Changed notification
        
    """

    ID: str = Field("updateNotification", alias="@type")
    notification_group_id: int
    notification: Notification

    @staticmethod
    def read(q: dict) -> UpdateNotification:
        return UpdateNotification.construct(**q)


class UpdateNotificationGroup(Update):
    """
    A list of active notifications in a notification group has changed
    
    Params:
        notification_group_id (:class:`int`)
            Unique notification group identifier
        
        type_ (:class:`NotificationGroupType`)
            New type of the notification group
        
        chat_id (:class:`int`)
            Identifier of a chat to which all notifications in the group belong
        
        notification_settings_chat_id (:class:`int`)
            Chat identifier, which notification settings must be applied to the added notifications
        
        is_silent (:class:`bool`)
            True, if the notifications should be shown without sound
        
        total_count (:class:`int`)
            Total number of unread notifications in the group, can be bigger than number of active notifications
        
        added_notifications (:obj:`list[Notification]`)
            List of added group notifications, sorted by notification ID
        
        removed_notification_ids (:obj:`list[int]`)
            Identifiers of removed group notifications, sorted by notification ID
        
    """

    ID: str = Field("updateNotificationGroup", alias="@type")
    notification_group_id: int
    type_: NotificationGroupType = Field(..., alias='type')
    chat_id: int
    notification_settings_chat_id: int
    is_silent: bool
    total_count: int
    added_notifications: list[Notification]
    removed_notification_ids: list[int]

    @staticmethod
    def read(q: dict) -> UpdateNotificationGroup:
        return UpdateNotificationGroup.construct(**q)


class UpdateOption(Update):
    """
    An option changed its value
    
    Params:
        name (:class:`str`)
            The option name
        
        value (:class:`OptionValue`)
            The new option value
        
    """

    ID: str = Field("updateOption", alias="@type")
    name: str
    value: OptionValue

    @staticmethod
    def read(q: dict) -> UpdateOption:
        return UpdateOption.construct(**q)


class UpdatePoll(Update):
    """
    A poll was updated; for bots only
    
    Params:
        poll (:class:`Poll`)
            New data about the poll
        
    """

    ID: str = Field("updatePoll", alias="@type")
    poll: Poll

    @staticmethod
    def read(q: dict) -> UpdatePoll:
        return UpdatePoll.construct(**q)


class UpdatePollAnswer(Update):
    """
    A user changed the answer to a poll; for bots only
    
    Params:
        poll_id (:class:`int`)
            Unique poll identifier
        
        user_id (:class:`int`)
            The user, who changed the answer to the poll
        
        option_ids (:obj:`list[int]`)
            0-based identifiers of answer options, chosen by the user
        
    """

    ID: str = Field("updatePollAnswer", alias="@type")
    poll_id: int
    user_id: int
    option_ids: list[int]

    @staticmethod
    def read(q: dict) -> UpdatePollAnswer:
        return UpdatePollAnswer.construct(**q)


class UpdateRecentStickers(Update):
    """
    The list of recently used stickers was updated
    
    Params:
        is_attached (:class:`bool`)
            True, if the list of stickers attached to photo or video files was updated, otherwise the list of sent stickers is updated
        
        sticker_ids (:obj:`list[int]`)
            The new list of file identifiers of recently used stickers
        
    """

    ID: str = Field("updateRecentStickers", alias="@type")
    is_attached: bool
    sticker_ids: list[int]

    @staticmethod
    def read(q: dict) -> UpdateRecentStickers:
        return UpdateRecentStickers.construct(**q)


class UpdateSavedAnimations(Update):
    """
    The list of saved animations was updated
    
    Params:
        animation_ids (:obj:`list[int]`)
            The new list of file identifiers of saved animations
        
    """

    ID: str = Field("updateSavedAnimations", alias="@type")
    animation_ids: list[int]

    @staticmethod
    def read(q: dict) -> UpdateSavedAnimations:
        return UpdateSavedAnimations.construct(**q)


class UpdateScopeNotificationSettings(Update):
    """
    Notification settings for some type of chats were updated
    
    Params:
        scope (:class:`NotificationSettingsScope`)
            Types of chats for which notification settings were updated
        
        notification_settings (:class:`ScopeNotificationSettings`)
            The new notification settings
        
    """

    ID: str = Field("updateScopeNotificationSettings", alias="@type")
    scope: NotificationSettingsScope
    notification_settings: ScopeNotificationSettings

    @staticmethod
    def read(q: dict) -> UpdateScopeNotificationSettings:
        return UpdateScopeNotificationSettings.construct(**q)


class UpdateSecretChat(Update):
    """
    Some data of a secret chat has changed. This update is guaranteed to come before the secret chat identifier is returned to the application
    
    Params:
        secret_chat (:class:`SecretChat`)
            New data about the secret chat
        
    """

    ID: str = Field("updateSecretChat", alias="@type")
    secret_chat: SecretChat

    @staticmethod
    def read(q: dict) -> UpdateSecretChat:
        return UpdateSecretChat.construct(**q)


class UpdateSelectedBackground(Update):
    """
    The selected background has changed
    
    Params:
        for_dark_theme (:class:`bool`)
            True, if background for dark theme has changed
        
        background (:class:`Background`)
            The new selected background; may be null
        
    """

    ID: str = Field("updateSelectedBackground", alias="@type")
    for_dark_theme: bool
    background: typing.Optional[Background] = None

    @staticmethod
    def read(q: dict) -> UpdateSelectedBackground:
        return UpdateSelectedBackground.construct(**q)


class UpdateServiceNotification(Update):
    """
    Service notification from the server. Upon receiving this the application must show a popup with the content of the notification
    
    Params:
        type_ (:class:`str`)
            Notification type. If type begins with "AUTH_KEY_DROP_", then two buttons "Cancel" and "Log out" should be shown under notification; if user presses the second, all local data should be destroyed using Destroy method
        
        content (:class:`MessageContent`)
            Notification content
        
    """

    ID: str = Field("updateServiceNotification", alias="@type")
    type_: str = Field(..., alias='type')
    content: MessageContent

    @staticmethod
    def read(q: dict) -> UpdateServiceNotification:
        return UpdateServiceNotification.construct(**q)


class UpdateStickerSet(Update):
    """
    A sticker set has changed
    
    Params:
        sticker_set (:class:`StickerSet`)
            The sticker set
        
    """

    ID: str = Field("updateStickerSet", alias="@type")
    sticker_set: StickerSet

    @staticmethod
    def read(q: dict) -> UpdateStickerSet:
        return UpdateStickerSet.construct(**q)


class UpdateSuggestedActions(Update):
    """
    The list of suggested to the user actions has changed
    
    Params:
        added_actions (:obj:`list[SuggestedAction]`)
            Added suggested actions
        
        removed_actions (:obj:`list[SuggestedAction]`)
            Removed suggested actions
        
    """

    ID: str = Field("updateSuggestedActions", alias="@type")
    added_actions: list[SuggestedAction]
    removed_actions: list[SuggestedAction]

    @staticmethod
    def read(q: dict) -> UpdateSuggestedActions:
        return UpdateSuggestedActions.construct(**q)


class UpdateSupergroup(Update):
    """
    Some data of a supergroup or a channel has changed. This update is guaranteed to come before the supergroup identifier is returned to the application
    
    Params:
        supergroup (:class:`Supergroup`)
            New data about the supergroup
        
    """

    ID: str = Field("updateSupergroup", alias="@type")
    supergroup: Supergroup

    @staticmethod
    def read(q: dict) -> UpdateSupergroup:
        return UpdateSupergroup.construct(**q)


class UpdateSupergroupFullInfo(Update):
    """
    Some data from supergroupFullInfo has been changed
    
    Params:
        supergroup_id (:class:`int`)
            Identifier of the supergroup or channel
        
        supergroup_full_info (:class:`SupergroupFullInfo`)
            New full information about the supergroup
        
    """

    ID: str = Field("updateSupergroupFullInfo", alias="@type")
    supergroup_id: int
    supergroup_full_info: SupergroupFullInfo

    @staticmethod
    def read(q: dict) -> UpdateSupergroupFullInfo:
        return UpdateSupergroupFullInfo.construct(**q)


class UpdateTermsOfService(Update):
    """
    New terms of service must be accepted by the user. If the terms of service are declined, then the deleteAccount method should be called with the reason "Decline ToS update"
    
    Params:
        terms_of_service_id (:class:`str`)
            Identifier of the terms of service
        
        terms_of_service (:class:`TermsOfService`)
            The new terms of service
        
    """

    ID: str = Field("updateTermsOfService", alias="@type")
    terms_of_service_id: str
    terms_of_service: TermsOfService

    @staticmethod
    def read(q: dict) -> UpdateTermsOfService:
        return UpdateTermsOfService.construct(**q)


class UpdateTrendingStickerSets(Update):
    """
    The list of trending sticker sets was updated or some of them were viewed
    
    Params:
        sticker_sets (:class:`StickerSets`)
            The prefix of the list of trending sticker sets with the newest trending sticker sets
        
    """

    ID: str = Field("updateTrendingStickerSets", alias="@type")
    sticker_sets: StickerSets

    @staticmethod
    def read(q: dict) -> UpdateTrendingStickerSets:
        return UpdateTrendingStickerSets.construct(**q)


class UpdateUnreadChatCount(Update):
    """
    Number of unread chats, i.e. with unread messages or marked as unread, has changed. This update is sent only if the message database is used
    
    Params:
        chat_list (:class:`ChatList`)
            The chat list with changed number of unread messages
        
        total_count (:class:`int`)
            Approximate total number of chats in the chat list
        
        unread_count (:class:`int`)
            Total number of unread chats
        
        unread_unmuted_count (:class:`int`)
            Total number of unread unmuted chats
        
        marked_as_unread_count (:class:`int`)
            Total number of chats marked as unread
        
        marked_as_unread_unmuted_count (:class:`int`)
            Total number of unmuted chats marked as unread
        
    """

    ID: str = Field("updateUnreadChatCount", alias="@type")
    chat_list: ChatList
    total_count: int
    unread_count: int
    unread_unmuted_count: int
    marked_as_unread_count: int
    marked_as_unread_unmuted_count: int

    @staticmethod
    def read(q: dict) -> UpdateUnreadChatCount:
        return UpdateUnreadChatCount.construct(**q)


class UpdateUnreadMessageCount(Update):
    """
    Number of unread messages in a chat list has changed. This update is sent only if the message database is used
    
    Params:
        chat_list (:class:`ChatList`)
            The chat list with changed number of unread messages
        
        unread_count (:class:`int`)
            Total number of unread messages
        
        unread_unmuted_count (:class:`int`)
            Total number of unread messages in unmuted chats
        
    """

    ID: str = Field("updateUnreadMessageCount", alias="@type")
    chat_list: ChatList
    unread_count: int
    unread_unmuted_count: int

    @staticmethod
    def read(q: dict) -> UpdateUnreadMessageCount:
        return UpdateUnreadMessageCount.construct(**q)


class UpdateUser(Update):
    """
    Some data of a user has changed. This update is guaranteed to come before the user identifier is returned to the application
    
    Params:
        user (:class:`User`)
            New data about the user
        
    """

    ID: str = Field("updateUser", alias="@type")
    user: User

    @staticmethod
    def read(q: dict) -> UpdateUser:
        return UpdateUser.construct(**q)


class UpdateUserChatAction(Update):
    """
    User activity in the chat has changed
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        message_thread_id (:class:`int`)
            If not 0, a message thread identifier in which the action was performed
        
        user_id (:class:`int`)
            Identifier of a user performing an action
        
        action (:class:`ChatAction`)
            The action description
        
    """

    ID: str = Field("updateUserChatAction", alias="@type")
    chat_id: int
    message_thread_id: int
    user_id: int
    action: ChatAction

    @staticmethod
    def read(q: dict) -> UpdateUserChatAction:
        return UpdateUserChatAction.construct(**q)


class UpdateUserFullInfo(Update):
    """
    Some data from userFullInfo has been changed
    
    Params:
        user_id (:class:`int`)
            User identifier
        
        user_full_info (:class:`UserFullInfo`)
            New full information about the user
        
    """

    ID: str = Field("updateUserFullInfo", alias="@type")
    user_id: int
    user_full_info: UserFullInfo

    @staticmethod
    def read(q: dict) -> UpdateUserFullInfo:
        return UpdateUserFullInfo.construct(**q)


class UpdateUserPrivacySettingRules(Update):
    """
    Some privacy setting rules have been changed
    
    Params:
        setting (:class:`UserPrivacySetting`)
            The privacy setting
        
        rules (:class:`UserPrivacySettingRules`)
            New privacy rules
        
    """

    ID: str = Field("updateUserPrivacySettingRules", alias="@type")
    setting: UserPrivacySetting
    rules: UserPrivacySettingRules

    @staticmethod
    def read(q: dict) -> UpdateUserPrivacySettingRules:
        return UpdateUserPrivacySettingRules.construct(**q)


class UpdateUserStatus(Update):
    """
    The user went online or offline
    
    Params:
        user_id (:class:`int`)
            User identifier
        
        status (:class:`UserStatus`)
            New status of the user
        
    """

    ID: str = Field("updateUserStatus", alias="@type")
    user_id: int
    status: UserStatus

    @staticmethod
    def read(q: dict) -> UpdateUserStatus:
        return UpdateUserStatus.construct(**q)


class UpdateUsersNearby(Update):
    """
    The list of users nearby has changed. The update is guaranteed to be sent only 60 seconds after a successful searchChatsNearby request
    
    Params:
        users_nearby (:obj:`list[ChatNearby]`)
            The new list of users nearby
        
    """

    ID: str = Field("updateUsersNearby", alias="@type")
    users_nearby: list[ChatNearby]

    @staticmethod
    def read(q: dict) -> UpdateUsersNearby:
        return UpdateUsersNearby.construct(**q)
