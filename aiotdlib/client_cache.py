from __future__ import annotations

import logging
import typing

from sortedcontainers import SortedSet

from .api import (
    API,
    AioTDLibError,
    BasicGroup,
    BasicGroupFullInfo,
    Chat,
    ChatListMain,
    ChatPosition,
    NotFound,
    Ok,
    OptionValueBoolean,
    OptionValueEmpty,
    OptionValueInteger,
    OptionValueString,
    SecretChat,
    Supergroup,
    SupergroupFullInfo,
    UpdateBasicGroup,
    UpdateBasicGroupFullInfo,
    UpdateChatAction,
    UpdateChatActionBar,
    UpdateChatAvailableReactions,
    UpdateChatBackground,
    UpdateChatBlockList,
    UpdateChatDefaultDisableNotification,
    UpdateChatDraftMessage,
    UpdateChatFolders,
    UpdateChatHasProtectedContent,
    UpdateChatHasScheduledMessages,
    UpdateChatIsMarkedAsUnread,
    UpdateChatIsTranslatable,
    UpdateChatLastMessage,
    UpdateChatMessageAutoDeleteTime,
    UpdateChatMessageSender,
    UpdateChatNotificationSettings,
    UpdateChatOnlineMemberCount,
    UpdateChatPendingJoinRequests,
    UpdateChatPermissions,
    UpdateChatPhoto,
    UpdateChatPosition,
    UpdateChatReadInbox,
    UpdateChatReadOutbox,
    UpdateChatReplyMarkup,
    UpdateChatTheme,
    UpdateChatThemes,
    UpdateChatTitle,
    UpdateChatUnreadMentionCount,
    UpdateChatUnreadReactionCount,
    UpdateChatVideoChat,
    UpdateNewChat,
    UpdateOption,
    UpdateSecretChat,
    UpdateSupergroup,
    UpdateSupergroupFullInfo,
    UpdateUser,
    UpdateUserFullInfo,
    UpdateUserStatus,
    User,
    UserFullInfo,
    Vector,
)

if typing.TYPE_CHECKING:
    from .client import Client


class OrderedChat:
    chat_id: int
    position: ChatPosition

    def __init__(self, chat_id: int, chat_position: ChatPosition):
        self.chat_id = chat_id
        self.position = chat_position

    @property
    def order_tuple(self) -> tuple[int, int]:
        return self.position.order, self.chat_id

    def __hash__(self):
        return object.__hash__(self.chat_id)

    def __eq__(self, other: OrderedChat):
        return self.order_tuple == other.order_tuple

    def __ne__(self, other: OrderedChat):
        return not self.__eq__(other)

    def __lt__(self, other: OrderedChat):
        # Reverse order
        return self.order_tuple >= other.order_tuple

    def __gt__(self, other: OrderedChat):
        # Reverse order
        return self.order_tuple <= other.order_tuple

    def __le__(self, other: OrderedChat):
        # Reverse order
        return self.order_tuple > other.order_tuple

    def __ge__(self, other: OrderedChat):
        # Reverse order
        return self.order_tuple < other.order_tuple


SomeChatUpdate = typing.Union[
    UpdateChatAction,
    UpdateChatActionBar,
    UpdateChatAvailableReactions,
    UpdateChatBackground,
    UpdateChatDefaultDisableNotification,
    UpdateChatDraftMessage,
    UpdateChatFolders,
    UpdateChatHasProtectedContent,
    UpdateChatHasScheduledMessages,
    UpdateChatBlockList,
    UpdateChatIsMarkedAsUnread,
    UpdateChatIsTranslatable,
    UpdateChatLastMessage,
    UpdateChatMessageAutoDeleteTime,
    UpdateChatMessageSender,
    UpdateChatNotificationSettings,
    UpdateChatOnlineMemberCount,
    UpdateChatPendingJoinRequests,
    UpdateChatPermissions,
    UpdateChatPhoto,
    UpdateChatPosition,
    UpdateChatReadInbox,
    UpdateChatReadOutbox,
    UpdateChatReplyMarkup,
    UpdateChatTheme,
    UpdateChatThemes,
    UpdateChatTitle,
    UpdateChatUnreadMentionCount,
    UpdateChatUnreadReactionCount,
    UpdateChatVideoChat,
]


class ClientCache:
    # noinspection PyTypeChecker
    def __init__(self, client: "Client"):
        self.logger = logging.getLogger(__name__)
        self.client = client

        # Client Options
        self.options: dict[str, typing.Union[str, int, bool]] = {}

        self.users: dict[int, User] = {}
        self.basic_groups: dict[int, BasicGroup] = {}
        self.supergroups: dict[int, Supergroup] = {}
        self.secret_chats: dict[int, SecretChat] = {}

        # Full Info
        self.users_full_info: dict[int, UserFullInfo] = {}
        self.basic_groups_full_info: dict[int, BasicGroupFullInfo] = {}
        self.supergroups_full_info: dict[int, SupergroupFullInfo] = {}

        # Chats
        self.chats: dict[int, Chat] = {}
        self.main_chat_list: SortedSet[OrderedChat] = SortedSet()
        self.have_full_main_chat_list: bool = False

        self.update_option_handler = client.add_event_handler(
            self.__on_update_option, API.Types.UPDATE_OPTION
        )
        self.update_user_handler = client.add_event_handler(
            self.__on_update_user, API.Types.UPDATE_USER
        )
        self.update_user_full_info_handler = client.add_event_handler(
            self.__on_update_user_full_info, API.Types.UPDATE_USER_FULL_INFO
        )
        self.update_basic_group_handler = client.add_event_handler(
            self.__on_update_basic_group, API.Types.UPDATE_BASIC_GROUP
        )
        self.update_basic_group_full_info_handler = client.add_event_handler(
            self.__on_update_basic_group_full_info, API.Types.UPDATE_BASIC_GROUP_FULL_INFO
        )
        self.update_supergroup_handler = client.add_event_handler(
            self.__on_update_supergroup, API.Types.UPDATE_SUPERGROUP
        )
        self.update_supergroup_full_info_handler = client.add_event_handler(
            self.__on_update_supergroup_full_info, API.Types.UPDATE_SUPERGROUP_FULL_INFO
        )
        self.update_secret_chat_handler = client.add_event_handler(
            self.__on_update_secret_chat, API.Types.UPDATE_SECRET_CHAT
        )
        self.update_new_chat_handler = client.add_event_handler(
            self.__on_update_new_chat, API.Types.UPDATE_NEW_CHAT
        )

        # Chat updates
        # Updates changing positions
        self.update_chat_position_handler = client.add_event_handler(
            self.__on_update_chat_position, API.Types.UPDATE_CHAT_POSITION
        )
        self.update_chat_last_message_handler = client.add_event_handler(
            self.__on_update_chat_last_message, API.Types.UPDATE_CHAT_LAST_MESSAGE
        )
        self.update_chat_draft_message_handler = client.add_event_handler(
            self.__on_update_chat_draft_message, API.Types.UPDATE_CHAT_DRAFT_MESSAGE
        )

        # Updates changing info only
        self.update_chat_action_bar_handler = client.add_event_handler(
            self.__on_update_chat_action_bar, API.Types.UPDATE_CHAT_ACTION_BAR
        )
        self.update_chat_available_reactions_handler = client.add_event_handler(
            self.__on_update_chat_available_reactions, API.Types.UPDATE_CHAT_AVAILABLE_REACTIONS
        )
        self.update_chat_background_handler = client.add_event_handler(
            self.__on_update_chat_background, API.Types.UPDATE_CHAT_BACKGROUND
        )
        self.update_chat_default_disable_notification_handler = self.client.add_event_handler(
            self.__on_update_chat_default_disable_notification,
            API.Types.UPDATE_CHAT_DEFAULT_DISABLE_NOTIFICATION,
        )
        self.update_chat_folders_handler = client.add_event_handler(
            self.__on_update_chat_folders, API.Types.UPDATE_CHAT_FOLDERS
        )
        self.update_chat_has_protected_content_handler = self.client.add_event_handler(
            self.__on_update_chat_has_protected_content, API.Types.UPDATE_CHAT_HAS_PROTECTED_CONTENT
        )
        self.update_chat_has_scheduled_messages_handler = self.client.add_event_handler(
            self.__on_update_chat_has_scheduled_messages,
            API.Types.UPDATE_CHAT_HAS_SCHEDULED_MESSAGES,
        )
        self.update_chat_block_list_handler = client.add_event_handler(
            self.__on_update_chat_is_blocked, API.Types.UPDATE_CHAT_BLOCK_LIST
        )
        self.update_chat_is_marked_as_unread_handler = client.add_event_handler(
            self.__on_update_chat_is_marked_as_unread, API.Types.UPDATE_CHAT_IS_MARKED_AS_UNREAD
        )
        self.update_chat_is_translatable_handler = client.add_event_handler(
            self.__on_update_chat_is_translatable, API.Types.UPDATE_CHAT_IS_TRANSLATABLE
        )
        self.update_chat_message_auto_delete_time_handler = self.client.add_event_handler(
            self.__on_update_chat_message_auto_delete_time,
            API.Types.UPDATE_CHAT_MESSAGE_AUTO_DELETE_TIME,
        )
        self.update_chat_message_sender_handler = client.add_event_handler(
            self.__on_update_chat_message_sender, API.Types.UPDATE_CHAT_MESSAGE_SENDER
        )
        self.update_chat_notification_settings_handler = self.client.add_event_handler(
            self.__on_update_chat_notification_settings, API.Types.UPDATE_CHAT_NOTIFICATION_SETTINGS
        )
        self.update_chat_online_member_count_handler = client.add_event_handler(
            self.__on_update_chat_online_member_count, API.Types.UPDATE_CHAT_ONLINE_MEMBER_COUNT
        )
        self.update_chat_pending_join_requests_handler = self.client.add_event_handler(
            self.__on_update_chat_pending_join_requests, API.Types.UPDATE_CHAT_PENDING_JOIN_REQUESTS
        )
        self.update_chat_permissions_handler = client.add_event_handler(
            self.__on_update_chat_permissions, API.Types.UPDATE_CHAT_PERMISSIONS
        )
        self.update_chat_photo_handler = client.add_event_handler(
            self.__on_update_chat_photo, API.Types.UPDATE_CHAT_PHOTO
        )
        self.update_chat_read_inbox_handler = client.add_event_handler(
            self.__on_update_chat_read_inbox, API.Types.UPDATE_CHAT_READ_INBOX
        )
        self.update_chat_read_outbox_handler = client.add_event_handler(
            self.__on_update_chat_read_outbox, API.Types.UPDATE_CHAT_READ_OUTBOX
        )
        self.update_chat_reply_markup_handler = client.add_event_handler(
            self.__on_update_chat_reply_markup, API.Types.UPDATE_CHAT_REPLY_MARKUP
        )
        self.update_chat_theme_handler = client.add_event_handler(
            self.__on_update_chat_theme, API.Types.UPDATE_CHAT_THEME
        )
        self.update_chat_title_handler = client.add_event_handler(
            self.__on_update_chat_title, API.Types.UPDATE_CHAT_TITLE
        )
        self.update_chat_unread_mention_count_handler = client.add_event_handler(
            self.__on_update_chat_unread_mention_count, API.Types.UPDATE_CHAT_UNREAD_MENTION_COUNT
        )
        self.update_chat_unread_reaction_count_handler = self.client.add_event_handler(
            self.__on_update_chat_unread_reaction_count, API.Types.UPDATE_CHAT_UNREAD_REACTION_COUNT
        )
        self.update_chat_video_chat_handler = client.add_event_handler(
            self.__on_update_chat_video_chat, API.Types.UPDATE_CHAT_VIDEO_CHAT
        )

    def clear(self):
        self.options.clear()
        self.users.clear()
        self.basic_groups.clear()
        self.supergroups.clear()
        self.secret_chats.clear()
        self.users_full_info.clear()
        self.basic_groups_full_info.clear()
        self.supergroups_full_info.clear()
        self.chats.clear()
        self.main_chat_list.clear()
        self.have_full_main_chat_list = False

        if bool(self.client):
            self.client.remove_event_handler(self.update_option_handler, API.Types.UPDATE_OPTION)
            self.client.remove_event_handler(self.update_user_handler, API.Types.UPDATE_USER)
            self.client.remove_event_handler(
                self.update_user_full_info_handler, API.Types.UPDATE_USER_FULL_INFO
            )
            self.client.remove_event_handler(
                self.update_basic_group_handler, API.Types.UPDATE_BASIC_GROUP
            )
            self.client.remove_event_handler(
                self.update_basic_group_full_info_handler, API.Types.UPDATE_BASIC_GROUP_FULL_INFO
            )
            self.client.remove_event_handler(
                self.update_supergroup_handler, API.Types.UPDATE_SUPERGROUP
            )
            self.client.remove_event_handler(
                self.update_supergroup_full_info_handler, API.Types.UPDATE_SUPERGROUP_FULL_INFO
            )
            self.client.remove_event_handler(
                self.update_secret_chat_handler, API.Types.UPDATE_SECRET_CHAT
            )
            self.client.remove_event_handler(
                self.update_new_chat_handler, API.Types.UPDATE_NEW_CHAT
            )
            self.client.remove_event_handler(
                self.update_chat_position_handler, API.Types.UPDATE_CHAT_POSITION
            )
            self.client.remove_event_handler(
                self.update_chat_last_message_handler, API.Types.UPDATE_CHAT_LAST_MESSAGE
            )
            self.client.remove_event_handler(
                self.update_chat_draft_message_handler, API.Types.UPDATE_CHAT_DRAFT_MESSAGE
            )
            self.client.remove_event_handler(
                self.update_chat_action_bar_handler, API.Types.UPDATE_CHAT_ACTION_BAR
            )
            self.client.remove_event_handler(
                self.update_chat_available_reactions_handler,
                API.Types.UPDATE_CHAT_AVAILABLE_REACTIONS,
            )
            self.client.remove_event_handler(
                self.update_chat_background_handler, API.Types.UPDATE_CHAT_BACKGROUND
            )
            self.client.remove_event_handler(
                self.update_chat_default_disable_notification_handler,
                API.Types.UPDATE_CHAT_DEFAULT_DISABLE_NOTIFICATION,
            )
            self.client.remove_event_handler(
                self.update_chat_folders_handler, API.Types.UPDATE_CHAT_FOLDERS
            )
            self.client.remove_event_handler(
                self.update_chat_has_protected_content_handler,
                API.Types.UPDATE_CHAT_HAS_PROTECTED_CONTENT,
            )
            self.client.remove_event_handler(
                self.update_chat_has_scheduled_messages_handler,
                API.Types.UPDATE_CHAT_HAS_SCHEDULED_MESSAGES,
            )
            self.client.remove_event_handler(
                self.update_chat_block_list_handler, API.Types.UPDATE_CHAT_BLOCK_LIST
            )
            self.client.remove_event_handler(
                self.update_chat_is_marked_as_unread_handler,
                API.Types.UPDATE_CHAT_IS_MARKED_AS_UNREAD,
            )
            self.client.remove_event_handler(
                self.update_chat_is_translatable_handler, API.Types.UPDATE_CHAT_IS_TRANSLATABLE
            )
            self.client.remove_event_handler(
                self.update_chat_message_auto_delete_time_handler,
                API.Types.UPDATE_CHAT_MESSAGE_AUTO_DELETE_TIME,
            )
            self.client.remove_event_handler(
                self.update_chat_message_sender_handler, API.Types.UPDATE_CHAT_MESSAGE_SENDER
            )
            self.client.remove_event_handler(
                self.update_chat_notification_settings_handler,
                API.Types.UPDATE_CHAT_NOTIFICATION_SETTINGS,
            )
            self.client.remove_event_handler(
                self.update_chat_online_member_count_handler,
                API.Types.UPDATE_CHAT_ONLINE_MEMBER_COUNT,
            )
            self.client.remove_event_handler(
                self.update_chat_pending_join_requests_handler,
                API.Types.UPDATE_CHAT_PENDING_JOIN_REQUESTS,
            )
            self.client.remove_event_handler(
                self.update_chat_permissions_handler, API.Types.UPDATE_CHAT_PERMISSIONS
            )
            self.client.remove_event_handler(
                self.update_chat_photo_handler, API.Types.UPDATE_CHAT_PHOTO
            )
            self.client.remove_event_handler(
                self.update_chat_read_inbox_handler, API.Types.UPDATE_CHAT_READ_INBOX
            )
            self.client.remove_event_handler(
                self.update_chat_read_outbox_handler, API.Types.UPDATE_CHAT_READ_OUTBOX
            )
            self.client.remove_event_handler(
                self.update_chat_reply_markup_handler, API.Types.UPDATE_CHAT_REPLY_MARKUP
            )
            self.client.remove_event_handler(
                self.update_chat_theme_handler, API.Types.UPDATE_CHAT_THEME
            )
            self.client.remove_event_handler(
                self.update_chat_title_handler, API.Types.UPDATE_CHAT_TITLE
            )
            self.client.remove_event_handler(
                self.update_chat_unread_mention_count_handler,
                API.Types.UPDATE_CHAT_UNREAD_MENTION_COUNT,
            )
            self.client.remove_event_handler(
                self.update_chat_unread_reaction_count_handler,
                API.Types.UPDATE_CHAT_UNREAD_REACTION_COUNT,
            )
            self.client.remove_event_handler(
                self.update_chat_video_chat_handler, API.Types.UPDATE_CHAT_VIDEO_CHAT
            )

    async def get_option_value(self, name: str) -> typing.Union[str, int, bool, None]:
        value = self.options.get(name)

        if not bool(value):
            option_value = await self.client.api.get_option(name)

            if isinstance(option_value, OptionValueEmpty):
                value = None
            elif isinstance(option_value, OptionValueInteger):
                value = int(option_value.value)
            elif isinstance(
                option_value,
                (
                    OptionValueString,
                    OptionValueBoolean,
                ),
            ):
                value = option_value.value
            else:
                value = None

            self.options[name] = value

        return value

    async def get_main_chat_list(self, limit: int = 100) -> list[Chat]:
        while not self.have_full_main_chat_list:
            try:
                result = await self.client.api.load_chats(
                    limit=100,
                    chat_list=ChatListMain(),
                    request_id="chats_preload",
                    request_timeout=300,
                )
            except NotFound:
                self.have_full_main_chat_list = True
            except AioTDLibError as e:
                self.logger.error(f"Received an error for get_main_list_chats: {e}")
                break
            else:
                if not isinstance(result, Ok):
                    break

        return [
            self.chats.get(ordered_chat.chat_id) for ordered_chat in self.main_chat_list[:limit]
        ]

    async def get_chat(self, chat_id: int, *, force_update: bool = True) -> Chat:
        chat = self.chats.get(chat_id)

        if not bool(chat) or force_update:
            chat = await self.client.api.get_chat(chat_id)
            self.__set_chat_positions(chat, chat.positions)
            self.chats[chat_id] = chat

        return chat

    async def get_user(self, user_id: int, *, force_update: bool = True) -> User:
        user = self.users.get(user_id)

        if not bool(user) or force_update:
            user = await self.client.api.get_user(user_id)
            self.users[user_id] = user

        return user

    async def get_user_full_info(self, user_id: int, *, force_update: bool = True) -> UserFullInfo:
        user_full_info = self.users_full_info.get(user_id)

        if not bool(user_full_info) or force_update:
            user_full_info = await self.client.api.get_user_full_info(user_id)
            self.users_full_info[user_id] = user_full_info

        return user_full_info

    async def get_basic_group(
        self, basic_group_id: int, *, force_update: bool = True
    ) -> BasicGroup:
        basic_group = self.basic_groups.get(basic_group_id)

        if not bool(basic_group) or force_update:
            basic_group = await self.client.api.get_basic_group(basic_group_id)
            self.basic_groups[basic_group_id] = basic_group

        return basic_group

    async def get_basic_group_full_info(
        self, basic_group_id: int, *, force_update: bool = True
    ) -> BasicGroupFullInfo:
        basic_group_full_info = self.basic_groups_full_info.get(basic_group_id)

        if not bool(basic_group_full_info) or force_update:
            basic_group_full_info = await self.client.api.get_basic_group_full_info(basic_group_id)
            self.basic_groups_full_info[basic_group_id] = basic_group_full_info

        return basic_group_full_info

    async def get_supergroup(self, supergroup_id: int, *, force_update: bool = True) -> Supergroup:
        supergroup = self.supergroups.get(supergroup_id)

        if not bool(supergroup) or force_update:
            supergroup = await self.client.api.get_supergroup(supergroup_id)
            self.supergroups[supergroup_id] = supergroup

        return supergroup

    async def get_supergroup_full_info(
        self, supergroup_id: int, *, force_update: bool = True
    ) -> SupergroupFullInfo:
        supergroup_full_info = self.supergroups_full_info.get(supergroup_id)

        if not bool(supergroup_full_info) or force_update:
            supergroup_full_info = await self.client.api.get_supergroup_full_info(supergroup_id)
            self.supergroups_full_info[supergroup_id] = supergroup_full_info

        return supergroup_full_info

    async def get_secret_chat(
        self, secret_chat_id: int, *, force_update: bool = True
    ) -> SecretChat:
        secret_chat = self.secret_chats.get(secret_chat_id)

        if not bool(secret_chat) or force_update:
            secret_chat = await self.client.api.get_secret_chat(secret_chat_id)
            self.secret_chats[secret_chat_id] = secret_chat

        return secret_chat

    def __set_chat_positions(self, chat: Chat, positions: Vector[ChatPosition]):
        for position in chat.positions:
            if isinstance(position.list, ChatListMain):
                try:
                    self.main_chat_list.remove(OrderedChat(chat.id, position))
                except (KeyError, ValueError):
                    pass

        chat.positions = positions

        for position in chat.positions:
            if isinstance(position.list, ChatListMain):
                self.main_chat_list.add(OrderedChat(chat.id, position))

    async def __on_update_option(self, _: Client, update: UpdateOption):
        if isinstance(update.value, OptionValueEmpty):
            value = None
        elif isinstance(update.value, OptionValueInteger):
            value = int(update.value.value)
        elif isinstance(
            update.value,
            (
                OptionValueString,
                OptionValueBoolean,
            ),
        ):
            value = update.value.value
        else:
            return

        self.options[update.name] = value

    async def __on_update_user(self, _: Client, update: UpdateUser):
        self.users[update.user.id] = update.user

    async def __on_update_user_full_info(self, _: Client, update: UpdateUserFullInfo):
        self.users_full_info[update.user_id] = update.user_full_info

    async def __on_update_user_status(self, _: Client, update: UpdateUserStatus):
        self.users[update.user_id].status = update.status

    async def __on_update_basic_group(self, _: Client, update: UpdateBasicGroup):
        self.basic_groups[update.basic_group.id] = update.basic_group

    async def __on_update_basic_group_full_info(self, _: Client, update: UpdateBasicGroupFullInfo):
        self.basic_groups_full_info[update.basic_group_id] = update.basic_group_full_info

    async def __on_update_supergroup(self, _: Client, update: UpdateSupergroup):
        self.supergroups[update.supergroup.id] = update.supergroup

    async def __on_update_supergroup_full_info(self, _: Client, update: UpdateSupergroupFullInfo):
        self.supergroups_full_info[update.supergroup_id] = update.supergroup_full_info

    async def __on_update_secret_chat(self, _: Client, update: UpdateSecretChat):
        self.secret_chats[update.secret_chat.id] = update.secret_chat

    async def __on_update_new_chat(self, _: Client, update: UpdateNewChat):
        self.chats[update.chat.id] = update.chat
        self.__set_chat_positions(update.chat, update.chat.positions)

    async def __on_update_chat_position(self, _: Client, update: UpdateChatPosition):
        if isinstance(update.position.list, ChatListMain):
            chat = self.chats.get(update.chat_id)
            new_positions = [update.position] + [
                p for p in chat.positions if not isinstance(p, ChatListMain)
            ]
            self.__set_chat_positions(chat, new_positions)

        # TODO: Update chat positions in archive and folders

    async def __on_update_chat_last_message(self, _: Client, update: UpdateChatLastMessage):
        chat = self.chats.get(update.chat_id)
        chat.last_message = update.last_message
        self.__set_chat_positions(chat, update.positions)

    async def __on_update_chat_draft_message(self, _: Client, update: UpdateChatDraftMessage):
        chat = self.chats[update.chat_id]
        chat.draft_message = update.draft_message
        self.__set_chat_positions(chat, update.positions)

    async def __on_update_chat_data(self, _: Client, update: SomeChatUpdate, *, attribute: str):
        if update.chat_id in self.chats:
            new_value = getattr(update, attribute)
            setattr(self.chats[update.chat_id], attribute, new_value)
            self.logger.debug(f"Updating {attribute} = {new_value} for chat {update.chat_id}")

    async def __on_update_chat_action_bar(self, _: Client, update: UpdateChatActionBar):
        self.chats[update.chat_id].action_bar = update.action_bar

    async def __on_update_chat_available_reactions(
        self, _: Client, update: UpdateChatAvailableReactions
    ):
        self.chats[update.chat_id].available_reactions = update.available_reactions

    async def __on_update_chat_background(self, _: Client, update: UpdateChatBackground):
        self.chats[update.chat_id].background = update.background

    async def __on_update_chat_default_disable_notification(
        self, _: Client, update: UpdateChatDefaultDisableNotification
    ):
        self.chats[
            update.chat_id
        ].default_disable_notification = update.default_disable_notification

    async def __on_update_chat_folders(self, _: Client, update: UpdateChatFolders):
        # TODO: Implement this
        pass

    async def __on_update_chat_has_protected_content(
        self, _: Client, update: UpdateChatHasProtectedContent
    ):
        self.chats[update.chat_id].has_protected_content = update.has_protected_content

    async def __on_update_chat_has_scheduled_messages(
        self, _: Client, update: UpdateChatHasScheduledMessages
    ):
        self.chats[update.chat_id].has_scheduled_messages = update.has_scheduled_messages

    async def __on_update_chat_is_blocked(self, _: Client, update: UpdateChatBlockList):
        self.chats[update.chat_id].block_list = update.block_list

    async def __on_update_chat_is_marked_as_unread(
        self, _: Client, update: UpdateChatIsMarkedAsUnread
    ):
        self.chats[update.chat_id].is_marked_as_unread = update.is_marked_as_unread

    async def __on_update_chat_is_translatable(self, _: Client, update: UpdateChatIsTranslatable):
        self.chats[update.chat_id].is_translatable = update.is_translatable

    async def __on_update_chat_message_auto_delete_time(
        self, _: Client, update: UpdateChatMessageAutoDeleteTime
    ):
        self.chats[update.chat_id].message_auto_delete_time = update.message_auto_delete_time

    async def __on_update_chat_message_sender(self, _: Client, update: UpdateChatMessageSender):
        self.chats[update.chat_id].message_sender_id = update.message_sender_id

    async def __on_update_chat_notification_settings(
        self, _: Client, update: UpdateChatNotificationSettings
    ):
        self.chats[update.chat_id].notification_settings = update.notification_settings

    async def __on_update_chat_online_member_count(
        self, _: Client, update: UpdateChatOnlineMemberCount
    ):
        pass

    async def __on_update_chat_pending_join_requests(
        self, _: Client, update: UpdateChatPendingJoinRequests
    ):
        self.chats[update.chat_id].pending_join_requests = update.pending_join_requests

    async def __on_update_chat_permissions(self, _: Client, update: UpdateChatPermissions):
        self.chats[update.chat_id].permissions = update.permissions

    async def __on_update_chat_photo(self, _: Client, update: UpdateChatPhoto):
        self.chats[update.chat_id].photo = update.photo

    async def __on_update_chat_read_inbox(self, _: Client, update: UpdateChatReadInbox):
        self.chats[update.chat_id].last_read_inbox_message_id = update.last_read_inbox_message_id
        self.chats[update.chat_id].unread_count = update.unread_count

    async def __on_update_chat_read_outbox(self, _: Client, update: UpdateChatReadOutbox):
        self.chats[update.chat_id].last_read_outbox_message_id = update.last_read_outbox_message_id

    async def __on_update_chat_reply_markup(self, _: Client, update: UpdateChatReplyMarkup):
        self.chats[update.chat_id].reply_markup_message_id = update.reply_markup_message_id

    async def __on_update_chat_theme(self, _: Client, update: UpdateChatTheme):
        self.chats[update.chat_id].theme_name = update.theme_name

    async def __on_update_chat_title(self, _: Client, update: UpdateChatTitle):
        self.chats[update.chat_id].title = update.title

    async def __on_update_chat_unread_mention_count(
        self, _: Client, update: UpdateChatUnreadMentionCount
    ):
        self.chats[update.chat_id].unread_mention_count = update.unread_mention_count

    async def __on_update_chat_unread_reaction_count(
        self, _: Client, update: UpdateChatUnreadReactionCount
    ):
        self.chats[update.chat_id].unread_reaction_count = update.unread_reaction_count

    async def __on_update_chat_video_chat(self, _: Client, update: UpdateChatVideoChat):
        self.chats[update.chat_id].video_chat = update.video_chat
