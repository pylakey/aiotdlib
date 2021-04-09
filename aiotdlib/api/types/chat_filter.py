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
    
    Params:
        title (:class:`str`)
            The title of the filter; 1-12 characters without line feeds
        
        icon_name (:class:`str`)
            The icon name for short filter representation. If non-empty, must be one of "All", "Unread", "Unmuted", "Bots", "Channels", "Groups", "Private", "Custom", "Setup", "Cat", "Crown", "Favorite", "Flower", "Game", "Home", "Love", "Mask", "Party", "Sport", "Study", "Trade", "Travel", "Work". If empty, use getChatFilterDefaultIconName to get default icon name for the filter
        
        pinned_chat_ids (:obj:`list[int]`)
            The chat identifiers of pinned chats in the filtered chat list
        
        included_chat_ids (:obj:`list[int]`)
            The chat identifiers of always included chats in the filtered chat list
        
        excluded_chat_ids (:obj:`list[int]`)
            The chat identifiers of always excluded chats in the filtered chat list
        
        exclude_muted (:class:`bool`)
            True, if muted chats need to be excluded
        
        exclude_read (:class:`bool`)
            True, if read chats need to be excluded
        
        exclude_archived (:class:`bool`)
            True, if archived chats need to be excluded
        
        include_contacts (:class:`bool`)
            True, if contacts need to be included
        
        include_non_contacts (:class:`bool`)
            True, if non-contact users need to be included
        
        include_bots (:class:`bool`)
            True, if bots need to be included
        
        include_groups (:class:`bool`)
            True, if basic groups and supergroups need to be included
        
        include_channels (:class:`bool`)
            True, if channels need to be included
        
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
