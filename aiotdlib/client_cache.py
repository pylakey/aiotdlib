from __future__ import annotations

import logging
import typing

from sortedcontainers import SortedSet

from .api import (
    API,
    BasicGroup,
    BasicGroupFullInfo,
    Chat,
    ChatListMain,
    ChatPosition,
    OptionValueBoolean,
    OptionValueEmpty,
    OptionValueInteger,
    OptionValueString,
    SecretChat,
    Supergroup,
    SupergroupFullInfo,
    UpdateBasicGroup,
    UpdateBasicGroupFullInfo,
    UpdateChatDefaultDisableNotification,
    UpdateChatDraftMessage,
    UpdateChatHasScheduledMessages,
    UpdateChatIsBlocked,
    UpdateChatIsMarkedAsUnread,
    UpdateChatLastMessage,
    UpdateChatMessageTtlSetting,
    UpdateChatNotificationSettings,
    UpdateChatPermissions,
    UpdateChatPhoto,
    UpdateChatPosition,
    UpdateChatReadInbox,
    UpdateChatReadOutbox,
    UpdateChatReplyMarkup,
    UpdateChatTitle,
    UpdateChatUnreadMentionCount,
    UpdateChatVoiceChat,
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
)
from .tdjson import TDLIB_MAX_INT

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


class ClientCache:
    # Client Options
    options: dict[str, typing.Union[str, int, bool]] = {}

    users: dict[int, User] = {}
    basic_groups: dict[int, BasicGroup] = {}
    supergroups: dict[int, Supergroup] = {}
    secret_chats: dict[int, SecretChat] = {}

    # Full Info
    users_full_info: dict[int, UserFullInfo] = {}
    basic_groups_full_info: dict[int, BasicGroupFullInfo] = {}
    supergroups_full_info: dict[int, SupergroupFullInfo] = {}

    # Chats
    chats: dict[int, Chat] = {}
    main_chats_list: SortedSet[OrderedChat] = SortedSet()
    have_full_main_chats_list: bool = False

    def __init__(self, client: 'Client'):
        self.logger = logging.getLogger(__name__)
        self.client = client
        client.add_event_handler(
            self.__on_update_option,
            API.Types.UPDATE_OPTION
        )
        client.add_event_handler(
            self.__on_update_user,
            API.Types.UPDATE_USER
        )
        client.add_event_handler(
            self.__on_update_user_full_info,
            API.Types.UPDATE_USER_FULL_INFO
        )
        client.add_event_handler(
            self.__on_update_basic_group,
            API.Types.UPDATE_BASIC_GROUP
        )
        client.add_event_handler(
            self.__on_update_basic_group_full_info,
            API.Types.UPDATE_BASIC_GROUP_FULL_INFO
        )
        client.add_event_handler(
            self.__on_update_supergroup,
            API.Types.UPDATE_SUPERGROUP
        )
        client.add_event_handler(
            self.__on_update_supergroup_full_info,
            API.Types.UPDATE_SUPERGROUP_FULL_INFO
        )
        client.add_event_handler(
            self.__on_update_secret_chat,
            API.Types.UPDATE_SECRET_CHAT
        )
        client.add_event_handler(
            self.__on_update_new_chat,
            API.Types.UPDATE_NEW_CHAT
        )
        client.add_event_handler(
            self.__on_update_chat_position,
            API.Types.UPDATE_CHAT_POSITION
        )
        client.add_event_handler(
            self.__on_update_chat_last_message,
            API.Types.UPDATE_CHAT_LAST_MESSAGE
        )
        client.add_event_handler(
            self.__on_update_chat_draft_message,
            API.Types.UPDATE_CHAT_DRAFT_MESSAGE
        )
        client.add_event_handler(
            self.__on_update_chat_title,
            API.Types.UPDATE_CHAT_TITLE
        )
        client.add_event_handler(
            self.__on_update_chat_photo,
            API.Types.UPDATE_CHAT_PHOTO
        )
        client.add_event_handler(
            self.__on_update_chat_permissions,
            API.Types.UPDATE_CHAT_PERMISSIONS
        )
        client.add_event_handler(
            self.__on_update_chat_read_inbox,
            API.Types.UPDATE_CHAT_READ_INBOX
        )
        client.add_event_handler(
            self.__on_update_chat_read_outbox,
            API.Types.UPDATE_CHAT_READ_OUTBOX
        )
        client.add_event_handler(
            self.__on_update_chat_reply_markup,
            API.Types.UPDATE_CHAT_REPLY_MARKUP
        )
        client.add_event_handler(
            self.__on_update_chat_notification_settings,
            API.Types.UPDATE_CHAT_NOTIFICATION_SETTINGS
        )
        client.add_event_handler(
            self.__on_update_chat_unread_mention_count,
            API.Types.UPDATE_CHAT_UNREAD_MENTION_COUNT
        )
        client.add_event_handler(
            self.__on_update_chat_default_disable_notification,
            API.Types.UPDATE_CHAT_DEFAULT_DISABLE_NOTIFICATION
        )
        client.add_event_handler(
            self.__on_update_chat_is_blocked,
            API.Types.UPDATE_CHAT_IS_BLOCKED
        )
        client.add_event_handler(
            self.__on_update_chat_is_marked_as_unread,
            API.Types.UPDATE_CHAT_IS_MARKED_AS_UNREAD
        )
        client.add_event_handler(
            self.__on_update_chat_has_scheduled_messages,
            API.Types.UPDATE_CHAT_HAS_SCHEDULED_MESSAGES
        )
        client.add_event_handler(
            self.__on_update_chat_message_ttl_setting,
            API.Types.UPDATE_CHAT_MESSAGE_TTL_SETTING
        )
        client.add_event_handler(
            self.__on_update_chat_voice_chat,
            API.Types.UPDATE_CHAT_VOICE_CHAT
        )

    async def get_option_value(self, name: str) -> typing.Union[str, int, bool, None]:
        value = self.options.get(name)

        if not bool(value):
            option_value = await self.client.api.get_option()

            if isinstance(option_value, OptionValueEmpty):
                value = None
            elif isinstance(option_value, OptionValueInteger):
                value = int(option_value.value)
            elif isinstance(option_value, (OptionValueString, OptionValueBoolean,)):
                value = option_value.value
            else:
                value = None

            self.options[name] = value

        return value

    async def get_main_list_chats(self, limit: int = 25) -> list[Chat]:
        cached_chats_count = len(self.main_chats_list)

        if not self.have_full_main_chats_list and limit > cached_chats_count:
            offset_order = TDLIB_MAX_INT
            offset_chat_id = 0

            if cached_chats_count > 0:
                last_chat = self.main_chats_list[-1]
                offset_order = last_chat.position.order
                offset_chat_id = last_chat.chat_id

            request_limit = max(100, limit - cached_chats_count)
            result = await self.client.api.get_chats(ChatListMain(), offset_order, offset_chat_id, request_limit)

            if len(result.chat_ids) == 0:
                self.have_full_main_chats_list = True

            return await self.get_main_list_chats(limit)

        return [self.chats.get(oc.chat_id) for oc in self.main_chats_list[:limit]]

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

    async def get_basic_group(self, basic_group_id: int, *, force_update: bool = True) -> BasicGroup:
        basic_group = self.basic_groups.get(basic_group_id)

        if not bool(basic_group) or force_update:
            basic_group = await self.client.api.get_basic_group(basic_group_id)
            self.basic_groups[basic_group_id] = basic_group

        return basic_group

    async def get_basic_group_full_info(self, basic_group_id: int, *, force_update: bool = True) -> BasicGroupFullInfo:
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

    async def get_supergroup_full_info(self, supergroup_id: int, *, force_update: bool = True) -> SupergroupFullInfo:
        supergroup_full_info = self.supergroups_full_info.get(supergroup_id)

        if not bool(supergroup_full_info) or force_update:
            supergroup_full_info = await self.client.api.get_supergroup_full_info(supergroup_id)
            self.supergroups_full_info[supergroup_id] = supergroup_full_info

        return supergroup_full_info

    async def get_secret_chat(self, secret_chat_id: int, *, force_update: bool = True) -> SecretChat:
        secret_chat = self.secret_chats.get(secret_chat_id)

        if not bool(secret_chat) or force_update:
            secret_chat = await self.client.api.get_secret_chat(secret_chat_id)
            self.secret_chats[secret_chat_id] = secret_chat

        return secret_chat

    def __set_chat_positions(self, chat: Chat, positions: list[ChatPosition]):
        for position in positions:
            if isinstance(position.list, ChatListMain):
                try:
                    self.main_chats_list.remove(OrderedChat(chat.id, position))
                except (KeyError, ValueError):
                    pass

        chat.positions = positions

        for position in positions:
            if isinstance(position.list, ChatListMain):
                self.main_chats_list.add(OrderedChat(chat.id, position))

    async def __on_update_option(self, _: Client, update: UpdateOption):
        if isinstance(update.value, OptionValueEmpty):
            value = None
        elif isinstance(update.value, OptionValueInteger):
            value = int(update.value.value)
        elif isinstance(update.value, (OptionValueString, OptionValueBoolean,)):
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
            new_positions = [update.position] + [p for p in chat.positions if not isinstance(p, ChatListMain)]
            self.__set_chat_positions(chat, new_positions)

    async def __on_update_chat_last_message(self, _: Client, update: UpdateChatLastMessage):
        chat = self.chats.get(update.chat_id)
        chat.last_message = update.last_message
        self.__set_chat_positions(chat, update.positions)

    async def __on_update_chat_draft_message(self, _: Client, update: UpdateChatDraftMessage):
        chat = self.chats.get(update.chat_id)
        if not hasattr(update, 'draft_message'):
            print(update)
        chat.draft_message = update.draft_message
        self.__set_chat_positions(chat, update.positions)

    async def __on_update_chat_title(self, _: Client, update: UpdateChatTitle):
        self.chats[update.chat_id].title = update.title

    async def __on_update_chat_photo(self, _: Client, update: UpdateChatPhoto):
        self.chats[update.chat_id].photo = update.photo

    async def __on_update_chat_permissions(self, _: Client, update: UpdateChatPermissions):
        self.chats[update.chat_id].permissions = update.permissions

    async def __on_update_chat_read_inbox(self, _: Client, update: UpdateChatReadInbox):
        self.chats[update.chat_id].unread_count = update.unread_count
        self.chats[update.chat_id].last_read_inbox_message_id = update.last_read_inbox_message_id

    async def __on_update_chat_read_outbox(self, _: Client, update: UpdateChatReadOutbox):
        self.chats[update.chat_id].last_read_outbox_message_id = update.last_read_outbox_message_id

    async def __on_update_chat_reply_markup(self, _: Client, update: UpdateChatReplyMarkup):
        self.chats[update.chat_id].reply_markup_message_id = update.reply_markup_message_id

    async def __on_update_chat_message_ttl_setting(self, _: Client, update: UpdateChatMessageTtlSetting):
        self.chats[update.chat_id].message_ttl_setting = update.message_ttl_setting

    async def __on_update_chat_notification_settings(self, _: Client, update: UpdateChatNotificationSettings):
        self.chats[update.chat_id].notification_settings = update.notification_settings

    async def __on_update_chat_unread_mention_count(self, _: Client, update: UpdateChatUnreadMentionCount):
        self.chats[update.chat_id].unread_mention_count = update.unread_mention_count

    async def __on_update_chat_default_disable_notification(
            self,
            _: Client,
            update: UpdateChatDefaultDisableNotification
    ):
        self.chats[update.chat_id].default_disable_notification = update.default_disable_notification

    async def __on_update_chat_is_blocked(self, _: Client, update: UpdateChatIsBlocked):
        self.chats[update.chat_id].is_blocked = update.is_blocked

    async def __on_update_chat_is_marked_as_unread(self, _: Client, update: UpdateChatIsMarkedAsUnread):
        self.chats[update.chat_id].is_marked_as_unread = update.is_marked_as_unread

    async def __on_update_chat_has_scheduled_messages(self, _: Client, update: UpdateChatHasScheduledMessages):
        self.chats[update.chat_id].has_scheduled_messages = update.has_scheduled_messages

    async def __on_update_chat_voice_chat(self, _: Client, update: UpdateChatVoiceChat):
        self.chats[update.chat_id].voice_chat = update.voice_chat
