# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ChatEventLogFilters(BaseObject):
    """
    Represents a set of filters used to obtain a chat event log
    
    :param message_edits: True, if message edits need to be returned
    :type message_edits: :class:`bool`
    
    :param message_deletions: True, if message deletions need to be returned
    :type message_deletions: :class:`bool`
    
    :param message_pins: True, if pin/unpin events need to be returned
    :type message_pins: :class:`bool`
    
    :param member_joins: True, if members joining events need to be returned
    :type member_joins: :class:`bool`
    
    :param member_leaves: True, if members leaving events need to be returned
    :type member_leaves: :class:`bool`
    
    :param member_invites: True, if invited member events need to be returned
    :type member_invites: :class:`bool`
    
    :param member_promotions: True, if member promotion/demotion events need to be returned
    :type member_promotions: :class:`bool`
    
    :param member_restrictions: True, if member restricted/unrestricted/banned/unbanned events need to be returned
    :type member_restrictions: :class:`bool`
    
    :param info_changes: True, if changes in chat information need to be returned
    :type info_changes: :class:`bool`
    
    :param setting_changes: True, if changes in chat settings need to be returned
    :type setting_changes: :class:`bool`
    
    :param invite_link_changes: True, if changes to invite links need to be returned
    :type invite_link_changes: :class:`bool`
    
    :param video_chat_changes: True, if video chat actions need to be returned
    :type video_chat_changes: :class:`bool`
    
    """

    ID: str = Field("chatEventLogFilters", alias="@type")
    message_edits: bool
    message_deletions: bool
    message_pins: bool
    member_joins: bool
    member_leaves: bool
    member_invites: bool
    member_promotions: bool
    member_restrictions: bool
    info_changes: bool
    setting_changes: bool
    invite_link_changes: bool
    video_chat_changes: bool

    @staticmethod
    def read(q: dict) -> ChatEventLogFilters:
        return ChatEventLogFilters.construct(**q)
