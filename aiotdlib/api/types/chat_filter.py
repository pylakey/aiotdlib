# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ChatFilter(BaseObject):
    """
    Represents a filter of user chats
    
    :param title: The title of the filter; 1-12 characters without line feeds
    :type title: :class:`str`
    
    :param icon_name: The chosen icon name for short filter representation. If non-empty, must be one of "All", "Unread", "Unmuted", "Bots", "Channels", "Groups", "Private", "Custom", "Setup", "Cat", "Crown", "Favorite", "Flower", "Game", "Home", "Love", "Mask", "Party", "Sport", "Study", "Trade", "Travel", "Work", "Airplane", "Book", "Light", "Like", "Money", "Note", "Palette". If empty, use getChatFilterDefaultIconName to get default icon name for the filter
    :type icon_name: :class:`str`
    
    :param pinned_chat_ids: The chat identifiers of pinned chats in the filtered chat list. There can be up to GetOption("chat_filter_chosen_chat_count_max") pinned and always included non-secret chats and the same number of secret chats, but the limit can be increased with Telegram Premium
    :type pinned_chat_ids: :class:`list[int]`
    
    :param included_chat_ids: The chat identifiers of always included chats in the filtered chat list. There can be up to GetOption("chat_filter_chosen_chat_count_max") pinned and always included non-secret chats and the same number of secret chats, but the limit can be increased with Telegram Premium
    :type included_chat_ids: :class:`list[int]`
    
    :param excluded_chat_ids: The chat identifiers of always excluded chats in the filtered chat list. There can be up to GetOption("chat_filter_chosen_chat_count_max") always excluded non-secret chats and the same number of secret chats, but the limit can be increased with Telegram Premium
    :type excluded_chat_ids: :class:`list[int]`
    
    :param exclude_muted: True, if muted chats need to be excluded
    :type exclude_muted: :class:`bool`
    
    :param exclude_read: True, if read chats need to be excluded
    :type exclude_read: :class:`bool`
    
    :param exclude_archived: True, if archived chats need to be excluded
    :type exclude_archived: :class:`bool`
    
    :param include_contacts: True, if contacts need to be included
    :type include_contacts: :class:`bool`
    
    :param include_non_contacts: True, if non-contact users need to be included
    :type include_non_contacts: :class:`bool`
    
    :param include_bots: True, if bots need to be included
    :type include_bots: :class:`bool`
    
    :param include_groups: True, if basic groups and supergroups need to be included
    :type include_groups: :class:`bool`
    
    :param include_channels: True, if channels need to be included
    :type include_channels: :class:`bool`
    
    """

    ID: str = Field("chatFilter", alias="@type")
    title: str = Field(..., min_length=1, max_length=12)
    icon_name: str
    pinned_chat_ids: list[int]
    included_chat_ids: list[int]
    excluded_chat_ids: list[int]
    exclude_muted: bool
    exclude_read: bool
    exclude_archived: bool
    include_contacts: bool
    include_non_contacts: bool
    include_bots: bool
    include_groups: bool
    include_channels: bool

    @staticmethod
    def read(q: dict) -> ChatFilter:
        return ChatFilter.construct(**q)
