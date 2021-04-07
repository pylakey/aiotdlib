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
    
    Params:
        message_edits (:class:`bool`)
            True, if message edits should be returned
        
        message_deletions (:class:`bool`)
            True, if message deletions should be returned
        
        message_pins (:class:`bool`)
            True, if pin/unpin events should be returned
        
        member_joins (:class:`bool`)
            True, if members joining events should be returned
        
        member_leaves (:class:`bool`)
            True, if members leaving events should be returned
        
        member_invites (:class:`bool`)
            True, if invited member events should be returned
        
        member_promotions (:class:`bool`)
            True, if member promotion/demotion events should be returned
        
        member_restrictions (:class:`bool`)
            True, if member restricted/unrestricted/banned/unbanned events should be returned
        
        info_changes (:class:`bool`)
            True, if changes in chat information should be returned
        
        setting_changes (:class:`bool`)
            True, if changes in chat settings should be returned
        
        invite_link_changes (:class:`bool`)
            True, if changes to invite links should be returned
        
        voice_chat_changes (:class:`bool`)
            True, if voice chat actions should be returned
        
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
    voice_chat_changes: bool

    @staticmethod
    def read(q: dict) -> ChatEventLogFilters:
        return ChatEventLogFilters.construct(**q)
