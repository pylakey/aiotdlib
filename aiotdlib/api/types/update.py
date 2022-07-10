# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .address import Address
from .attachment_menu_bot import AttachmentMenuBot
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
from .chat_join_request import ChatJoinRequest
from .chat_join_requests_info import ChatJoinRequestsInfo
from .chat_list import ChatList
from .chat_member import ChatMember
from .chat_nearby import ChatNearby
from .chat_notification_settings import ChatNotificationSettings
from .chat_permissions import ChatPermissions
from .chat_photo_info import ChatPhotoInfo
from .chat_position import ChatPosition
from .chat_theme import ChatTheme
from .chat_type import ChatType
from .connection_state import ConnectionState
from .downloaded_file_counts import DownloadedFileCounts
from .draft_message import DraftMessage
from .file import File
from .file_download import FileDownload
from .group_call import GroupCall
from .group_call_participant import GroupCallParticipant
from .language_pack_string import LanguagePackString
from .location import Location
from .message import Message
from .message_content import MessageContent
from .message_interaction_info import MessageInteractionInfo
from .message_sender import MessageSender
from .notification import Notification
from .notification_group import NotificationGroup
from .notification_group_type import NotificationGroupType
from .notification_settings_scope import NotificationSettingsScope
from .option_value import OptionValue
from .order_info import OrderInfo
from .poll import Poll
from .reaction import Reaction
from .reply_markup import ReplyMarkup
from .scope_notification_settings import ScopeNotificationSettings
from .secret_chat import SecretChat
from .sticker import Sticker
from .sticker_set import StickerSet
from .suggested_action import SuggestedAction
from .supergroup import Supergroup
from .supergroup_full_info import SupergroupFullInfo
from .terms_of_service import TermsOfService
from .trending_sticker_sets import TrendingStickerSets
from .unread_reaction import UnreadReaction
from .user import User
from .user_full_info import UserFullInfo
from .user_privacy_setting import UserPrivacySetting
from .user_privacy_setting_rules import UserPrivacySettingRules
from .user_status import UserStatus
from .video_chat import VideoChat
from ..base_object import BaseObject


class Update(BaseObject):
    """
    Contains notifications about data changes
    
    """

    ID: str = Field("update", alias="@type")


class UpdateActiveNotifications(Update):
    """
    Contains active notifications that was shown on previous application launches. This update is sent only if the message database is used. In that case it comes once before any updateNotification and updateNotificationGroup update
    
    :param groups: Lists of active notification groups
    :type groups: :class:`list[NotificationGroup]`
    
    """

    ID: str = Field("updateActiveNotifications", alias="@type")
    groups: list[NotificationGroup]

    @staticmethod
    def read(q: dict) -> UpdateActiveNotifications:
        return UpdateActiveNotifications.construct(**q)


class UpdateAnimatedEmojiMessageClicked(Update):
    """
    Some animated emoji message was clicked and a big animated sticker must be played if the message is visible on the screen. chatActionWatchingAnimations with the text of the message needs to be sent if the sticker is played
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param message_id: Message identifier
    :type message_id: :class:`int`
    
    :param sticker: The animated sticker to be played
    :type sticker: :class:`Sticker`
    
    """

    ID: str = Field("updateAnimatedEmojiMessageClicked", alias="@type")
    chat_id: int
    message_id: int
    sticker: Sticker

    @staticmethod
    def read(q: dict) -> UpdateAnimatedEmojiMessageClicked:
        return UpdateAnimatedEmojiMessageClicked.construct(**q)


class UpdateAnimationSearchParameters(Update):
    """
    The parameters of animation search through GetOption("animation_search_bot_username") bot has changed
    
    :param provider: Name of the animation search provider
    :type provider: :class:`str`
    
    :param emojis: The new list of emojis suggested for searching
    :type emojis: :class:`list[str]`
    
    """

    ID: str = Field("updateAnimationSearchParameters", alias="@type")
    provider: str
    emojis: list[str]

    @staticmethod
    def read(q: dict) -> UpdateAnimationSearchParameters:
        return UpdateAnimationSearchParameters.construct(**q)


class UpdateAttachmentMenuBots(Update):
    """
    The list of bots added to attachment menu has changed
    
    :param bots: The new list of bots added to attachment menu. The bots must not be shown on scheduled messages screen
    :type bots: :class:`list[AttachmentMenuBot]`
    
    """

    ID: str = Field("updateAttachmentMenuBots", alias="@type")
    bots: list[AttachmentMenuBot]

    @staticmethod
    def read(q: dict) -> UpdateAttachmentMenuBots:
        return UpdateAttachmentMenuBots.construct(**q)


class UpdateAuthorizationState(Update):
    """
    The user authorization state has changed
    
    :param authorization_state: New authorization state
    :type authorization_state: :class:`AuthorizationState`
    
    """

    ID: str = Field("updateAuthorizationState", alias="@type")
    authorization_state: AuthorizationState

    @staticmethod
    def read(q: dict) -> UpdateAuthorizationState:
        return UpdateAuthorizationState.construct(**q)


class UpdateBasicGroup(Update):
    """
    Some data of a basic group has changed. This update is guaranteed to come before the basic group identifier is returned to the application
    
    :param basic_group: New data about the group
    :type basic_group: :class:`BasicGroup`
    
    """

    ID: str = Field("updateBasicGroup", alias="@type")
    basic_group: BasicGroup

    @staticmethod
    def read(q: dict) -> UpdateBasicGroup:
        return UpdateBasicGroup.construct(**q)


class UpdateBasicGroupFullInfo(Update):
    """
    Some data in basicGroupFullInfo has been changed
    
    :param basic_group_id: Identifier of a basic group
    :type basic_group_id: :class:`int`
    
    :param basic_group_full_info: New full information about the group
    :type basic_group_full_info: :class:`BasicGroupFullInfo`
    
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
    
    :param call: New data about a call
    :type call: :class:`Call`
    
    """

    ID: str = Field("updateCall", alias="@type")
    call: Call

    @staticmethod
    def read(q: dict) -> UpdateCall:
        return UpdateCall.construct(**q)


class UpdateChatAction(Update):
    """
    A message sender activity in the chat has changed
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param message_thread_id: If not 0, a message thread identifier in which the action was performed
    :type message_thread_id: :class:`int`
    
    :param sender_id: Identifier of a message sender performing the action
    :type sender_id: :class:`MessageSender`
    
    :param action: The action
    :type action: :class:`ChatAction`
    
    """

    ID: str = Field("updateChatAction", alias="@type")
    chat_id: int
    message_thread_id: int
    sender_id: MessageSender
    action: ChatAction

    @staticmethod
    def read(q: dict) -> UpdateChatAction:
        return UpdateChatAction.construct(**q)


class UpdateChatActionBar(Update):
    """
    The chat action bar was changed
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param action_bar: The new value of the action bar; may be null, defaults to None
    :type action_bar: :class:`ChatActionBar`, optional
    
    """

    ID: str = Field("updateChatActionBar", alias="@type")
    chat_id: int
    action_bar: typing.Optional[ChatActionBar] = None

    @staticmethod
    def read(q: dict) -> UpdateChatActionBar:
        return UpdateChatActionBar.construct(**q)


class UpdateChatAvailableReactions(Update):
    """
    The chat available reactions were changed
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param available_reactions: The new list of reactions, available in the chat
    :type available_reactions: :class:`list[str]`
    
    """

    ID: str = Field("updateChatAvailableReactions", alias="@type")
    chat_id: int
    available_reactions: list[str]

    @staticmethod
    def read(q: dict) -> UpdateChatAvailableReactions:
        return UpdateChatAvailableReactions.construct(**q)


class UpdateChatDefaultDisableNotification(Update):
    """
    The value of the default disable_notification parameter, used when a message is sent to the chat, was changed
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param default_disable_notification: The new default_disable_notification value
    :type default_disable_notification: :class:`bool`
    
    """

    ID: str = Field("updateChatDefaultDisableNotification", alias="@type")
    chat_id: int
    default_disable_notification: bool

    @staticmethod
    def read(q: dict) -> UpdateChatDefaultDisableNotification:
        return UpdateChatDefaultDisableNotification.construct(**q)


class UpdateChatDraftMessage(Update):
    """
    A chat draft has changed. Be aware that the update may come in the currently opened chat but with old content of the draft. If the user has changed the content of the draft, this update mustn't be applied
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param draft_message: The new draft message; may be null, defaults to None
    :type draft_message: :class:`DraftMessage`, optional
    
    :param positions: The new chat positions in the chat lists
    :type positions: :class:`list[ChatPosition]`
    
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
    
    :param chat_filters: The new list of chat filters
    :type chat_filters: :class:`list[ChatFilterInfo]`
    
    :param main_chat_list_position: Position of the main chat list among chat filters, 0-based
    :type main_chat_list_position: :class:`int`
    
    """

    ID: str = Field("updateChatFilters", alias="@type")
    chat_filters: list[ChatFilterInfo]
    main_chat_list_position: int

    @staticmethod
    def read(q: dict) -> UpdateChatFilters:
        return UpdateChatFilters.construct(**q)


class UpdateChatHasProtectedContent(Update):
    """
    A chat content was allowed or restricted for saving
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param has_protected_content: New value of has_protected_content
    :type has_protected_content: :class:`bool`
    
    """

    ID: str = Field("updateChatHasProtectedContent", alias="@type")
    chat_id: int
    has_protected_content: bool

    @staticmethod
    def read(q: dict) -> UpdateChatHasProtectedContent:
        return UpdateChatHasProtectedContent.construct(**q)


class UpdateChatHasScheduledMessages(Update):
    """
    A chat's has_scheduled_messages field has changed
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param has_scheduled_messages: New value of has_scheduled_messages
    :type has_scheduled_messages: :class:`bool`
    
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
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param is_blocked: New value of is_blocked
    :type is_blocked: :class:`bool`
    
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
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param is_marked_as_unread: New value of is_marked_as_unread
    :type is_marked_as_unread: :class:`bool`
    
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
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param last_message: The new last message in the chat; may be null, defaults to None
    :type last_message: :class:`Message`, optional
    
    :param positions: The new chat positions in the chat lists
    :type positions: :class:`list[ChatPosition]`
    
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
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param actor_user_id: Identifier of the user, changing the rights
    :type actor_user_id: :class:`int`
    
    :param date: Point in time (Unix timestamp) when the user rights was changed
    :type date: :class:`int`
    
    :param invite_link: If user has joined the chat using an invite link, the invite link; may be null, defaults to None
    :type invite_link: :class:`ChatInviteLink`, optional
    
    :param old_chat_member: Previous chat member
    :type old_chat_member: :class:`ChatMember`
    
    :param new_chat_member: New chat member
    :type new_chat_member: :class:`ChatMember`
    
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


class UpdateChatMessageSender(Update):
    """
    The message sender that is selected to send messages in a chat has changed
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param message_sender_id: New value of message_sender_id; may be null if the user can't change message sender, defaults to None
    :type message_sender_id: :class:`MessageSender`, optional
    
    """

    ID: str = Field("updateChatMessageSender", alias="@type")
    chat_id: int
    message_sender_id: typing.Optional[MessageSender] = None

    @staticmethod
    def read(q: dict) -> UpdateChatMessageSender:
        return UpdateChatMessageSender.construct(**q)


class UpdateChatMessageTtl(Update):
    """
    The message Time To Live setting for a chat was changed
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param message_ttl: New value of message_ttl
    :type message_ttl: :class:`int`
    
    """

    ID: str = Field("updateChatMessageTtl", alias="@type")
    chat_id: int
    message_ttl: int

    @staticmethod
    def read(q: dict) -> UpdateChatMessageTtl:
        return UpdateChatMessageTtl.construct(**q)


class UpdateChatNotificationSettings(Update):
    """
    Notification settings for a chat were changed
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param notification_settings: The new notification settings
    :type notification_settings: :class:`ChatNotificationSettings`
    
    """

    ID: str = Field("updateChatNotificationSettings", alias="@type")
    chat_id: int
    notification_settings: ChatNotificationSettings

    @staticmethod
    def read(q: dict) -> UpdateChatNotificationSettings:
        return UpdateChatNotificationSettings.construct(**q)


class UpdateChatOnlineMemberCount(Update):
    """
    The number of online group members has changed. This update with non-zero number of online group members is sent only for currently opened chats. There is no guarantee that it will be sent just after the number of online users has changed
    
    :param chat_id: Identifier of the chat
    :type chat_id: :class:`int`
    
    :param online_member_count: New number of online members in the chat, or 0 if unknown
    :type online_member_count: :class:`int`
    
    """

    ID: str = Field("updateChatOnlineMemberCount", alias="@type")
    chat_id: int
    online_member_count: int

    @staticmethod
    def read(q: dict) -> UpdateChatOnlineMemberCount:
        return UpdateChatOnlineMemberCount.construct(**q)


class UpdateChatPendingJoinRequests(Update):
    """
    The chat pending join requests were changed
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param pending_join_requests: The new data about pending join requests; may be null, defaults to None
    :type pending_join_requests: :class:`ChatJoinRequestsInfo`, optional
    
    """

    ID: str = Field("updateChatPendingJoinRequests", alias="@type")
    chat_id: int
    pending_join_requests: typing.Optional[ChatJoinRequestsInfo] = None

    @staticmethod
    def read(q: dict) -> UpdateChatPendingJoinRequests:
        return UpdateChatPendingJoinRequests.construct(**q)


class UpdateChatPermissions(Update):
    """
    Chat permissions was changed
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param permissions: The new chat permissions
    :type permissions: :class:`ChatPermissions`
    
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
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param photo: The new chat photo; may be null, defaults to None
    :type photo: :class:`ChatPhotoInfo`, optional
    
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
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param position: New chat position. If new order is 0, then the chat needs to be removed from the list
    :type position: :class:`ChatPosition`
    
    """

    ID: str = Field("updateChatPosition", alias="@type")
    chat_id: int
    position: ChatPosition

    @staticmethod
    def read(q: dict) -> UpdateChatPosition:
        return UpdateChatPosition.construct(**q)


class UpdateChatReadInbox(Update):
    """
    Incoming messages were read or the number of unread messages has been changed
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param last_read_inbox_message_id: Identifier of the last read incoming message
    :type last_read_inbox_message_id: :class:`int`
    
    :param unread_count: The number of unread messages left in the chat
    :type unread_count: :class:`int`
    
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
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param last_read_outbox_message_id: Identifier of last read outgoing message
    :type last_read_outbox_message_id: :class:`int`
    
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
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param reply_markup_message_id: Identifier of the message from which reply markup needs to be used; 0 if there is no default custom reply markup in the chat
    :type reply_markup_message_id: :class:`int`
    
    """

    ID: str = Field("updateChatReplyMarkup", alias="@type")
    chat_id: int
    reply_markup_message_id: int

    @staticmethod
    def read(q: dict) -> UpdateChatReplyMarkup:
        return UpdateChatReplyMarkup.construct(**q)


class UpdateChatTheme(Update):
    """
    The chat theme was changed
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param theme_name: The new name of the chat theme; may be empty if theme was reset to default
    :type theme_name: :class:`str`
    
    """

    ID: str = Field("updateChatTheme", alias="@type")
    chat_id: int
    theme_name: str

    @staticmethod
    def read(q: dict) -> UpdateChatTheme:
        return UpdateChatTheme.construct(**q)


class UpdateChatThemes(Update):
    """
    The list of available chat themes has changed
    
    :param chat_themes: The new list of chat themes
    :type chat_themes: :class:`list[ChatTheme]`
    
    """

    ID: str = Field("updateChatThemes", alias="@type")
    chat_themes: list[ChatTheme]

    @staticmethod
    def read(q: dict) -> UpdateChatThemes:
        return UpdateChatThemes.construct(**q)


class UpdateChatTitle(Update):
    """
    The title of a chat was changed
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param title: The new chat title
    :type title: :class:`str`
    
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
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param unread_mention_count: The number of unread mention messages left in the chat
    :type unread_mention_count: :class:`int`
    
    """

    ID: str = Field("updateChatUnreadMentionCount", alias="@type")
    chat_id: int
    unread_mention_count: int

    @staticmethod
    def read(q: dict) -> UpdateChatUnreadMentionCount:
        return UpdateChatUnreadMentionCount.construct(**q)


class UpdateChatUnreadReactionCount(Update):
    """
    The chat unread_reaction_count has changed
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param unread_reaction_count: The number of messages with unread reactions left in the chat
    :type unread_reaction_count: :class:`int`
    
    """

    ID: str = Field("updateChatUnreadReactionCount", alias="@type")
    chat_id: int
    unread_reaction_count: int

    @staticmethod
    def read(q: dict) -> UpdateChatUnreadReactionCount:
        return UpdateChatUnreadReactionCount.construct(**q)


class UpdateChatVideoChat(Update):
    """
    A chat video chat state has changed
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param video_chat: New value of video_chat
    :type video_chat: :class:`VideoChat`
    
    """

    ID: str = Field("updateChatVideoChat", alias="@type")
    chat_id: int
    video_chat: VideoChat

    @staticmethod
    def read(q: dict) -> UpdateChatVideoChat:
        return UpdateChatVideoChat.construct(**q)


class UpdateConnectionState(Update):
    """
    The connection state has changed. This update must be used only to show a human-readable description of the connection state
    
    :param state: The new connection state
    :type state: :class:`ConnectionState`
    
    """

    ID: str = Field("updateConnectionState", alias="@type")
    state: ConnectionState

    @staticmethod
    def read(q: dict) -> UpdateConnectionState:
        return UpdateConnectionState.construct(**q)


class UpdateDeleteMessages(Update):
    """
    Some messages were deleted
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param message_ids: Identifiers of the deleted messages
    :type message_ids: :class:`list[int]`
    
    :param is_permanent: True, if the messages are permanently deleted by a user (as opposed to just becoming inaccessible)
    :type is_permanent: :class:`bool`
    
    :param from_cache: True, if the messages are deleted only from the cache and can possibly be retrieved again in the future
    :type from_cache: :class:`bool`
    
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
    
    :param emojis: The new list of supported dice emojis
    :type emojis: :class:`list[str]`
    
    """

    ID: str = Field("updateDiceEmojis", alias="@type")
    emojis: list[str]

    @staticmethod
    def read(q: dict) -> UpdateDiceEmojis:
        return UpdateDiceEmojis.construct(**q)


class UpdateFavoriteStickers(Update):
    """
    The list of favorite stickers was updated
    
    :param sticker_ids: The new list of file identifiers of favorite stickers
    :type sticker_ids: :class:`list[int]`
    
    """

    ID: str = Field("updateFavoriteStickers", alias="@type")
    sticker_ids: list[int]

    @staticmethod
    def read(q: dict) -> UpdateFavoriteStickers:
        return UpdateFavoriteStickers.construct(**q)


class UpdateFile(Update):
    """
    Information about a file was updated
    
    :param file: New data about the file
    :type file: :class:`File`
    
    """

    ID: str = Field("updateFile", alias="@type")
    file: File

    @staticmethod
    def read(q: dict) -> UpdateFile:
        return UpdateFile.construct(**q)


class UpdateFileAddedToDownloads(Update):
    """
    A file was added to the file download list. This update is sent only after file download list is loaded for the first time
    
    :param file_download: The added file download
    :type file_download: :class:`FileDownload`
    
    :param counts: New number of being downloaded and recently downloaded files found
    :type counts: :class:`DownloadedFileCounts`
    
    """

    ID: str = Field("updateFileAddedToDownloads", alias="@type")
    file_download: FileDownload
    counts: DownloadedFileCounts

    @staticmethod
    def read(q: dict) -> UpdateFileAddedToDownloads:
        return UpdateFileAddedToDownloads.construct(**q)


class UpdateFileDownload(Update):
    """
    A file download was changed. This update is sent only after file download list is loaded for the first time
    
    :param file_id: File identifier
    :type file_id: :class:`int`
    
    :param complete_date: Point in time (Unix timestamp) when the file downloading was completed; 0 if the file downloading isn't completed
    :type complete_date: :class:`int`
    
    :param is_paused: True, if downloading of the file is paused
    :type is_paused: :class:`bool`
    
    :param counts: New number of being downloaded and recently downloaded files found
    :type counts: :class:`DownloadedFileCounts`
    
    """

    ID: str = Field("updateFileDownload", alias="@type")
    file_id: int
    complete_date: int
    is_paused: bool
    counts: DownloadedFileCounts

    @staticmethod
    def read(q: dict) -> UpdateFileDownload:
        return UpdateFileDownload.construct(**q)


class UpdateFileDownloads(Update):
    """
    The state of the file download list has changed
    
    :param total_size: Total size of files in the file download list, in bytes
    :type total_size: :class:`int`
    
    :param total_count: Total number of files in the file download list
    :type total_count: :class:`int`
    
    :param downloaded_size: Total downloaded size of files in the file download list, in bytes
    :type downloaded_size: :class:`int`
    
    """

    ID: str = Field("updateFileDownloads", alias="@type")
    total_size: int
    total_count: int
    downloaded_size: int

    @staticmethod
    def read(q: dict) -> UpdateFileDownloads:
        return UpdateFileDownloads.construct(**q)


class UpdateFileGenerationStart(Update):
    """
    The file generation process needs to be started by the application
    
    :param generation_id: Unique identifier for the generation process
    :type generation_id: :class:`int`
    
    :param original_path: The path to a file from which a new file is generated; may be empty
    :type original_path: :class:`str`
    
    :param destination_path: The path to a file that must be created and where the new file is generated
    :type destination_path: :class:`str`
    
    :param conversion: String specifying the conversion applied to the original file. If conversion is "#url#" than original_path contains an HTTP/HTTPS URL of a file, which must be downloaded by the application
    :type conversion: :class:`str`
    
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
    
    :param generation_id: Unique identifier for the generation process
    :type generation_id: :class:`int`
    
    """

    ID: str = Field("updateFileGenerationStop", alias="@type")
    generation_id: int

    @staticmethod
    def read(q: dict) -> UpdateFileGenerationStop:
        return UpdateFileGenerationStop.construct(**q)


class UpdateFileRemovedFromDownloads(Update):
    """
    A file was removed from the file download list. This update is sent only after file download list is loaded for the first time
    
    :param file_id: File identifier
    :type file_id: :class:`int`
    
    :param counts: New number of being downloaded and recently downloaded files found
    :type counts: :class:`DownloadedFileCounts`
    
    """

    ID: str = Field("updateFileRemovedFromDownloads", alias="@type")
    file_id: int
    counts: DownloadedFileCounts

    @staticmethod
    def read(q: dict) -> UpdateFileRemovedFromDownloads:
        return UpdateFileRemovedFromDownloads.construct(**q)


class UpdateGroupCall(Update):
    """
    Information about a group call was updated
    
    :param group_call: New data about a group call
    :type group_call: :class:`GroupCall`
    
    """

    ID: str = Field("updateGroupCall", alias="@type")
    group_call: GroupCall

    @staticmethod
    def read(q: dict) -> UpdateGroupCall:
        return UpdateGroupCall.construct(**q)


class UpdateGroupCallParticipant(Update):
    """
    Information about a group call participant was changed. The updates are sent only after the group call is received through getGroupCall and only if the call is joined or being joined
    
    :param group_call_id: Identifier of group call
    :type group_call_id: :class:`int`
    
    :param participant: New data about a participant
    :type participant: :class:`GroupCallParticipant`
    
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
    
    :param have_delayed_notifications: True, if there are some delayed notification updates, which will be sent soon
    :type have_delayed_notifications: :class:`bool`
    
    :param have_unreceived_notifications: True, if there can be some yet unreceived notifications, which are being fetched from the server
    :type have_unreceived_notifications: :class:`bool`
    
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
    
    :param is_masks: True, if the list of installed mask sticker sets was updated
    :type is_masks: :class:`bool`
    
    :param sticker_set_ids: The new list of installed ordinary sticker sets
    :type sticker_set_ids: :class:`list[int]`
    
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
    
    :param localization_target: Localization target to which the language pack belongs
    :type localization_target: :class:`str`
    
    :param language_pack_id: Identifier of the updated language pack
    :type language_pack_id: :class:`str`
    
    :param strings: List of changed language pack strings
    :type strings: :class:`list[LanguagePackString]`
    
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
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param message_id: Message identifier
    :type message_id: :class:`int`
    
    :param new_content: New message content
    :type new_content: :class:`MessageContent`
    
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
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param message_id: Message identifier
    :type message_id: :class:`int`
    
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
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param message_id: Message identifier
    :type message_id: :class:`int`
    
    :param edit_date: Point in time (Unix timestamp) when the message was edited
    :type edit_date: :class:`int`
    
    :param reply_markup: New message reply markup; may be null, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    
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
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param message_id: Message identifier
    :type message_id: :class:`int`
    
    :param interaction_info: New information about interactions with the message; may be null, defaults to None
    :type interaction_info: :class:`MessageInteractionInfo`, optional
    
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
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param message_id: The message identifier
    :type message_id: :class:`int`
    
    :param is_pinned: True, if the message is pinned
    :type is_pinned: :class:`bool`
    
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
    
    :param chat_id: Identifier of the chat with the live location message
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the message with live location
    :type message_id: :class:`int`
    
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
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param message_id: Message identifier
    :type message_id: :class:`int`
    
    :param unread_mention_count: The new number of unread mention messages left in the chat
    :type unread_mention_count: :class:`int`
    
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
    
    :param chat_id: The chat identifier of the sent message
    :type chat_id: :class:`int`
    
    :param message_id: A temporary message identifier
    :type message_id: :class:`int`
    
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
    
    :param message: The failed to send message
    :type message: :class:`Message`
    
    :param old_message_id: The previous temporary message identifier
    :type old_message_id: :class:`int`
    
    :param error_code: An error code
    :type error_code: :class:`int`
    
    :param error_message: Error message
    :type error_message: :class:`str`
    
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
    
    :param message: The sent message. Usually only the message identifier, date, and content are changed, but almost all other fields can also change
    :type message: :class:`Message`
    
    :param old_message_id: The previous temporary message identifier
    :type old_message_id: :class:`int`
    
    """

    ID: str = Field("updateMessageSendSucceeded", alias="@type")
    message: Message
    old_message_id: int

    @staticmethod
    def read(q: dict) -> UpdateMessageSendSucceeded:
        return UpdateMessageSendSucceeded.construct(**q)


class UpdateMessageUnreadReactions(Update):
    """
    The list of unread reactions added to a message was changed
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param message_id: Message identifier
    :type message_id: :class:`int`
    
    :param unread_reactions: The new list of unread reactions
    :type unread_reactions: :class:`list[UnreadReaction]`
    
    :param unread_reaction_count: The new number of messages with unread reactions left in the chat
    :type unread_reaction_count: :class:`int`
    
    """

    ID: str = Field("updateMessageUnreadReactions", alias="@type")
    chat_id: int
    message_id: int
    unread_reactions: list[UnreadReaction]
    unread_reaction_count: int

    @staticmethod
    def read(q: dict) -> UpdateMessageUnreadReactions:
        return UpdateMessageUnreadReactions.construct(**q)


class UpdateNewCallSignalingData(Update):
    """
    New call signaling data arrived
    
    :param call_id: The call identifier
    :type call_id: :class:`int`
    
    :param data: The data
    :type data: :class:`str`
    
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
    
    :param id: Unique query identifier
    :type id: :class:`int`
    
    :param sender_user_id: Identifier of the user who sent the query
    :type sender_user_id: :class:`int`
    
    :param chat_id: Identifier of the chat where the query was sent
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the message from which the query originated
    :type message_id: :class:`int`
    
    :param chat_instance: Identifier that uniquely corresponds to the chat to which the message was sent
    :type chat_instance: :class:`int`
    
    :param payload: Query payload
    :type payload: :class:`CallbackQueryPayload`
    
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
    
    :param chat: The chat
    :type chat: :class:`Chat`
    
    """

    ID: str = Field("updateNewChat", alias="@type")
    chat: Chat

    @staticmethod
    def read(q: dict) -> UpdateNewChat:
        return UpdateNewChat.construct(**q)


class UpdateNewChatJoinRequest(Update):
    """
    A user sent a join request to a chat; for bots only
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param request: Join request
    :type request: :class:`ChatJoinRequest`
    
    :param invite_link: The invite link, which was used to send join request; may be null, defaults to None
    :type invite_link: :class:`ChatInviteLink`, optional
    
    """

    ID: str = Field("updateNewChatJoinRequest", alias="@type")
    chat_id: int
    request: ChatJoinRequest
    invite_link: typing.Optional[ChatInviteLink] = None

    @staticmethod
    def read(q: dict) -> UpdateNewChatJoinRequest:
        return UpdateNewChatJoinRequest.construct(**q)


class UpdateNewChosenInlineResult(Update):
    """
    The user has chosen a result of an inline query; for bots only
    
    :param sender_user_id: Identifier of the user who sent the query
    :type sender_user_id: :class:`int`
    
    :param user_location: User location; may be null, defaults to None
    :type user_location: :class:`Location`, optional
    
    :param query: Text of the query
    :type query: :class:`str`
    
    :param result_id: Identifier of the chosen result
    :type result_id: :class:`str`
    
    :param inline_message_id: Identifier of the sent inline message, if known
    :type inline_message_id: :class:`str`
    
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
    
    :param event: A JSON-serialized event
    :type event: :class:`str`
    
    """

    ID: str = Field("updateNewCustomEvent", alias="@type")
    event: str

    @staticmethod
    def read(q: dict) -> UpdateNewCustomEvent:
        return UpdateNewCustomEvent.construct(**q)


class UpdateNewCustomQuery(Update):
    """
    A new incoming query; for bots only
    
    :param id: The query identifier
    :type id: :class:`int`
    
    :param data: JSON-serialized query data
    :type data: :class:`str`
    
    :param timeout: Query timeout
    :type timeout: :class:`int`
    
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
    
    :param id: Unique query identifier
    :type id: :class:`int`
    
    :param sender_user_id: Identifier of the user who sent the query
    :type sender_user_id: :class:`int`
    
    :param inline_message_id: Identifier of the inline message from which the query originated
    :type inline_message_id: :class:`str`
    
    :param chat_instance: An identifier uniquely corresponding to the chat a message was sent to
    :type chat_instance: :class:`int`
    
    :param payload: Query payload
    :type payload: :class:`CallbackQueryPayload`
    
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
    
    :param id: Unique query identifier
    :type id: :class:`int`
    
    :param sender_user_id: Identifier of the user who sent the query
    :type sender_user_id: :class:`int`
    
    :param user_location: User location; may be null, defaults to None
    :type user_location: :class:`Location`, optional
    
    :param chat_type: The type of the chat from which the query originated; may be null if unknown, defaults to None
    :type chat_type: :class:`ChatType`, optional
    
    :param query: Text of the query
    :type query: :class:`str`
    
    :param offset: Offset of the first entry to return
    :type offset: :class:`str`
    
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
    
    :param message: The new message
    :type message: :class:`Message`
    
    """

    ID: str = Field("updateNewMessage", alias="@type")
    message: Message

    @staticmethod
    def read(q: dict) -> UpdateNewMessage:
        return UpdateNewMessage.construct(**q)


class UpdateNewPreCheckoutQuery(Update):
    """
    A new incoming pre-checkout query; for bots only. Contains full information about a checkout
    
    :param id: Unique query identifier
    :type id: :class:`int`
    
    :param sender_user_id: Identifier of the user who sent the query
    :type sender_user_id: :class:`int`
    
    :param currency: Currency for the product price
    :type currency: :class:`str`
    
    :param total_amount: Total price for the product, in the smallest units of the currency
    :type total_amount: :class:`int`
    
    :param invoice_payload: Invoice payload
    :type invoice_payload: :class:`str`
    
    :param shipping_option_id: Identifier of a shipping option chosen by the user; may be empty if not applicable
    :type shipping_option_id: :class:`str`
    
    :param order_info: Information about the order; may be null, defaults to None
    :type order_info: :class:`OrderInfo`, optional
    
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
    
    :param id: Unique query identifier
    :type id: :class:`int`
    
    :param sender_user_id: Identifier of the user who sent the query
    :type sender_user_id: :class:`int`
    
    :param invoice_payload: Invoice payload
    :type invoice_payload: :class:`str`
    
    :param shipping_address: User shipping address
    :type shipping_address: :class:`Address`
    
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
    
    :param notification_group_id: Unique notification group identifier
    :type notification_group_id: :class:`int`
    
    :param notification: Changed notification
    :type notification: :class:`Notification`
    
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
    
    :param notification_group_id: Unique notification group identifier
    :type notification_group_id: :class:`int`
    
    :param type_: New type of the notification group
    :type type_: :class:`NotificationGroupType`
    
    :param chat_id: Identifier of a chat to which all notifications in the group belong
    :type chat_id: :class:`int`
    
    :param notification_settings_chat_id: Chat identifier, which notification settings must be applied to the added notifications
    :type notification_settings_chat_id: :class:`int`
    
    :param notification_sound_id: Identifier of the notification sound to be played; 0 if sound is disabled
    :type notification_sound_id: :class:`int`
    
    :param total_count: Total number of unread notifications in the group, can be bigger than number of active notifications
    :type total_count: :class:`int`
    
    :param added_notifications: List of added group notifications, sorted by notification ID
    :type added_notifications: :class:`list[Notification]`
    
    :param removed_notification_ids: Identifiers of removed group notifications, sorted by notification ID
    :type removed_notification_ids: :class:`list[int]`
    
    """

    ID: str = Field("updateNotificationGroup", alias="@type")
    notification_group_id: int
    type_: NotificationGroupType = Field(..., alias='type')
    chat_id: int
    notification_settings_chat_id: int
    notification_sound_id: int
    total_count: int
    added_notifications: list[Notification]
    removed_notification_ids: list[int]

    @staticmethod
    def read(q: dict) -> UpdateNotificationGroup:
        return UpdateNotificationGroup.construct(**q)


class UpdateOption(Update):
    """
    An option changed its value
    
    :param name: The option name
    :type name: :class:`str`
    
    :param value: The new option value
    :type value: :class:`OptionValue`
    
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
    
    :param poll: New data about the poll
    :type poll: :class:`Poll`
    
    """

    ID: str = Field("updatePoll", alias="@type")
    poll: Poll

    @staticmethod
    def read(q: dict) -> UpdatePoll:
        return UpdatePoll.construct(**q)


class UpdatePollAnswer(Update):
    """
    A user changed the answer to a poll; for bots only
    
    :param poll_id: Unique poll identifier
    :type poll_id: :class:`int`
    
    :param user_id: The user, who changed the answer to the poll
    :type user_id: :class:`int`
    
    :param option_ids: 0-based identifiers of answer options, chosen by the user
    :type option_ids: :class:`list[int]`
    
    """

    ID: str = Field("updatePollAnswer", alias="@type")
    poll_id: int
    user_id: int
    option_ids: list[int]

    @staticmethod
    def read(q: dict) -> UpdatePollAnswer:
        return UpdatePollAnswer.construct(**q)


class UpdateReactions(Update):
    """
    The list of supported reactions has changed
    
    :param reactions: The new list of supported reactions
    :type reactions: :class:`list[Reaction]`
    
    """

    ID: str = Field("updateReactions", alias="@type")
    reactions: list[Reaction]

    @staticmethod
    def read(q: dict) -> UpdateReactions:
        return UpdateReactions.construct(**q)


class UpdateRecentStickers(Update):
    """
    The list of recently used stickers was updated
    
    :param is_attached: True, if the list of stickers attached to photo or video files was updated, otherwise the list of sent stickers is updated
    :type is_attached: :class:`bool`
    
    :param sticker_ids: The new list of file identifiers of recently used stickers
    :type sticker_ids: :class:`list[int]`
    
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
    
    :param animation_ids: The new list of file identifiers of saved animations
    :type animation_ids: :class:`list[int]`
    
    """

    ID: str = Field("updateSavedAnimations", alias="@type")
    animation_ids: list[int]

    @staticmethod
    def read(q: dict) -> UpdateSavedAnimations:
        return UpdateSavedAnimations.construct(**q)


class UpdateSavedNotificationSounds(Update):
    """
    The list of saved notifications sounds was updated. This update may not be sent until information about a notification sound was requested for the first time
    
    :param notification_sound_ids: The new list of identifiers of saved notification sounds
    :type notification_sound_ids: :class:`list[int]`
    
    """

    ID: str = Field("updateSavedNotificationSounds", alias="@type")
    notification_sound_ids: list[int]

    @staticmethod
    def read(q: dict) -> UpdateSavedNotificationSounds:
        return UpdateSavedNotificationSounds.construct(**q)


class UpdateScopeNotificationSettings(Update):
    """
    Notification settings for some type of chats were updated
    
    :param scope: Types of chats for which notification settings were updated
    :type scope: :class:`NotificationSettingsScope`
    
    :param notification_settings: The new notification settings
    :type notification_settings: :class:`ScopeNotificationSettings`
    
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
    
    :param secret_chat: New data about the secret chat
    :type secret_chat: :class:`SecretChat`
    
    """

    ID: str = Field("updateSecretChat", alias="@type")
    secret_chat: SecretChat

    @staticmethod
    def read(q: dict) -> UpdateSecretChat:
        return UpdateSecretChat.construct(**q)


class UpdateSelectedBackground(Update):
    """
    The selected background has changed
    
    :param for_dark_theme: True, if background for dark theme has changed
    :type for_dark_theme: :class:`bool`
    
    :param background: The new selected background; may be null, defaults to None
    :type background: :class:`Background`, optional
    
    """

    ID: str = Field("updateSelectedBackground", alias="@type")
    for_dark_theme: bool
    background: typing.Optional[Background] = None

    @staticmethod
    def read(q: dict) -> UpdateSelectedBackground:
        return UpdateSelectedBackground.construct(**q)


class UpdateServiceNotification(Update):
    """
    A service notification from the server was received. Upon receiving this the application must show a popup with the content of the notification
    
    :param type_: Notification type. If type begins with "AUTH_KEY_DROP_", then two buttons "Cancel" and "Log out" must be shown under notification; if user presses the second, all local data must be destroyed using Destroy method
    :type type_: :class:`str`
    
    :param content: Notification content
    :type content: :class:`MessageContent`
    
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
    
    :param sticker_set: The sticker set
    :type sticker_set: :class:`StickerSet`
    
    """

    ID: str = Field("updateStickerSet", alias="@type")
    sticker_set: StickerSet

    @staticmethod
    def read(q: dict) -> UpdateStickerSet:
        return UpdateStickerSet.construct(**q)


class UpdateSuggestedActions(Update):
    """
    The list of suggested to the user actions has changed
    
    :param added_actions: Added suggested actions
    :type added_actions: :class:`list[SuggestedAction]`
    
    :param removed_actions: Removed suggested actions
    :type removed_actions: :class:`list[SuggestedAction]`
    
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
    
    :param supergroup: New data about the supergroup
    :type supergroup: :class:`Supergroup`
    
    """

    ID: str = Field("updateSupergroup", alias="@type")
    supergroup: Supergroup

    @staticmethod
    def read(q: dict) -> UpdateSupergroup:
        return UpdateSupergroup.construct(**q)


class UpdateSupergroupFullInfo(Update):
    """
    Some data in supergroupFullInfo has been changed
    
    :param supergroup_id: Identifier of the supergroup or channel
    :type supergroup_id: :class:`int`
    
    :param supergroup_full_info: New full information about the supergroup
    :type supergroup_full_info: :class:`SupergroupFullInfo`
    
    """

    ID: str = Field("updateSupergroupFullInfo", alias="@type")
    supergroup_id: int
    supergroup_full_info: SupergroupFullInfo

    @staticmethod
    def read(q: dict) -> UpdateSupergroupFullInfo:
        return UpdateSupergroupFullInfo.construct(**q)


class UpdateTermsOfService(Update):
    """
    New terms of service must be accepted by the user. If the terms of service are declined, then the deleteAccount method must be called with the reason "Decline ToS update"
    
    :param terms_of_service_id: Identifier of the terms of service
    :type terms_of_service_id: :class:`str`
    
    :param terms_of_service: The new terms of service
    :type terms_of_service: :class:`TermsOfService`
    
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
    
    :param sticker_sets: The prefix of the list of trending sticker sets with the newest trending sticker sets
    :type sticker_sets: :class:`TrendingStickerSets`
    
    """

    ID: str = Field("updateTrendingStickerSets", alias="@type")
    sticker_sets: TrendingStickerSets

    @staticmethod
    def read(q: dict) -> UpdateTrendingStickerSets:
        return UpdateTrendingStickerSets.construct(**q)


class UpdateUnreadChatCount(Update):
    """
    Number of unread chats, i.e. with unread messages or marked as unread, has changed. This update is sent only if the message database is used
    
    :param chat_list: The chat list with changed number of unread messages
    :type chat_list: :class:`ChatList`
    
    :param total_count: Approximate total number of chats in the chat list
    :type total_count: :class:`int`
    
    :param unread_count: Total number of unread chats
    :type unread_count: :class:`int`
    
    :param unread_unmuted_count: Total number of unread unmuted chats
    :type unread_unmuted_count: :class:`int`
    
    :param marked_as_unread_count: Total number of chats marked as unread
    :type marked_as_unread_count: :class:`int`
    
    :param marked_as_unread_unmuted_count: Total number of unmuted chats marked as unread
    :type marked_as_unread_unmuted_count: :class:`int`
    
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
    
    :param chat_list: The chat list with changed number of unread messages
    :type chat_list: :class:`ChatList`
    
    :param unread_count: Total number of unread messages
    :type unread_count: :class:`int`
    
    :param unread_unmuted_count: Total number of unread messages in unmuted chats
    :type unread_unmuted_count: :class:`int`
    
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
    
    :param user: New data about the user
    :type user: :class:`User`
    
    """

    ID: str = Field("updateUser", alias="@type")
    user: User

    @staticmethod
    def read(q: dict) -> UpdateUser:
        return UpdateUser.construct(**q)


class UpdateUserFullInfo(Update):
    """
    Some data in userFullInfo has been changed
    
    :param user_id: User identifier
    :type user_id: :class:`int`
    
    :param user_full_info: New full information about the user
    :type user_full_info: :class:`UserFullInfo`
    
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
    
    :param setting: The privacy setting
    :type setting: :class:`UserPrivacySetting`
    
    :param rules: New privacy rules
    :type rules: :class:`UserPrivacySettingRules`
    
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
    
    :param user_id: User identifier
    :type user_id: :class:`int`
    
    :param status: New status of the user
    :type status: :class:`UserStatus`
    
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
    
    :param users_nearby: The new list of users nearby
    :type users_nearby: :class:`list[ChatNearby]`
    
    """

    ID: str = Field("updateUsersNearby", alias="@type")
    users_nearby: list[ChatNearby]

    @staticmethod
    def read(q: dict) -> UpdateUsersNearby:
        return UpdateUsersNearby.construct(**q)


class UpdateWebAppMessageSent(Update):
    """
    A message was sent by an opened Web App, so the Web App needs to be closed
    
    :param web_app_launch_id: Identifier of Web App launch
    :type web_app_launch_id: :class:`int`
    
    """

    ID: str = Field("updateWebAppMessageSent", alias="@type")
    web_app_launch_id: int

    @staticmethod
    def read(q: dict) -> UpdateWebAppMessageSent:
        return UpdateWebAppMessageSent.construct(**q)
